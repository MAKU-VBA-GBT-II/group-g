import os
import random

# data klasörünü yoksa otomatik oluşturur
os.makedirs("data", exist_ok=True)

# 1 ile 100 arasında 10 rastgele sayı üretir
sayilar = [random.randint(1, 100) for _ in range(10)]

# data/prova-tuana.csv dosyasına yazar
with open("data/prova-tuana.csv", "w", encoding="utf-8") as f:
    f.write("deger\n")  # Başlık satırı
    for sayi in sayilar:
        f.write(f"{sayi}\n")

print("Dosya başarıyla oluşturuldu!")