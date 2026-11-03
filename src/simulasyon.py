"""Görev 2 için tekrarlanabilir parametreli kampanya simülasyonu.

Varsayılan çıktı: data/kampanya-simulasyon-g2.csv
Örnek: python src/simulasyon.py --hafta_sayisi 10 --kampanya_sayisi 3
       python src/simulasyon.py --kanallar "E-posta" SEO
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

BASLIK = [
    "kampanya_id",
    "tarih",
    "kanal",
    "gosterim",
    "tiklama",
    "donusum",
    "harcama_tl",
    "gelir_tl",
]
KOK = Path(__file__).resolve().parent.parent
HEDEF = KOK / "data" / "kampanya-simulasyon-g2.csv"


def parametreleri_dogrula(
    tohum: int,
    hafta_sayisi: int,
    kampanya_sayisi: int | None,
    baslangic_tarihi: date,
    kanal_adlari: list[str] | None = None,
) -> None:
    if tohum < 0:
        raise ValueError("tohum sıfır veya daha büyük olmalıdır")
    if not 1 <= hafta_sayisi <= 104:
        raise ValueError("hafta_sayisi 1 ile 104 arasında olmalıdır")
    if baslangic_tarihi.weekday() != 0:
        raise ValueError("baslangic_tarihi bir Pazartesi olmalıdır")
    secili_kanallari_belirle(kampanya_sayisi, kanal_adlari)


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
) -> list[list[str]]:
    parametreleri_dogrula(
        tohum, hafta_sayisi, kampanya_sayisi, baslangic_tarihi, kanal_adlari
    )
    rng = random.Random(tohum)
    secili_kanallar = secili_kanallari_belirle(kampanya_sayisi, kanal_adlari)
    kampanya_sayisi = len(secili_kanallar)
    satirlar = []
    sayac = 1

    for hafta in range(hafta_sayisi):
        tarih = baslangic_tarihi + timedelta(weeks=hafta)
        for kanal, araliklar in secili_kanallar:
            gosterim = rng.randint(*araliklar["gosterim"])
            tiklama = max(1, int(gosterim * rng.uniform(*araliklar["ctr"])))
            donusum = int(tiklama * rng.uniform(*araliklar["cvr"]))
            harcama = round(tiklama * rng.uniform(*araliklar["cpc"]), 2)
            gelir = (
                round(donusum * rng.uniform(*araliklar["sepet"]), 2)
                if donusum > 0
                else 0.00
            )
            satirlar.append(
                [
                    f"K{sayac:03d}",
                    tarih.isoformat(),
                    kanal,
                    str(gosterim),
                    str(tiklama),
                    str(donusum),
                    f"{harcama:.2f}",
                    f"{gelir:.2f}",
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
    parametreleri_dogrula(
        tohum, hafta_sayisi, kampanya_sayisi, baslangic_tarihi, kanal_adlari
    )
    kanallar = secili_kanallari_belirle(kampanya_sayisi, kanal_adlari)
    kampanya_sayisi = len(kanallar)
    beklenen_satir = hafta_sayisi * kampanya_sayisi
    if len(satirlar) != beklenen_satir:
        raise ValueError(f"satır sayısı {beklenen_satir} olmalı; bulunan {len(satirlar)}")

    beklenen_idler = {f"K{i:03d}" for i in range(1, beklenen_satir + 1)}
    bulunan_idler = set()
    bulunan_ciftler = set()
    for sira, satir in enumerate(satirlar):
        if len(satir) != len(BASLIK) or any(deger == "" for deger in satir):
            raise ValueError(f"{sira + 1}. satırda eksik veya hatalı alan sayısı var")

        kampanya_id, tarih_metni, kanal, gosterim_metni, tiklama_metni, donusum_metni, harcama, gelir = satir
        if not re.fullmatch(r"K\d{3}", kampanya_id):
            raise ValueError(f"kampanya_id biçimi hatalı: {kampanya_id}")
        if kampanya_id != f"K{sira + 1:03d}":
            raise ValueError(f"kampanya_id sırası hatalı: {kampanya_id}")
        if kampanya_id in bulunan_idler:
            raise ValueError(f"kampanya_id yineleniyor: {kampanya_id}")
        bulunan_idler.add(kampanya_id)

        if kanal not in dict(kanallar):
            raise ValueError(f"geçersiz kanal: {kanal}")
        try:
            tarih = date.fromisoformat(tarih_metni)
            gosterim = int(gosterim_metni)
            tiklama = int(tiklama_metni)
            donusum = int(donusum_metni)
        except ValueError as exc:
            raise ValueError(f"satırda tarih veya tam sayı biçimi hatalı: {satir}") from exc

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

        araliklar = dict(kanallar)[kanal]
        gosterim_min, gosterim_max = araliklar["gosterim"]
        if not gosterim_min <= gosterim <= gosterim_max:
            raise ValueError(f"gosterim kanal aralığı dışında: {satir}")
        if not 1 <= tiklama <= gosterim:
            raise ValueError(f"tiklama 1 ile gosterim arasında olmalı: {satir}")
        if not 0 <= donusum <= tiklama:
            raise ValueError(f"donusum 0 ile tiklama arasında olmalı: {satir}")
        if not re.fullmatch(r"\d+\.\d{2}", harcama):
            raise ValueError(f"harcama_tl tam 2 ondalık basamaklı olmalı: {satir}")
        if not re.fullmatch(r"\d+\.\d{2}", gelir):
            raise ValueError(f"gelir_tl tam 2 ondalık basamaklı olmalı: {satir}")
        if float(harcama) <= 0 or float(gelir) < 0:
            raise ValueError(f"tutar aralıkları şemaya uymuyor: {satir}")
        if donusum == 0 and gelir != "0.00":
            raise ValueError(f"donusum sıfırsa gelir_tl 0.00 olmalı: {satir}")

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
    parser = argparse.ArgumentParser(description="G2 kampanya simülasyonu")
    parser.add_argument("--tohum", type=int, default=42)
    parser.add_argument("--hafta_sayisi", "--hafta-sayisi", type=int, default=52)
    parser.add_argument("--kampanya_sayisi", "--kampanya-sayisi", type=int)
    parser.add_argument(
        "--kanallar",
        nargs="+",
        choices=list(KANALLAR),
        help="Simüle edilecek kanallar; örnek: --kanallar E-posta SEO",
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
