import csv
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from src.simulasyon import KANALLAR, secili_kanallari_belirle


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "src" / "simulasyon.py"


class KanalSecimiTestleri(unittest.TestCase):
    def test_cli_belirli_kanallari_secer(self):
        with tempfile.TemporaryDirectory() as gecici_dizin:
            cikti = Path(gecici_dizin) / "kanallar.csv"
            subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--hafta_sayisi",
                    "2",
                    "--kanallar",
                    "E-posta",
                    "SEO",
                    "--cikti",
                    str(cikti),
                ],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            )

            with cikti.open(encoding="utf-8", newline="") as dosya:
                satirlar = list(csv.DictReader(dosya))

        self.assertEqual(len(satirlar), 4)
        self.assertEqual(
            [satir["kanal"] for satir in satirlar],
            ["E-posta", "SEO", "E-posta", "SEO"],
        )

    def test_cli_kanal_adediyle_secili_kanallar_eslesir(self):
        with tempfile.TemporaryDirectory() as gecici_dizin:
            cikti = Path(gecici_dizin) / "kanallar.csv"
            subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--hafta_sayisi",
                    "2",
                    "--kampanya_sayisi",
                    "2",
                    "--kanallar",
                    "E-posta",
                    "SEO",
                    "--cikti",
                    str(cikti),
                ],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            )

            with cikti.open(encoding="utf-8", newline="") as dosya:
                satirlar = list(csv.DictReader(dosya))

        self.assertEqual(len(satirlar), 4)
        self.assertEqual(
            [satir["kanal"] for satir in satirlar],
            ["E-posta", "SEO", "E-posta", "SEO"],
        )

    def test_eski_kampanya_sayisi_kullanimi_korunur(self):
        kanallar = secili_kanallari_belirle(2, None)
        self.assertEqual([ad for ad, _ in kanallar], list(KANALLAR)[:2])

    def test_kanal_adedi_kanal_listesinden_turetilir(self):
        kanallar = secili_kanallari_belirle(None, ["E-posta", "SEO"])
        self.assertEqual([ad for ad, _ in kanallar], ["E-posta", "SEO"])

    def test_uyusmayan_adet_reddedilir(self):
        with self.assertRaisesRegex(ValueError, "eşleşmelidir"):
            secili_kanallari_belirle(1, ["E-posta", "SEO"])

    def test_bilinmeyen_kanal_reddedilir(self):
        with self.assertRaisesRegex(ValueError, "geçersiz kanal"):
            secili_kanallari_belirle(None, ["Bilinmeyen"])

    def test_yinelenen_kanal_reddedilir(self):
        with self.assertRaisesRegex(ValueError, "yinelenen"):
            secili_kanallari_belirle(None, ["SEO", "SEO"])


if __name__ == "__main__":
    unittest.main()
