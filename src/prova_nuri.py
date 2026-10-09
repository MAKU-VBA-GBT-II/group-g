import csv
import random
from pathlib import Path


def main():
    data_dir = Path(__file__).resolve().parents[1] / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    file_path = data_dir / "prova-nuri.csv"
    numbers = [random.randint(1, 100) for _ in range(10)]

    with file_path.open(mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["deger"])
        writer.writerows([[number] for number in numbers])


if __name__ == "__main__":
    main()
