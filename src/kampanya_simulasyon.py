"""G1 - Dijital pazarlama kampanya performansı simülasyonu (v3).

Amaç : 5 kanal x 52 hafta = 260 satırlık sentetik kampanya verisi üretmek.
Çıktı: data/kampanya-performans.csv
Kural: SEED sabit olduğu için betik her çalıştığında BİREBİR aynı dosyayı üretir.
       Dosya yazılmadan önce veri sözlüğündeki TÜM kurallar kontrol edilir;
       bir kural bozuksa betik hata verir ve dosya yazılmaz.
       Dosya yazıldıktan sonra da başlık satırı ve satır sayısı yeniden kontrol edilir.

Parametreler (KANALLAR) ve formüller docs/veri-sozlugu-g1.md içindeki
"Simülasyon parametreleri" bölümüyle birebir aynıdır.

Çalıştırma (deponun kök klasöründe):
    python src/kampanya_simulasyon.py
"""
import csv
import random
import re
from datetime import date, datetime, timedelta
from pathlib import Path

SEED = 42             # sabit tohum: aynı tohum -> aynı dosya
HAFTA_SAYISI = 52     # kaç hafta üretilecek
BASLANGIC = date(2025, 10, 6)  # bir Pazartesi
BITIS = BASLANGIC + timedelta(weeks=HAFTA_SAYISI - 1)

# Her kanal için sabit aralıklar
# gosterim: haftalık gösterim | ctr: tıklama oranı | cvr: tıklamadan dönüşüm oranı
# cpc: tıklama başına maliyet (TL) | sepet: dönüşüm başına ortalama gelir (TL)
KANALLAR = {
    "Google Ads": {"gosterim": (40000, 120000), "ctr": (0.020, 0.060), "cvr": (0.020, 0.060), "cpc": (3.0, 8.0), "sepet": (400, 900)},
    "Meta Ads":   {"gosterim": (60000, 180000), "ctr": (0.010, 0.030), "cvr": (0.010, 0.040), "cpc": (2.0, 5.0), "sepet": (300, 700)},
    "TikTok Ads": {"gosterim": (80000, 250000), "ctr": (0.005, 0.020), "cvr": (0.005, 0.025), "cpc": (1.5, 4.0), "sepet": (250, 600)},
    "E-posta":    {"gosterim": (5000, 30000),   "ctr": (0.020, 0.080), "cvr": (0.030, 0.080), "cpc": (0.3, 1.0), "sepet": (350, 800)},
    "SEO":        {"gosterim": (20000, 90000),  "ctr": (0.020, 0.050), "cvr": (0.020, 0.050), "cpc": (0.5, 1.5), "sepet": (400, 900)},
}

BASLIK = ["kampanya_id", "tarih", "kanal", "gosterim", "tiklama", "donusum", "harcama_tl", "gelir_tl"]

# Veri sözlüğündeki genel sınırlar
GOSTERIM_MIN, GOSTERIM_MAX = 5000, 250000

KOK = Path(__file__).resolve().parent.parent
HEDEF = KOK / "data" / "kampanya-performans.csv"


def tutar_yaz(x):
    """Tutarı HER ZAMAN tam 2 ondalık basamakla metne çevirir (4717.0 -> '4717.00')."""
    return f"{x:.2f}"


def satirlari_uret():
    """Satırları METİN olarak döndürür: CSV'ye yazılacak hâliyle birebir aynı.

    Her satırda rastgele sayılar şu SIRAYLA çekilir: gosterim, ctr, cvr, cpc, sepet.
    Satır sırası: önce hafta, her haftada kanallar KANALLAR sırasıyla.
    """
    rng = random.Random(SEED)  # kendi rastgele üretecimiz, başka koddan etkilenmez
    satirlar = []
    sayac = 1
    for hafta in range(HAFTA_SAYISI):
        tarih = BASLANGIC + timedelta(weeks=hafta)
        for kanal, p in KANALLAR.items():
            gosterim = rng.randint(*p["gosterim"])
            tiklama = max(1, int(gosterim * rng.uniform(*p["ctr"])))
            donusum = int(tiklama * rng.uniform(*p["cvr"]))
            harcama = round(tiklama * rng.uniform(*p["cpc"]), 2)
            gelir = round(donusum * rng.uniform(*p["sepet"]), 2)
            satirlar.append([f"K{sayac:03d}", tarih.isoformat(), kanal,
                             str(gosterim), str(tiklama), str(donusum),
                             tutar_yaz(harcama), tutar_yaz(gelir)])
            sayac += 1
    return satirlar


def hata(mesaj):
    raise ValueError(mesaj)


def dogrula(satirlar):
    """docs/veri-sozlugu-g1.md içindeki TÜM kuralların kontrolü."""
    if len(satirlar) < 100:
        hata("en az 100 satır olmalı")
    if len(satirlar) != HAFTA_SAYISI * len(KANALLAR):
        hata("satır sayısı kanal x hafta sayısına eşit olmalı")

    idler = [s[0] for s in satirlar]
    if len(set(idler)) != len(idler):
        hata("kampanya_id benzersiz olmalı")
    beklenen_idler = {f"K{i:03d}" for i in range(1, len(satirlar) + 1)}
    if set(idler) != beklenen_idler:
        hata("kampanya_id değerleri K001'den başlayarak sıralı olmalı")

    kanal_sayilari = {}
    for s in satirlar:
        kid, tarih, kanal, gosterim, tiklama, donusum, harcama, gelir = s
        if not re.fullmatch(r"K\d{3}", kid):
            hata(f"kampanya_id biçimi hatalı: {s}")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", tarih):
            hata(f"tarih biçimi yyyy-mm-dd olmalı: {s}")
        tarih_degeri = datetime.strptime(tarih, "%Y-%m-%d").date()
        if tarih_degeri.weekday() != 0:
            hata(f"tarih bir Pazartesi olmalı: {s}")
        if not (BASLANGIC <= tarih_degeri <= BITIS):
            hata(f"tarih sözlükteki aralıkta olmalı: {s}")
        if kanal not in KANALLAR:
            hata(f"geçersiz kanal: {s}")
        kanal_sayilari[kanal] = kanal_sayilari.get(kanal, 0) + 1
        for ad, deger in (("gosterim", gosterim), ("tiklama", tiklama), ("donusum", donusum)):
            if not re.fullmatch(r"\d+", deger):
                hata(f"{ad} tam sayı olmalı: {s}")
        for ad, deger in (("harcama_tl", harcama), ("gelir_tl", gelir)):
            if not re.fullmatch(r"\d+\.\d{2}", deger):
                hata(f"{ad} tam 2 ondalık basamaklı olmalı: {s}")
        g, t, d = int(gosterim), int(tiklama), int(donusum)
        if not (GOSTERIM_MIN <= g <= GOSTERIM_MAX):
            hata(f"gösterim aralık dışı: {s}")
        if not (1 <= t <= g):
            hata(f"tıklama 1 ile gösterim arasında olmalı: {s}")
        if not (0 <= d <= t):
            hata(f"dönüşüm 0 ile tıklama arasında olmalı: {s}")
        if float(harcama) <= 0:
            hata(f"harcama sıfırdan büyük olmalı: {s}")
        if float(gelir) < 0:
            hata(f"gelir negatif olamaz: {s}")
        if d == 0 and float(gelir) != 0:
            hata(f"dönüşüm 0 ise gelir_tl 0.00 olmalı: {s}")

    if len(KANALLAR) != 5 or set(kanal_sayilari) != set(KANALLAR):
        hata("veri tam olarak sözlükteki 5 kanalı içermeli")
    if any(n != HAFTA_SAYISI for n in kanal_sayilari.values()):
        hata("her kanalda hafta sayısı kadar satır olmalı")


def dosyayi_kontrol_et(yol, satir_sayisi):
    """Yazılan dosyayı geri okuyup başlığı ve satır sayısını doğrular."""
    with open(yol, encoding="utf-8", newline="") as f:
        satirlar = list(csv.reader(f))
    if satirlar[0] != BASLIK:
        hata("yazılan dosyanın başlık satırı veri sözlüğüyle uyuşmuyor")
    if len(satirlar) - 1 != satir_sayisi:
        hata("yazılan dosyadaki satır sayısı beklenenle uyuşmuyor")


def main():
    satirlar = satirlari_uret()
    dogrula(satirlar)  # hata varsa buradan öteye geçilmez, dosya yazılmaz
    HEDEF.parent.mkdir(exist_ok=True)
    with open(HEDEF, "w", newline="", encoding="utf-8") as f:
        yazici = csv.writer(f, lineterminator="\n")  # her işletim sisteminde aynı satır sonu
        yazici.writerow(BASLIK)
        yazici.writerows(satirlar)
    dosyayi_kontrol_et(HEDEF, len(satirlar))
    print(f"{len(satirlar)} satır yazıldı: {HEDEF}")


if __name__ == "__main__":
    main()
