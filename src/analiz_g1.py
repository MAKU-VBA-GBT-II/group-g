"""G1 kampanya performans analizini CSV verisinden yeniden üretir.

Depo kökünden çalıştırma:
    python src/analiz_g1.py
"""

import csv
import re
from collections import Counter, defaultdict
from datetime import date, timedelta
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP, localcontext
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "data" / "kampanya-performans.csv"
REPORT_PATH = ROOT / "docs" / "analiz-g1.md"
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
    FIRST_WEEK + timedelta(weeks=index) for index in range(WEEK_COUNT)
)
CENT = Decimal("0.01")
MONEY_PATTERN = re.compile(r"\d+\.\d{2}\Z")
ID_PATTERN = re.compile(r"K\d{3}\Z")


def parse_integer(value, field, line_number):
    try:
        if not re.fullmatch(r"\d+", value):
            raise ValueError
        return int(value)
    except ValueError as error:
        raise ValueError(
            f"CSV satır {line_number}: {field} tam sayı değil: {value!r}"
        ) from error


def parse_money(value, field, line_number):
    if not MONEY_PATTERN.fullmatch(value):
        raise ValueError(
            f"CSV satır {line_number}: {field} tam iki ondalık basamaklı değil: "
            f"{value!r}"
        )
    try:
        return Decimal(value)
    except InvalidOperation as error:
        raise ValueError(
            f"CSV satır {line_number}: {field} sayısal değil: {value!r}"
        ) from error


def load_and_validate(path):
    with path.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames != HEADERS:
            raise ValueError(
                "CSV sütunları veri sözlüğüyle uyuşmuyor. "
                f"Beklenen: {HEADERS}; bulunan: {reader.fieldnames}"
            )

        records = []
        seen_ids = set()
        channel_counts = Counter()
        week_channel_counts = Counter()

        for line_number, row in enumerate(reader, start=2):
            if None in row or any(row.get(field) is None for field in HEADERS):
                raise ValueError(f"CSV satır {line_number}: sütun sayısı hatalı")

            campaign_id = row["kampanya_id"]
            if not ID_PATTERN.fullmatch(campaign_id) or campaign_id in seen_ids:
                raise ValueError(
                    f"CSV satır {line_number}: kampanya_id biçimi hatalı "
                    f"veya yinelenmiş: {campaign_id!r}"
                )
            seen_ids.add(campaign_id)

            try:
                week = date.fromisoformat(row["tarih"])
            except ValueError as error:
                raise ValueError(
                    f"CSV satır {line_number}: tarih yyyy-aa-gg biçiminde değil"
                ) from error
            if week.isoformat() != row["tarih"] or week not in EXPECTED_WEEKS:
                raise ValueError(
                    f"CSV satır {line_number}: tarih beklenen 52 haftalık "
                    f"dönemde değil: {row['tarih']!r}"
                )

            channel = row["kanal"]
            if channel not in CHANNELS:
                raise ValueError(
                    f"CSV satır {line_number}: bilinmeyen kanal: {channel!r}"
                )

            impressions = parse_integer(row["gosterim"], "gosterim", line_number)
            clicks = parse_integer(row["tiklama"], "tiklama", line_number)
            conversions = parse_integer(row["donusum"], "donusum", line_number)
            spend = parse_money(row["harcama_tl"], "harcama_tl", line_number)
            revenue = parse_money(row["gelir_tl"], "gelir_tl", line_number)

            if not 5000 <= impressions <= 250000:
                raise ValueError(
                    f"CSV satır {line_number}: gosterim aralık dışında"
                )
            if not 1 <= clicks <= impressions:
                raise ValueError(
                    f"CSV satır {line_number}: tiklama aralık dışında"
                )
            if not 0 <= conversions <= clicks:
                raise ValueError(
                    f"CSV satır {line_number}: donusum aralık dışında"
                )
            if spend <= 0 or revenue < 0:
                raise ValueError(
                    f"CSV satır {line_number}: harcama/gelir alt sınırı ihlali"
                )
            if conversions == 0 and revenue != 0:
                raise ValueError(
                    f"CSV satır {line_number}: sıfır dönüşümde gelir sıfır olmalı"
                )

            channel_counts[channel] += 1
            week_channel_counts[(week, channel)] += 1
            records.append(
                {
                    "week": week,
                    "channel": channel,
                    "spend": spend,
                    "revenue": revenue,
                }
            )

    expected_ids = {f"K{index:03d}" for index in range(1, 261)}
    if len(records) != 260 or seen_ids != expected_ids:
        raise ValueError(
            "Veri sözlüğüne göre 260 kayıt ve K001–K260 kimlikleri bekleniyor; "
            f"bulunan kayıt sayısı: {len(records)}"
        )
    if any(channel_counts[channel] != WEEK_COUNT for channel in CHANNELS):
        raise ValueError(
            f"Her kanalda 52 kayıt olmalı; bulunan dağılım: {dict(channel_counts)}"
        )
    if any(
        week_channel_counts[(week, channel)] != 1
        for week in EXPECTED_WEEKS
        for channel in CHANNELS
    ):
        raise ValueError("Her hafta için her kanalda tam bir kayıt olmalı")

    return records


def money(value):
    formatted = f"{value.quantize(CENT, rounding=ROUND_HALF_UP):,.2f}"
    return formatted.replace(",", "_").replace(".", ",").replace("_", ".")


def decimal_value(value, places=2):
    return f"{value.quantize(CENT, rounding=ROUND_HALF_UP):.{places}f}".replace(
        ".", ","
    )


def build_report(records):
    with localcontext() as context:
        context.prec = 40
        total_revenue = sum(
            (record["revenue"] for record in records), Decimal("0")
        )
        total_spend = sum((record["spend"] for record in records), Decimal("0"))
        mean_campaign_roas = sum(
            (record["revenue"] / record["spend"] for record in records),
            Decimal("0"),
        ) / Decimal(len(records))
        combined_roas = total_revenue / total_spend

        revenue_by_channel = defaultdict(Decimal)
        spend_by_channel = defaultdict(Decimal)
        revenue_by_week = defaultdict(Decimal)
        for record in records:
            revenue_by_channel[record["channel"]] += record["revenue"]
            spend_by_channel[record["channel"]] += record["spend"]
            revenue_by_week[record["week"]] += record["revenue"]

        channel_stats = {
            channel: {
                "revenue": revenue_by_channel[channel],
                "spend": spend_by_channel[channel],
                "share": revenue_by_channel[channel] / total_revenue * 100,
                "roas": revenue_by_channel[channel] / spend_by_channel[channel],
            }
            for channel in CHANNELS
        }
        revenue_ranking = sorted(
            CHANNELS, key=lambda channel: channel_stats[channel]["revenue"], reverse=True
        )
        roas_ranking = sorted(
            CHANNELS, key=lambda channel: channel_stats[channel]["roas"], reverse=True
        )
        highest_revenue = revenue_ranking[0]
        highest_roas = roas_ranking[0]
        lowest_revenue = revenue_ranking[-1]
        lowest_roas = roas_ranking[-1]

        lines = [
            "# G1 — Kampanya Performans Analizi",
            "",
            "**Veri:** `data/kampanya-performans.csv` · "
            "**Şema:** [`veri-sozlugu-g1.md`](veri-sozlugu-g1.md) v3",
            f"**Kapsam:** 5 kanal × 52 hafta = {len(records)} kampanya-hafta kaydı, "
            f"{EXPECTED_WEEKS[0].isoformat()}–{EXPECTED_WEEKS[-1].isoformat()}",
            "**Yöntem:** Para toplamları `Decimal` ile hesaplanmıştır. "
            "Ortalama kampanya ROAS'ı, satır bazındaki gelir/harcama oranlarının "
            "aritmetik ortalamasıdır. Kanal ROAS'ı kanal toplam geliri / kanal "
            "toplam harcamasıdır. Veriler sentetiktir; gözlemler nedensellik kanıtlamaz.",
            "",
            "## Metrikler",
            "",
            "### 1. Toplam gelir",
            "",
            f"Toplam gelir **{money(total_revenue)} TL**'dir. "
            f"52 haftalık dönem için haftalık ortalama toplam gelir "
            f"**{money(total_revenue / Decimal(WEEK_COUNT))} TL**; toplam harcama "
            f"**{money(total_spend)} TL** ve birleşik ROAS "
            f"(toplam gelir / toplam harcama) **"
            f"{decimal_value(combined_roas)}x** olarak hesaplanmıştır.",
            "",
            "### 2. Ortalama kampanya-hafta ROAS",
            "",
            f"{len(records)} kampanya-hafta kaydındaki ROAS değerlerinin eşit "
            f"ağırlıklı aritmetik ortalaması **"
            f"{decimal_value(mean_campaign_roas)}x**'tir. Bu ölçü, her kayda eşit "
            "ağırlık verir; toplam gelir/toplam harcama ile bulunan birleşik "
            f"ROAS'tan (**{decimal_value(combined_roas)}x**) farklı olması bu nedenle "
            "beklenebilir.",
            "",
            "### 3. Kanala göre gelir",
            "",
            "| Kanal | Toplam gelir (TL) | Toplam gelir payı |",
            "|---|---:|---:|",
        ]

        for channel in revenue_ranking:
            stats = channel_stats[channel]
            lines.append(
                f"| {channel} | {money(stats['revenue'])} | "
                f"%{decimal_value(stats['share'])} |"
            )
        lines.extend(
            [
                f"| **Toplam** | **{money(total_revenue)}** | **%100,00** |",
                "",
                f"{highest_revenue}, **{money(channel_stats[highest_revenue]['revenue'])} TL** "
                f"ile en yüksek toplam geliri üretmiştir; "
                f"{lowest_revenue} kanalının geliri en düşüktür. Gelir sıralaması "
                "tek başına verimliliği göstermez; ROAS ile birlikte değerlendirilmelidir.",
                "",
                "### 4. Kanala göre birleşik ROAS",
                "",
                "| Kanal | Toplam harcama (TL) | Toplam gelir (TL) | Birleşik ROAS |",
                "|---|---:|---:|---:|",
            ]
        )
        for channel in roas_ranking:
            stats = channel_stats[channel]
            lines.append(
                f"| {channel} | {money(stats['spend'])} | "
                f"{money(stats['revenue'])} | {decimal_value(stats['roas'])}x |"
            )
        lines.extend(
            [
                "",
                "ROAS gelir ve harcamaya dayanır; kâr marjını veya diğer ek "
                "maliyetleri içermez.",
                "",
                "### 5. ROAS'a göre ilk üç kanal",
                "",
                "| Sıra | Kanal | Birleşik ROAS |",
                "|---:|---|---:|",
            ]
        )
        for rank, channel in enumerate(roas_ranking[:3], start=1):
            lines.append(
                f"| {rank} | {channel} | "
                f"{decimal_value(channel_stats[channel]['roas'])}x |"
            )

        lines.extend(
            [
                "",
                "### 6. Haftalık toplam gelir",
                "",
                "Aşağıdaki tabloda her hafta için beş kanalın gelirleri toplanmıştır.",
                "",
                "| Hafta başlangıcı | Toplam gelir (TL) |",
                "|---|---:|",
            ]
        )
        for week in EXPECTED_WEEKS:
            lines.append(f"| {week.isoformat()} | {money(revenue_by_week[week])} |")

        lines.extend(
            [
                "",
                "## Somut gözlemler",
                "",
                f"1. {highest_revenue}, **{money(channel_stats[highest_revenue]['revenue'])} TL** "
                f"ile toplam gelirin **%{decimal_value(channel_stats[highest_revenue]['share'])}**'sini "
                "üretmiştir.",
                f"2. {highest_roas}, **{money(channel_stats[highest_roas]['spend'])} TL** "
                f"harcamaya karşılık **{money(channel_stats[highest_roas]['revenue'])} TL** "
                f"gelir ve en yüksek kanal birleşik ROAS'ı olan "
                f"**{decimal_value(channel_stats[highest_roas]['roas'])}x** değerini "
                "üretmiştir.",
                f"3. {lowest_revenue}, **"
                f"{money(channel_stats[lowest_revenue]['revenue'])} TL** ile en düşük "
                f"toplam gelire; {lowest_roas} ise **"
                f"{decimal_value(channel_stats[lowest_roas]['roas'])}x** ile en düşük "
                "kanal birleşik ROAS'ına sahiptir. Bu sentetik dönem tek başına bir "
                "kanalı durdurma gerekçesi değildir.",
                "",
                "## Eylem önerisi",
                "",
                f"{highest_roas} ve {roas_ranking[1]} için küçük ve süreli bir bütçe "
                "artışını kontrollü pilot olarak değerlendirin. Pilot boyunca haftalık "
                "harcama, gelir, ROAS ve dönüşümü izleyin; kâr marjı ve kapasiteyi de "
                "hesaba katmadan bütçeyi genişletmeyin.",
                "",
            ]
        )
        return "\n".join(lines)


def main():
    records = load_and_validate(CSV_PATH)
    report = build_report(records)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(report, encoding="utf-8", newline="\n")
    print(f"Analiz {len(records)} kayıt üzerinden yazıldı: {REPORT_PATH}")


if __name__ == "__main__":
    main()
