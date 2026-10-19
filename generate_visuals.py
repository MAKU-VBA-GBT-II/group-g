import os
import matplotlib.pyplot as plt
import pandas as pd

# visuals klasörünü oluştur
os.makedirs("visuals", exist_ok=True)

# 260 satırlık asıl veriyi oku
df = pd.read_csv("data/kampanya-performans.csv")

# Sütun isimlerini küçük harfe çevirip düzenle
df.columns = df.columns.str.strip().str.lower()

# Hafta veya Tarih sütununu bul
week_col = next(
    (
        c
        for c in df.columns
        if any(k in c for k in ["hafta", "date", "tarih", "week"])
    ),
    df.columns[0],
)
revenue_col = next(
    (
        c
        for c in df.columns
        if any(k in c for k in ["gelir", "revenue", "harcama", "ciro"])
    ),
    df.columns[1],
)
channel_col = next(
    (
        c
        for c in df.columns
        if any(k in c for k in ["kanal", "channel", "medium"])
    ),
    df.columns[2],
)
roas_col = next(
    (c for c in df.columns if "roas" in c),
    df.columns[-1] if len(df.columns) > 3 else df.columns[1],
)

# 1. Grafik: Zaman Serisi (Toplam Gelir)
plt.figure(figsize=(10, 5))
df_weekly = df.groupby(week_col)[revenue_col].sum().reset_index()

plt.plot(
    df_weekly[week_col].astype(str),
    df_weekly[revenue_col],
    marker="o",
    linewidth=2,
    color="#1f77b4",
)
plt.title("Haftalık Toplam Gelir Trendi", fontsize=14, fontweight="bold")
plt.xlabel("Hafta / Tarih", fontsize=12)
plt.ylabel("Toplam Gelir (TL)", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("visuals/gelir-zaman-serisi.png", dpi=300)
plt.close()

# 2. Grafik: Kırılım (Kanala Göre ROAS)
plt.figure(figsize=(10, 5))
df_channel = df.groupby(channel_col)[roas_col].mean().reset_index()

bars = plt.bar(df_channel[channel_col], df_channel[roas_col], color="#2ca02c")
plt.title("Pazarlama Kanalına Göre Ortalama ROAS", fontsize=14, fontweight="bold")
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

print("Grafikler 260 satırlık asıl veriden başarıyla üretildi!")