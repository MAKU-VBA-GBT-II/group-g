import os
import matplotlib.pyplot as plt
import pandas as pd

# visuals klasörünü oluştur
os.makedirs("visuals", exist_ok=True)

# 260 satırlık veriyi oku
df = pd.read_csv("data/kampanya-performans.csv")
df.columns = df.columns.str.strip().str.lower()

# ROAS Sütun Hesabı
if "harcama_tl" in df.columns and "gelir_tl" in df.columns:
    df["roas_val"] = df["gelir_tl"] / df["harcama_tl"]
elif "roas" in df.columns:
    df["roas_val"] = df["roas"]
else:
    df["roas_val"] = df.iloc[:, -2]

week_col = next(
    (
        c
        for c in df.columns
        if any(k in c for k in ["hafta", "tarih", "date", "week"])
    ),
    df.columns[0],
)
revenue_col = next(
    (
        c
        for c in df.columns
        if any(k in c for k in ["gelir", "revenue", "ciro"])
    ),
    "gelir_tl",
)
channel_col = next(
    (
        c
        for c in df.columns
        if any(k in c for k in ["kanal", "channel", "medium"])
    ),
    "kanal",
)

# ---------------------------------------------------------
# 1. GRAFİK: Zaman Serisi (Haftalık Toplam Gelir)
# ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(11, 5.5))
df_weekly = df.groupby(week_col, as_index=False)[revenue_col].sum()

ax.plot(
    range(len(df_weekly)),
    df_weekly[revenue_col],
    marker="o",
    markersize=4,
    linewidth=2,
    color="#1f77b4",
)

# Başlık ve Alt Başlığı Birbirinden Ayırıyoruz
plt.title(
    "Haftalık Toplam Gelir Trendi", fontsize=14, fontweight="bold", pad=25
)
plt.text(
    0.5,
    1.02,
    "5 kanal · 52 hafta · 6 Ekim 2025 – 28 Eylül 2026",
    transform=ax.transAxes,
    ha="center",
    fontsize=9.5,
    color="gray",
)

weeks = df_weekly[week_col].astype(str).tolist()
step = max(1, len(weeks) // 12)
plt.xticks(
    range(0, len(weeks), step), weeks[::step], rotation=45, ha="right", fontsize=9
)

plt.xlabel("Hafta / Dönem", fontsize=11, labelpad=10)
plt.ylabel("Toplam Gelir (TL)", fontsize=11)
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("visuals/gelir-zaman-serisi.png", dpi=300)
plt.close()

# ---------------------------------------------------------
# 2. GRAFİK: Kırılım (Kanala Göre Ortalama ROAS)
# ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.5))
df_channel = df.groupby(channel_col, as_index=False)["roas_val"].mean()

bars = ax.bar(
    df_channel[channel_col],
    df_channel["roas_val"],
    color="#2ca02c",
    width=0.5,
)

# Başlık Düzeltmesi
plt.title(
    "Pazarlama Kanalına Göre Ortalama ROAS",
    fontsize=14,
    fontweight="bold",
    pad=25,
)
plt.text(
    0.5,
    1.02,
    "5 kanal · 52 hafta · 6 Ekim 2025 – 28 Eylül 2026",
    transform=ax.transAxes,
    ha="center",
    fontsize=9.5,
    color="gray",
)

plt.xlabel("Kanal", fontsize=11, labelpad=10)
plt.ylabel("Ortalama ROAS (x)", fontsize=11)

max_y = df_channel["roas_val"].max()
for bar in bars:
    yval = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        yval + (max_y * 0.02),
        f"{yval:.2f}x",
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight="bold",
    )

ax.set_ylim(0, max_y * 1.18)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("visuals/kanal-kirilim.png", dpi=300)
plt.close()

print("Grafikler başlıklar düzeltilerek yeniden üretildi!")