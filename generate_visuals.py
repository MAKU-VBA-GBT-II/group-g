import os
import matplotlib.pyplot as plt
import pandas as pd

# visuals klasörünü oluştur
os.makedirs("visuals", exist_ok=True)

# Veriyi oku
df = pd.read_csv("data/kampanya-performans.csv")

# 1. Grafik: Zaman Serisi (Haftalık Toplam Gelir)
plt.figure(figsize=(10, 5))
df_weekly = df.groupby("hafta")["gelir"].sum().reset_index()

plt.plot(
    df_weekly["hafta"],
    df_weekly["gelir"],
    marker="o",
    linewidth=2,
    color="#1f77b4",
)
plt.title("Haftalık Toplam Gelir Trendi", fontsize=14, fontweight="bold")
plt.xlabel("Hafta", fontsize=12)
plt.ylabel("Gelir (TL)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("visuals/gelir-zaman-serisi.png", dpi=300)
plt.close()

# 2. Grafik: Kırılım (Kanala Göre ROAS)
plt.figure(figsize=(10, 5))
df_channel = df.groupby("kanal")["roas"].mean().reset_index()

bars = plt.bar(df_channel["kanal"], df_channel["roas"], color="#2ca02c")
plt.title("Pazarlama Kanalına Göre ROAS", fontsize=14, fontweight="bold")
plt.xlabel("Kanal", fontsize=12)
plt.ylabel("ROAS (x)", fontsize=12)

for bar in bars:
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        yval + 0.05,
        f"{yval:.2f}x",
        ha="center",
        va="bottom",
        fontsize=10,
    )

plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("visuals/kanal-kirilim.png", dpi=300)
plt.close()

print("Grafikler visuals/ klasörüne kaydedildi!")