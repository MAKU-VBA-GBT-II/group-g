"""Duyuru 10 (Çok Ajanlı Şirket Programı) için genişletilmiş parametreli kampanya simülasyonu.

Web kaynaklarıyla (Meta Ad Library & Google Trends) eşleşen alanlar:
- kategori (sektör/ürün grubu)
- hedef_bolge (coğrafi pazar hedefi)
- trend_kelime (Google Trends arama terimi)
- rakip_cpa_tl (piyasa referans edinme maliyeti)
- simule_cpa_tl (kampanyanın hesaplanan edinme maliyeti)

Dışarıdan liste ve aralık parametreleri:
--kategoriler Moda Elektronik Kozmetik
--bolgeler TR-Marmara TR-Ege
--butce_araligi 500 15000
--hedef_cpa_max 120.00

Varsayılan çıktı: data/kampanya-simulasyon-g3.csv
"""

import argparse
import csv
import random
import re
from datetime import date, timedelta
from pathlib import Path


KANALLAR = {
    "Google Ads": {
        "gosterim": (40_000, 120_000),
        "ctr": (0.020, 0.060),
        "cvr": (0.020, 0.060),
        "cpc": (3.00, 8.00),
        "sepet": (400, 900),
    },
    "Meta Ads": {
        "gosterim": (60_000, 180_000),
        "ctr": (0.010, 0.030),
        "cvr": (0.010, 0.040),
        "cpc": (2.00, 5.00),
        "sepet": (300, 700),
    },
    "TikTok Ads": {
        "gosterim": (80_000, 250_000),
        "ctr": (0.005, 0.020),
        "cvr": (0.005, 0.025),
        "cpc": (1.50, 4.00),
        "sepet": (250, 600),
    },
    "E-posta": {
        "gosterim": (5_000, 30_000),
        "ctr": (0.020, 0.080),
        "cvr": (0.030, 0.080),
        "cpc": (0.30, 1.00),
        "sepet": (350, 800),
    },
    "SEO": {
        "gosterim": (20_000, 90_000),
        "ctr": (0.020, 0.050),
        "cvr": (0.020, 0.050),
        "cpc": (0.50, 1.50),
        "sepet": (400, 900),
    },
}

KATEGORILER = ["Moda", "Elektronik", "Kozmetik", "Ev-Yasam", "Spor"]
BOLGELER = ["TR-Marmara", "TR-Ege", "TR-Ic-Anadolu", "TR-Akdeniz", "TR-Genel"]
TREND_KELIMELER = ["indirim", "yeni-sezon", "kampanya", "firsat", "trend-urun"]

BASLIK = [
    "kampanya_id",
    "tarih",
    "kanal",
    "kategori",
    "hedef_bolge",
    "trend_kelime",
    "gosterim",
    "tiklama",
    "donusum",
    "harcama_tl",
    "gelir_tl",
    "rakip_cpa_tl",
    "simule_cpa_tl",
]

KOK = Path(__file__).resolve().parent.parent
HEDEF = KOK / "data" / "kampanya-simulasyon-g3.csv"


def parametreleri_dogrula(
    tohum: int,
    hafta_sayisi: int,
    kampanya_sayisi: int | None,
    baslangic_tarihi: date,
    kanal_adlari: list[str] | None = None,
    kategoriler: list[str] | None = None,
    bolgeler: list[str] | None = None,
    butce_araligi: list[float] | None = None,
    hedef_cpa_max: float | None = None,
) -> None:
    if tohum < 0:
        raise ValueError("tohum sıfır veya daha büyük olmalıdır")
    if not 1 <= hafta_sayisi <= 104:
        raise ValueError("hafta_sayisi 1 ile 104 arasında olmalıdır")
    if baslangic_tarihi.weekday() != 0:
        raise ValueError("baslangic_tarihi bir Pazartesi olmalıdır")
    secili_kanallari_belirle(kampanya_sayisi, kanal_adlari)

    if butce_araligi is not None:
        if len(butce_araligi) != 2 or butce_araligi[0] <= 0 or butce_araligi[0] > butce_araligi[1]:
            raise ValueError("butce_araligi pozitif ve [min, max] biçiminde olmalıdır")
    if hedef_cpa_max is not None and hedef_cpa_max <= 0:
        raise ValueError("hedef_cpa_max sıfırdan büyük olmalıdır")


def secili_kanallari_belirle(
    kampanya_sayisi: int | None, kanal_adlari: list[str] | None
) -> list[tuple[str, dict[str, tuple[int, int] | tuple[float, float]]]]:
    if kanal_adlari is None:
        sayi = len(KANALLAR) if kampanya_sayisi is None else kampanya_sayisi
        if not 1 <= sayi <= len(KANALLAR):
            raise ValueError(f"kampanya_sayisi 1 ile {len(KANALLAR)} arasında olmalıdır")
        return list(KANALLAR.items())[:sayi]

    if not kanal_adlari:
        raise ValueError("en az bir kanal seçilmelidir")
    if len(set(kanal_adlari)) != len(kanal_adlari):
        raise ValueError("kanal listesinde yinelenen değer olamaz")
    bilinmeyenler = [ad for ad in kanal_adlari if ad not in KANALLAR]
    if bilinmeyenler:
        raise ValueError(f"geçersiz kanal adı: {', '.join(bilinmeyenler)}")
    if kampanya_sayisi is not None and kampanya_sayisi != len(kanal_adlari):
        raise ValueError(
            "kampanya_sayisi, --kanallar ile seçilen kanal sayısıyla eşleşmelidir"
        )
    return [(ad, KANALLAR[ad]) for ad in kanal_adlari]


def satirlari_uret(
    tohum: int,
    hafta_sayisi: int,
    kampanya_sayisi: int | None,
    baslangic_tarihi: date,
    kanal_adlari: list[str] | None = None,
    kategoriler: list[str] | None = None,
    bolgeler: list[str] | None = None,
    butce_araligi: list[float] | None = None,
    hedef_cpa_max: float | None = None,
) -> list[list[str]]:
    parametreleri_dogrula(
        tohum,
        hafta_sayisi,
        kampanya_sayisi,
        baslangic_tarihi,
        kanal_adlari,
        kategoriler,
        bolgeler,
        butce_araligi,
        hedef_cpa_max,
    )
    rng = random.Random(tohum)
    secili_kanallar = secili_kanallari_belirle(kampanya_sayisi, kanal_adlari)
    aktif_kategoriler = kategoriler if kategoriler else KATEGORILER
    aktif_bolgeler = bolgeler if bolgeler else BOLGELER

    satirlar = []
    sayac = 1

    for hafta in range(hafta_sayisi):
        tarih = baslangic_tarihi + timedelta(weeks=hafta)
        for kanal, araliklar in secili_kanallar:
            kategori = aktif_kategoriler[(sayac - 1) % len(aktif_kategoriler)]
            hedef_bolge = aktif_bolgeler[(sayac - 1) % len(aktif_bolgeler)]
            trend_kelime = rng.choice(TREND_KELIMELER)

            gosterim = rng.randint(*araliklar["gosterim"])
            tiklama = max(1, int(gosterim * rng.uniform(*araliklar["ctr"])))
            donusum = int(tiklama * rng.uniform(*araliklar["cvr"]))
            
            cpc = rng.uniform(*araliklar["cpc"])
            harcama = round(tiklama * cpc, 2)
            if butce_araligi is not None:
                harcama = max(butce_araligi[0], min(butce_araligi[1], harcama))

            gelir = (
                round(donusum * rng.uniform(*araliklar["sepet"]), 2)
                if donusum > 0
                else 0.00
            )

            # Rakiplerin piyasa CPA'sı ve simüle edilen gerçek CPA (TL)
            rakip_cpa = round(rng.uniform(35.00, 110.00), 2)
            simule_cpa = round(harcama / donusum, 2) if donusum > 0 else round(harcama, 2)

            satirlar.append(
                [
                    f"K{sayac:03d}",
                    tarih.isoformat(),
                    kanal,
                    kategori,
                    hedef_bolge,
                    trend_kelime,
                    str(gosterim),
                    str(tiklama),
                    str(donusum),
                    f"{harcama:.2f}",
                    f"{gelir:.2f}",
                    f"{rakip_cpa:.2f}",
                    f"{simule_cpa:.2f}",
                ]
            )
            sayac += 1

    return satirlar


def satirlari_dogrula(
    satirlar: list[list[str]],
    tohum: int,
    hafta_sayisi: int,
    kampanya_sayisi: int | None,
    baslangic_tarihi: date,
    kanal_adlari: list[str] | None = None,
) -> None:
    kanallar = secili_kanallari_belirle(kampanya_sayisi, kanal_adlari)
    kampanya_sayisi = len(kanallar)
    beklenen_satir = hafta_sayisi * kampanya_sayisi

    if len(satirlar) != beklenen_satir:
        raise ValueError(
            f"satır sayısı beklenenle uyuşmuyor: beklenen {beklenen_satir}, bulunan {len(satirlar)}"
        )

    beklenen_idler = [f"K{i:03d}" for i in range(1, beklenen_satir + 1)]
    bulunan_idler = []
    bulunan_ciftler = set()

    for sira, satir in enumerate(satirlar):
        if len(satir) != len(BASLIK):
            raise ValueError(f"satırdaki sütun sayısı {len(BASLIK)} olmalıdır: {satir}")

        (
            kampanya_id,
            tarih_metni,
            kanal,
            kategori,
            hedef_bolge,
            trend_kelime,
            gosterim_metni,
            tiklama_metni,
            donusum_metni,
            harcama,
            gelir,
            rakip_cpa,
            simule_cpa,
        ) = satir

        bulunan_idler.append(kampanya_id)
        try:
            tarih = date.fromisoformat(tarih_metni)
            gosterim = int(gosterim_metni)
            tiklama = int(tiklama_metni)
            donusum = int(donusum_metni)
        except ValueError as exc:
            raise ValueError(f"satırda tarih veya sayı biçimi hatalı: {satir}") from exc

        hafta = sira // kampanya_sayisi
        beklenen_tarih = baslangic_tarihi + timedelta(weeks=hafta)
        beklenen_kanal = kanallar[sira % kampanya_sayisi][0]

        if tarih.isoformat() != tarih_metni or tarih.weekday() != 0:
            raise ValueError(f"tarih YYYY-MM-DD biçiminde Pazartesi olmalı: {tarih_metni}")
        if tarih != beklenen_tarih or kanal != beklenen_kanal:
            raise ValueError(f"hafta ve kanal sıralaması beklenenle uyuşmuyor: {satir}")

        cift = (tarih, kanal)
        if cift in bulunan_ciftler:
            raise ValueError(f"tarih-kanal çifti yineleniyor: {tarih_metni}, {kanal}")
        bulunan_ciftler.add(cift)

        if not 1 <= tiklama <= gosterim:
            raise ValueError(f"tiklama 1 ile gosterim arasında olmalı: {satir}")
        if not 0 <= donusum <= tiklama:
            raise ValueError(f"donusum 0 ile tiklama arasında olmalı: {satir}")
        if not re.fullmatch(r"\d+\.\d{2}", harcama) or not re.fullmatch(r"\d+\.\d{2}", gelir):
            raise ValueError(f"tutar alanları tam 2 ondalık basamaklı olmalı: {satir}")
        if not re.fullmatch(r"\d+\.\d{2}", rakip_cpa) or not re.fullmatch(r"\d+\.\d{2}", simule_cpa):
            raise ValueError(f"CPA alanları tam 2 ondalık basamaklı olmalı: {satir}")

    if bulunan_idler != beklenen_idler:
        raise ValueError("kampanya_id değerleri K001'den başlayarak sıralı olmalı")
    if len(bulunan_ciftler) != beklenen_satir:
        raise ValueError("her hafta-kanal çifti tam bir kez bulunmalı")


def dosyayi_yaz_ve_dogrula(
    satirlar: list[list[str]],
    hedef: Path,
    tohum: int,
    hafta_sayisi: int,
    kampanya_sayisi: int | None,
    baslangic_tarihi: date,
    kanal_adlari: list[str] | None = None,
) -> None:
    hedef.parent.mkdir(parents=True, exist_ok=True)
    with hedef.open("w", encoding="utf-8", newline="") as dosya:
        yazici = csv.writer(dosya, lineterminator="\n")
        yazici.writerow(BASLIK)
        yazici.writerows(satirlar)

    with hedef.open("r", encoding="utf-8", newline="") as dosya:
        icerik = list(csv.reader(dosya))
    if not icerik or icerik[0] != BASLIK:
        raise ValueError("yazılan CSV başlığı veri sözlüğüyle uyuşmuyor")
    satirlari_dogrula(
        icerik[1:],
        tohum,
        hafta_sayisi,
        kampanya_sayisi,
        baslangic_tarihi,
        kanal_adlari,
    )


def argumanlari_oku() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Çok Ajanlı Sistem G3 Kampanya Simülasyonu")
    parser.add_argument("--tohum", type=int, default=42)
    parser.add_argument("--hafta_sayisi", "--hafta-sayisi", type=int, default=52)
    parser.add_argument("--kampanya_sayisi", "--kampanya-sayisi", type=int)
    parser.add_argument(
        "--kanallar",
        nargs="+",
        choices=list(KANALLAR),
        help="Simüle edilecek kanallar; örnek: --kanallar Google Ads Meta Ads",
    )
    parser.add_argument(
        "--kategoriler",
        nargs="+",
        help="Dışarıdan verilecek hedef ürün/hizmet kategorileri listesi",
    )
    parser.add_argument(
        "--bolgeler",
        nargs="+",
        help="Dışarıdan verilecek coğrafi hedef bölge listesi",
    )
    parser.add_argument(
        "--butce_araligi",
        nargs=2,
        type=float,
        metavar=("MIN_TL", "MAX_TL"),
        help="Harcama bütçesi için [min, max] aralığı",
    )
    parser.add_argument(
        "--hedef_cpa_max",
        type=float,
        help="Ajan 3 denetim eşiği: izin verilen azami hedef CPA (TL)",
    )
    parser.add_argument(
        "--baslangic_tarihi",
        "--baslangic-tarihi",
        default="2025-10-06",
        help="YYYY-MM-DD biçiminde bir Pazartesi",
    )
    parser.add_argument("--cikti", type=Path, default=HEDEF)
    args = parser.parse_args()
    try:
        args.baslangic_tarihi = date.fromisoformat(args.baslangic_tarihi)
    except ValueError as exc:
        raise ValueError("baslangic_tarihi YYYY-MM-DD biçiminde olmalıdır") from exc
    return args


def main() -> None:
    args = argumanlari_oku()
    satirlar = satirlari_uret(
        args.tohum,
        args.hafta_sayisi,
        args.kampanya_sayisi,
        args.baslangic_tarihi,
        args.kanallar,
        args.kategoriler,
        args.bolgeler,
        args.butce_araligi,
        args.hedef_cpa_max,
    )
    satirlari_dogrula(
        satirlar,
        args.tohum,
        args.hafta_sayisi,
        args.kampanya_sayisi,
        args.baslangic_tarihi,
        args.kanallar,
    )
    dosyayi_yaz_ve_dogrula(
        satirlar,
        args.cikti,
        args.tohum,
        args.hafta_sayisi,
        args.kampanya_sayisi,
        args.baslangic_tarihi,
        args.kanallar,
    )
    print(f"{len(satirlar)} satır yazıldı ve doğrulandı: {args.cikti}")


if __name__ == "__main__":
    main()
