"""G1 - Dijital pazarlama kampanya performansı simülasyonu.

Amaç : 5 kanal x 26 hafta = 130 satırlık sentetik kampanya verisi üretmek.
Çıktı: data/kampanya-performans.csv
Kural: SEED sabit olduğu için betik her çalıştığında BİREBİR aynı dosyayı üretir.

Çalıştırma (deponun kök klasöründe):
    python src/kampanya_simulasyon.py
"""
import csv
import random
from datetime import date, timedelta
from pathlib import Path

SEED = 42            # sabit tohum: aynı tohum -> aynı dosya
HAFTA_SAYISI = 26    # kaç hafta üretilecek
BASLANGIC = date(2026, 3, 2)  # bir Pazartesi

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

KOK = Path(__file__).resolve().parent.parent
HEDEF = KOK / "data" / "kampanya-performans.csv"


def satirlari_uret():
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
                             gosterim, tiklama, donusum, harcama, gelir])
            sayac += 1
    return satirlar


def dogrula(satirlar):
    """Veri sözlüğündeki kuralların kodla kontrolü."""
    assert len(satirlar) >= 100, "en az 100 satır olmalı"
    assert len({s[2] for s in satirlar}) >= 4, "en az 4 farklı kanal olmalı"
    for s in satirlar:
        _, _, _, gosterim, tiklama, donusum, harcama, gelir = s
        assert tiklama <= gosterim, f"tıklama gösterimden fazla: {s}"
        assert donusum <= tiklama, f"dönüşüm tıklamadan fazla: {s}"
        assert harcama > 0 and gelir >= 0, f"negatif/sıfır tutar: {s}"


def main():
    satirlar = satirlari_uret()
    dogrula(satirlar)
    HEDEF.parent.mkdir(exist_ok=True)
    with open(HEDEF, "w", newline="", encoding="utf-8") as f:
        yazici = csv.writer(f, lineterminator="\n")  # her işletim sisteminde aynı satır sonu
        yazici.writerow(BASLIK)
        yazici.writerows(satirlar)
    print(f"{len(satirlar)} satır yazıldı: {HEDEF}")


if __name__ == "__main__":
    main()
