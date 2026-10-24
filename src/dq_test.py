"""Run the G1 campaign CSV checks defined by the current schema."""

import argparse
import csv
import io
import re
import sys
from collections import Counter
from datetime import date, timedelta
from decimal import Decimal, InvalidOperation
from pathlib import Path

import kampanya_simulasyon as schema


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CSV = ROOT / "data" / "kampanya-performans.csv"
EXPECTED_ROWS = schema.HAFTA_SAYISI * len(schema.KANALLAR)
EXPECTED_DATES = {
    (schema.BASLANGIC + timedelta(weeks=week)).isoformat()
    for week in range(schema.HAFTA_SAYISI)
}


def fail_if(condition, message):
    return message if condition else None


def has_expected_columns(rows):
    return bool(rows) and rows[0] == schema.BASLIK


def data_rows(rows):
    return rows[1:] if rows else []


def serialize_generated_rows(rows):
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(schema.BASLIK)
    writer.writerows(rows)
    return output.getvalue().encode("utf-8")


def check_campaign_ids(rows):
    ids = [row[0] for row in data_rows(rows) if len(row) == len(schema.BASLIK)]
    expected = [f"K{number:03d}" for number in range(1, EXPECTED_ROWS + 1)]
    return fail_if(ids != expected, "Kimlikler K001'den başlayıp sıralı ve benzersiz olmalı.")


def check_dates(rows):
    values = [row[1] for row in data_rows(rows) if len(row) == len(schema.BASLIK)]
    invalid = []
    for line_number, value in enumerate(values, start=2):
        try:
            parsed = date.fromisoformat(value)
        except ValueError:
            invalid.append(f"satır {line_number}: geçersiz ISO tarih")
            continue
        if parsed.isoformat() != value or parsed.weekday() != 0 or value not in EXPECTED_DATES:
            invalid.append(f"satır {line_number}: tarih biçimi, günü veya aralığı uygun değil")
    return fail_if(bool(invalid), "; ".join(invalid[:3]))


def check_numeric_values(rows):
    issues = []
    for line_number, row in enumerate(data_rows(rows), start=2):
        if len(row) != len(schema.BASLIK):
            issues.append(f"satır {line_number}: sütun sayısı hatalı")
            continue
        impressions, clicks, conversions = row[3:6]
        if not all(re.fullmatch(r"\d+", value) for value in (impressions, clicks, conversions)):
            issues.append(f"satır {line_number}: gösterim/tıklama/dönüşüm tam sayı değil")
            continue
        impressions, clicks, conversions = map(int, (impressions, clicks, conversions))
        if not schema.GOSTERIM_MIN <= impressions <= schema.GOSTERIM_MAX:
            issues.append(f"satır {line_number}: gösterim aralık dışında")
        elif not 1 <= clicks <= impressions:
            issues.append(f"satır {line_number}: tıklama 1 ile gösterim arasında değil")
        elif not 0 <= conversions <= clicks:
            issues.append(f"satır {line_number}: dönüşüm 0 ile tıklama arasında değil")
    return fail_if(bool(issues), "; ".join(issues[:3]))


def check_amounts(rows):
    issues = []
    for line_number, row in enumerate(data_rows(rows), start=2):
        if len(row) != len(schema.BASLIK):
            issues.append(f"satır {line_number}: sütun sayısı hatalı")
            continue
        spend, revenue = row[6:8]
        if not re.fullmatch(r"\d+\.\d{2}", spend) or not re.fullmatch(r"\d+\.\d{2}", revenue):
            issues.append(f"satır {line_number}: tutarlar tam iki ondalık basamaklı değil")
            continue
        try:
            spend_value, revenue_value = Decimal(spend), Decimal(revenue)
        except InvalidOperation:
            issues.append(f"satır {line_number}: tutarlar sayısal değil")
            continue
        if spend_value <= 0 or revenue_value < 0:
            issues.append(f"satır {line_number}: tutar alt sınırı ihlal edildi")
        elif row[5] == "0" and revenue_value != Decimal("0.00"):
            issues.append(f"satır {line_number}: dönüşüm sıfırken gelir 0.00 değil")
    return fail_if(bool(issues), "; ".join(issues[:3]))


def check_channels(rows):
    values = [row[2] for row in data_rows(rows) if len(row) == len(schema.BASLIK)]
    counts = Counter(values)
    expected = {channel: schema.HAFTA_SAYISI for channel in schema.KANALLAR}
    return fail_if(
        counts != expected,
        f"Kanal dağılımı beklenenden farklı: {dict(counts)}",
    )


def check_week_channel_pairs(rows):
    pairs = [
        (row[1], row[2])
        for row in data_rows(rows)
        if len(row) == len(schema.BASLIK)
    ]
    expected = {
        (week, channel)
        for week in EXPECTED_DATES
        for channel in schema.KANALLAR
    }
    duplicates = len(pairs) != len(set(pairs))
    return fail_if(
        duplicates or set(pairs) != expected,
        "Hafta-kanal çiftleri benzersiz olmalı ve beklenen 260 kombinasyonun tamamını içermeli.",
    )


def check_empty_cells(rows):
    empty = [
        f"satır {line_number}, sütun {column_number}"
        for line_number, row in enumerate(data_rows(rows), start=2)
        for column_number, value in enumerate(row, start=1)
        if not value.strip()
    ]
    return fail_if(bool(empty), "Boş hücre bulundu: " + ", ".join(empty[:3]))


def check_reproducibility(raw):
    first = serialize_generated_rows(schema.satirlari_uret())
    second = serialize_generated_rows(schema.satirlari_uret())
    if first != second:
        return "Üretici betiği iki çalıştırmada aynı baytları üretmedi."
    return fail_if(raw != first, "CSV, sabit tohumla üretilen beklenen baytlarla aynı değil.")


def check_file_format(raw, text):
    issues = []
    if text is None:
        issues.append("Dosya UTF-8 olarak çözümlenemedi.")
    elif not text.splitlines() or "," not in text.splitlines()[0]:
        issues.append("CSV başlığı virgülle ayrılmış olmalı.")
    if raw.startswith(b"\xef\xbb\xbf"):
        issues.append("UTF-8 BOM bulunmamalı.")
    if b"\r" in raw:
        issues.append("Satır sonları LF (\\n) olmalı; CR karakteri bulundu.")
    if raw and not raw.endswith(b"\n"):
        issues.append("Dosya sonu LF satır sonuyla bitmeli.")
    return "; ".join(issues) if issues else None


def run_checks(path):
    if not path.is_file():
        raise FileNotFoundError(f"CSV dosyası bulunamadı: {path}")

    raw = path.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        text = None

    rows = []
    if text is not None:
        try:
            rows = list(csv.reader(io.StringIO(text, newline=""), strict=True))
        except csv.Error:
            rows = []

    checks = [
        ("TC-01", "Dosya var ve okunabilir", None),
        ("TC-02", "Tam veri satırı sayısı", fail_if(len(data_rows(rows)) != EXPECTED_ROWS, f"{len(data_rows(rows))} satır bulundu; {EXPECTED_ROWS} bekleniyordu.")),
        ("TC-03", "Sütun adları ve sırası", fail_if(not has_expected_columns(rows), f"Beklenen başlık: {schema.BASLIK}")),
        ("TC-04", "Kampanya kimlikleri", check_campaign_ids(rows)),
        ("TC-05", "Tarih biçimi, günü ve aralığı", check_dates(rows)),
        ("TC-06", "Sayısal türler, aralıklar ve ilişkiler", check_numeric_values(rows)),
        ("TC-07", "Tutar biçimi ve tutarlılığı", check_amounts(rows)),
        ("TC-08", "Kanal değerleri ve kanal başına kayıt sayısı", check_channels(rows)),
        ("TC-09", "Hafta-kanal çiftlerinin benzersizliği", check_week_channel_pairs(rows)),
        ("TC-10", "Boş hücre kontrolü", check_empty_cells(rows)),
        ("TC-11", "Üretim tekrarlanabilirliği", check_reproducibility(raw)),
        ("TC-12", "UTF-8, BOM ve satır sonu biçimi", check_file_format(raw, text)),
    ]

    print(f"Test dosyası: {path}")
    print(f"Beklenen veri satırı: {EXPECTED_ROWS}; bulunan: {len(data_rows(rows))}")
    for test_id, title, error in checks:
        status = "KALDI" if error else "GEÇTİ"
        detail = error or "Beklenen koşul doğrulandı."
        print(f"{test_id} | {status} | {title} | {detail}")

    failures = sum(error is not None for _, _, error in checks)
    print(f"Özet: {len(checks) - failures}/{len(checks)} geçti; {failures} kaldı.")
    return 1 if failures else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--csv",
        type=Path,
        default=DEFAULT_CSV,
        help="Kontrol edilecek CSV yolu (varsayılan: data/kampanya-performans.csv)",
    )
    args = parser.parse_args()
    return run_checks(args.csv)


if __name__ == "__main__":
    sys.exit(main())
