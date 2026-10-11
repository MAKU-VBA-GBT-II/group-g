import csv
import random
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
HEDEF = KOK / "data" / "prova-ozge.csv"

random.seed(42)
sayilar = [random.randint(1, 100) for _ in range(10)]

HEDEF.parent.mkdir(exist_ok=True)
with open(HEDEF, "w", newline="", encoding="utf-8") as f:
    yazici = csv.writer(f)
    yazici.writerow(["deger"])
    for s in sayilar:
        yazici.writerow([s])

print("Bitti!")