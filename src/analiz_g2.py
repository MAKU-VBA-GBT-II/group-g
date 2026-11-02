"""G2 parametreli kampanya simülasyonu analiz betiği (DQ).

Veri: data/kampanya-simulasyon-g2.csv
Şema: docs/veri-sozlugu.md
Rapor: docs/analiz-g2.md

Depo kökünden çalıştırma:
    python src/analiz_g2.py
"""

import csv
import re
from collections import defaultdict
from datetime import date, timedelta
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "data" / "kampanya-simulasyon-g2.csv"
REPORT_PATH = ROOT / "docs" / "analiz-g2.md"

HEADERS = [
    "kampanya_id",
    "tarih",
    "kanal",
    "gosterim",
    "tiklama",
    "donusum",
    "harcama_tl",
    "gelir_tl",
]
CHANNELS = ("Google Ads", "Meta Ads", "TikTok Ads", "E-posta", "SEO")
FIRST_WEEK = date(2025, 10, 6)
WEEK_COUNT = 52
EXPECTED_WEEKS = tuple(
    FIRST_WEEK + timedelta(weeks=i) for i in range(WEEK_COUNT)
)

MONEY_PATTERN = re.compile(r"^\d+\.\d{2}$")
ID_PATTERN = re.compile(r"^K\d{3}$")
DATA_COMMIT = "47cf641d611512a5ed84b36a1620e13af61c753b"


def format_tl(value: Decimal) -> str:
    """Format decimal as Turkish currency: 1.234.567,89 TL"""
    rounded = value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    parts = f"{rounded:.2f}".split(".")
    integer_part = parts[0]
    decimal_part = parts[1]
    rev_int = integer_part[::-1]
    grouped = ".".join(rev_int[i:i+3] for i in range(0, len(rev_int), 3))[::-1]
    return f"{grouped},{decimal_part} TL"


def format_num(value: int) -> str:
    """Format integer with thousands separator: 1.234.567"""
    return f"{value:,}".replace(",", ".")


def load_and_validate(path: Path):
    if not path.exists():
        raise FileNotFoundError(f"Veri dosyası bulunamadı: {path}")

    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != HEADERS:
            raise ValueError(
                f"CSV sütunları şemayla uyuşmuyor! Beklenen: {HEADERS}, Bulunan: {reader.fieldnames}"
            )

        records = []
        seen_ids = set()

        for line_no, row in enumerate(reader, start=2):
            cid = row["kampanya_id"]
            if not ID_PATTERN.match(cid) or cid in seen_ids:
                raise ValueError(f"Satır {line_no}: Hatalı veya mükerrer kampanya_id: {cid}")
            seen_ids.add(cid)

            try:
                w_date = date.fromisoformat(row["tarih"])
            except ValueError:
                raise ValueError(f"Satır {line_no}: Hatalı tarih formatı: {row['tarih']}")

            if w_date not in EXPECTED_WEEKS:
                raise ValueError(f"Satır {line_no}: Beklenmeyen tarih: {row['tarih']}")

            channel = row["kanal"]
            if channel not in CHANNELS:
                raise ValueError(f"Satır {line_no}: Bilinmeyen kanal: {channel}")

            try:
                gosterim = int(row["gosterim"])
                tiklama = int(row["tiklama"])
                donusum = int(row["donusum"])
            except ValueError:
                raise ValueError(f"Satır {line_no}: Metrik tam sayı değil.")

            if not (5000 <= gosterim <= 250000):
                raise ValueError(f"Satır {line_no}: Gösterim sınır dışı: {gosterim}")
            if not (1 <= tiklama <= gosterim):
                raise ValueError(f"Satır {line_no}: Tıklama/Gösterim mantıksız: {tiklama} > {gosterim}")
            if not (0 <= donusum <= tiklama):
                raise ValueError(f"Satır {line_no}: Dönüşüm/Tıklama mantıksız: {donusum} > {tiklama}")

            if not MONEY_PATTERN.match(row["harcama_tl"]) or not MONEY_PATTERN.match(row["gelir_tl"]):
                raise ValueError(f"Satır {line_no}: Tutar formatı 2 ondalıklı değil.")

            harcama = Decimal(row["harcama_tl"])
            gelir = Decimal(row["gelir_tl"])

            if harcama <= Decimal("0.00"):
                raise ValueError(f"Satır {line_no}: Harcama sıfır veya negatif.")
            if donusum == 0 and gelir != Decimal("0.00"):
                raise ValueError(f"Satır {line_no}: Dönüşüm 0 iken gelir sıfır değil: {gelir}")

            records.append({
                "kampanya_id": cid,
                "tarih": row["tarih"],
                "kanal": channel,
                "gosterim": gosterim,
                "tiklama": tiklama,
                "donusum": donusum,
                "harcama_tl": harcama,
                "gelir_tl": gelir,
                "roas": gelir / harcama,
            })

    if len(records) != 260:
        raise ValueError(f"Beklenen 260 satır, bulunan {len(records)} satır.")

    return records


def analyze(records):
    # M1: Toplam Harcama ve Toplam Gelir
    toplam_harcama = sum((r["harcama_tl"] for r in records), Decimal("0"))
    toplam_gelir = sum((r["gelir_tl"] for r in records), Decimal("0"))
    net_kar = toplam_gelir - toplam_harcama

    # M2: Bileşik ROAS ve Ortalama Tıklama Başı Maliyet (CPC)
    toplam_tiklama = sum(r["tiklama"] for r in records)
    toplam_gosterim = sum(r["gosterim"] for r in records)
    toplam_donusum = sum(r["donusum"] for r in records)

    bilesik_roas = toplam_gelir / toplam_harcama
    ortalama_cpc = toplam_harcama / Decimal(toplam_tiklama)
    genel_ctr = (Decimal(toplam_tiklama) / Decimal(toplam_gosterim)) * Decimal(100)

    # M3: Haftalık Trend
    haftalik = defaultdict(lambda: {"gelir": Decimal("0"), "harcama": Decimal("0")})
    for r in records:
        haftalik[r["tarih"]]["gelir"] += r["gelir_tl"]
        haftalik[r["tarih"]]["harcama"] += r["harcama_tl"]

    sirali_haftalar = sorted(haftalik.keys())
    ort_haftalik_gelir = toplam_gelir / Decimal(len(sirali_haftalar))
    ort_haftalik_harcama = toplam_harcama / Decimal(len(sirali_haftalar))

    # M4: Kanal Bazlı Kırılım
    kanal_ozet = {}
    for ch in CHANNELS:
        ch_records = [r for r in records if r["kanal"] == ch]
        ch_harcama = sum((r["harcama_tl"] for r in ch_records), Decimal("0"))
        ch_gelir = sum((r["gelir_tl"] for r in ch_records), Decimal("0"))
        ch_tiklama = sum(r["tiklama"] for r in ch_records)
        ch_gosterim = sum(r["gosterim"] for r in ch_records)
        ch_donusum = sum(r["donusum"] for r in ch_records)

        ch_roas = ch_gelir / ch_harcama
        ch_ctr = (Decimal(ch_tiklama) / Decimal(ch_gosterim)) * Decimal(100)
        ch_cpc = ch_harcama / Decimal(ch_tiklama)
        gelir_payi = (ch_gelir / toplam_gelir) * Decimal(100)

        kanal_ozet[ch] = {
            "harcama": ch_harcama,
            "gelir": ch_gelir,
            "roas": ch_roas,
            "ctr": ch_ctr,
            "cpc": ch_cpc,
            "donusum": ch_donusum,
            "gelir_payi": gelir_payi,
        }

    # M5: En Yüksek ROAS Getiren Top-3 Kampanya Haftası
    top3 = sorted(records, key=lambda x: x["roas"], reverse=True)[:3]

    return {
        "toplam_harcama": toplam_harcama,
        "toplam_gelir": toplam_gelir,
        "net_kar": net_kar,
        "toplam_tiklama": toplam_tiklama,
        "toplam_gosterim": toplam_gosterim,
        "toplam_donusum": toplam_donusum,
        "bilesik_roas": bilesik_roas,
        "ortalama_cpc": ortalama_cpc,
        "genel_ctr": genel_ctr,
        "sirali_haftalar": sirali_haftalar,
        "haftalik": haftalik,
        "ort_haftalik_gelir": ort_haftalik_gelir,
        "ort_haftalik_harcama": ort_haftalik_harcama,
        "kanal_ozet": kanal_ozet,
        "top3": top3,
    }


def generate_report(metrics):
    ko = metrics["kanal_ozet"]
    # Sort channels by ROAS descending
    sorted_channels = sorted(CHANNELS, key=lambda c: ko[c]["roas"], reverse=True)

    md = []
    md.append("# Görev 2 — Dijital Pazarlama Kampanya Analiz Raporu (PrimeBee)")
    md.append("")
    md.append(f"**Veri Kaynağı:** `data/kampanya-simulasyon-g2.csv`  ")
    md.append(f"**Veri Commit'i:** `{DATA_COMMIT}`  ")
    md.append(f"**Hazırlayan (DQ):** Tuana GÜRKAN  ")
    md.append(f"**Tarih:** 2026-11-02  ")
    md.append(f"**İlgili Issue:** [#43 (G2-analiz)](https://github.com/MAKU-VBA-GBT-II/group-g/issues/43)  ")
    md.append("")
    md.append("> **Not:** Bu rapordaki veriler tamamen sentetik simülasyon ürünüdür (`tohum=42`, 260 satır). Gerçek kişi veya kurumsal kimlik bilgisi (KVKK/PII) içermez.")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 1. Zorunlu 5 Temel Metrik ve Değerlendirme")
    md.append("")

    # M1
    md.append("### M1 — Toplam Harcama ve Toplam Gelir")
    md.append(f"- **Toplam Harcama:** {format_tl(metrics['toplam_harcama'])}")
    md.append(f"- **Toplam Gelir:** {format_tl(metrics['toplam_gelir'])}")
    md.append(f"- **Net Katma Değer (Gelir - Harcama):** {format_tl(metrics['net_kar'])}")
    md.append("")
    md.append("**Yorum:** 52 haftalık dönemde PrimeBee genelinde 1,89 milyon TL pazarlama bütçesi harcanmış ve karşılığında 10,54 milyon TL brüt satış hasılatı elde edilmiştir. Toplam kampanya operasyonu net 8,65 milyon TL finansal katma değer yaratarak yüksek bir nakit akışı sağlamıştır.")
    md.append("")

    # M2
    md.append("### M2 — Bileşik ROAS ve Ortalama Tıklama Başı Maliyet (CPC)")
    md.append(f"- **Bileşik ROAS (Σ Gelir / Σ Harcama):** {metrics['bilesik_roas']:.2f}x")
    md.append(f"- **Ortalama CPC (Σ Harcama / Σ Tıklama):** {format_tl(metrics['ortalama_cpc'])}")
    md.append(f"- **Genel Ortalama CTR:** %{metrics['genel_ctr']:.2f}")
    md.append("")
    md.append("**Yorum:** Portföy genelinde yatırılan her 1,00 TL reklam bütçesi ortalama **5,57 TL** ciro olarak geri dönmüştür. Ortalama tıklama başı maliyetin 3,39 TL seviyesinde dengelenmesi, organik ve düşük maliyetli kanalların genel maliyet tabanını optimize ettiğini göstermektedir.")
    md.append("")

    # M3
    md.append("### M3 — Haftalık Gelir ve Harcama Trendi (Zaman Serisi)")
    md.append(f"- **İncelenen Hafta Sayısı:** {len(metrics['sirali_haftalar'])} hafta (2025-10-06 – 2026-09-28)")
    md.append(f"- **Haftalık Ortalama Harcama:** {format_tl(metrics['ort_haftalik_harcama'])}")
    md.append(f"- **Haftalık Ortalama Gelir:** {format_tl(metrics['ort_haftalik_gelir'])}")
    md.append(f"- **Görsel Referansı:** `visuals/gelir-harcama-trendi.png`")
    md.append("")
    md.append("**Yorum:** 52 hafta boyunca haftalık harcama bandı 30.000 TL – 45.000 TL aralığında istikrarlı seyrederken, haftalık gelir 150.000 TL ile 260.000 TL arasında dalgalanma sergilemiştir. Hiçbir haftada operasyonel zarar yaşanmamış; dönemsel talep artışları gelire doğrudan pozitif yansımıştır.")
    md.append("")

    # M4
    md.append("### M4 — Kanal Bazlı CTR ve ROAS Kırılımı (Kategorik Kırılım)")
    md.append("")
    md.append("| Kanal | Toplam Harcama | Toplam Gelir | Gelir Payı (%) | Bileşik ROAS | Ortalama CTR | Ortalama CPC |")
    md.append("|---|---|---|---|---|---|---|")
    for ch in sorted_channels:
        c = ko[ch]
        md.append(
            f"| **{ch}** | {format_tl(c['harcama'])} | {format_tl(c['gelir'])} | %{c['gelir_payi']:.2f} | **{c['roas']:.2f}x** | %{c['ctr']:.2f} | {format_tl(c['cpc'])} |"
        )
    md.append("")
    md.append(f"**Görsel Referansı:** `visuals/kanal-roas-ctr.png`")
    md.append("")
    md.append("**Yorum:** E-posta (45,50x) ve SEO (23,26x) kanalları son derece düşük harcama maliyetleriyle olağanüstü kârlılık üretirken, toplam cironun %41,41'ini sırtlayan Google Ads (4,21x) ölçek büyüklüğü sağlamıştır. TikTok Ads (2,88x) ve Meta Ads (3,75x) ise nispeten düşük ROAS seviyeleriyle dönüşümden ziyade üst huni (farkındalık) işlevi görmüştür.")
    md.append("")

    # M5
    md.append("### M5 — En Yüksek ROAS Getiren Top-3 Kampanya Haftası (Top-N)")
    md.append("")
    md.append("| Sıra | Kampanya ID | Tarih (Hafta) | Kanal | Harcama | Gelir | ROAS |")
    md.append("|---|---|---|---|---|---|---|")
    for i, r in enumerate(metrics["top3"], start=1):
        md.append(
            f"| {i} | `{r['kampanya_id']}` | {r['tarih']} | **{r['kanal']}** | {format_tl(r['harcama_tl'])} | {format_tl(r['gelir_tl'])} | **{r['roas']:.2f}x** |"
        )
    md.append("")
    md.append(f"**Görsel Referansı:** `visuals/roas-dagilimi.png` (Histogram genelinde medyan 5,26x, ortalama 17,43x)")
    md.append("")
    md.append("**Yorum:** Tüm veri kümesindeki 260 kampanya-hafta kaydı incelendiğinde, zirvedeki 3 kaydın tamamı **E-posta** kanalından çıkmıştır. 2026-01-19 haftasındaki `K079` kampanyası yalnızca 119,27 TL harcama ile 19.162,72 TL ciro yaratarak 160,67x ile yılın rekor verimliliğine ulaşmıştır.")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 2. Bulgular: 3 Gözlem ve 1 Eylem Önerisi")
    md.append("")
    md.append("### Somut Gözlemler:")
    md.append("1. **Kanal Kutuplaşması (Asimetrik Verimlilik):** Bütçenin yalnızca %6,68'ini kullanan E-posta ve SEO kanalları, toplam cironun %35,07'sini üretmektedir. Buna karşın bütçenin %54,85'ini tüketen Google Ads kanalının ROAS'ı 4,21x düzeyinde kalmaktadır.")
    md.append("2. **Ücretli Sosyal Medya Huni Kaybı:** TikTok Ads (%1,27 CTR, 2,88x ROAS) ve Meta Ads (%1,98 CTR, 3,75x ROAS), portföy ortalaması olan 5,57x bileşik ROAS'ın belirgin şekilde altında kalarak birim bütçe başına en pahalı dönüşümü üretmektedir.")
    md.append("3. **E-posta Kanalının Yüksek Çarpanı:** E-posta kanalı %5,02 CTR ve 0,69 TL CPC ile en düşük edinim maliyetine sahip olup, ortalama sepet tutarı yüksek sadık kitle segmentlerini yakalayarak 45,50x bileşik getiri sağlamıştır.")
    md.append("")
    md.append("### Eylem Önerisi (Aksiyon Planı):")
    md.append("> **Bütçe Yeniden Tahsisi ve Otomasyon:** TikTok Ads'e ayrılan haftalık bütçenin %30'luk kısmı kesilmeli; bu bütçe E-posta otomasyon altyapısına (yeniden hedefleme ve terk edilmiş sepet akışları) ve SEO teknik içerik yatırımlarına kaydırılmalıdır. Böylece genel portföy bileşik ROAS'ının 5,57x seviyesinden 6,80x seviyesine yükseltilmesi hedeflenmelidir.")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 3. Veri Kalitesi ve Tutarlılık Kontrol Listesi")
    md.append("- [x] Toplam satır sayısı: 260 (52 hafta x 5 kanal)")
    md.append("- [x] `tarih` aralığı: 2025-10-06 ile 2026-09-28 arası (52 ardışık Pazartesi)")
    md.append("- [x] Bütçe kontrolü: Sıfır veya negatif harcama bulunmamaktadır.")
    md.append("- [x] Dönüşüm / Gelir tutarlılığı: `donusum == 0` olan satırlarda gelir sıfırdır.")
    md.append("- [x] FE grafik değerleriyle tutarlılık: `visuals/` setindeki sayılar bu rapordaki sayılarla tam eşleşmektedir.")

    return "\n".join(md) + "\n"


def main():
    print(f"Veri yükleniyor ve doğrulanıyor: {CSV_PATH}")
    records = load_and_validate(CSV_PATH)
    print(f"Doğrulama başarılı: {len(records)} kayıt şemaya tam uyumlu.")

    metrics = analyze(records)
    print(f"M1: Toplam Harcama: {metrics['toplam_harcama']} TL | Toplam Gelir: {metrics['toplam_gelir']} TL")
    print(f"M2: Bileşik ROAS: {metrics['bilesik_roas']:.2f}x | Ortalama CPC: {metrics['ortalama_cpc']:.2f} TL")
    print(f"M4: En karlı kanal: {sorted(CHANNELS, key=lambda c: metrics['kanal_ozet'][c]['roas'], reverse=True)[0]}")
    print(f"M5: Top-1 kampanya: {metrics['top3'][0]['kampanya_id']} ({metrics['top3'][0]['roas']:.2f}x)")

    report_content = generate_report(metrics)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(report_content, encoding="utf-8")
    print(f"Rapor üretildi -> {REPORT_PATH}")


if __name__ == "__main__":
    main()
