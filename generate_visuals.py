import os
import matplotlib.pyplot as plt
import pandas as pd

# visuals klasörünü oluştur
os.makedirs("visuals", exist_ok=True)

# 260 satırlık asıl veriyi oku
df = pd.read_csv("data/kampanya-performans.csv")

# Sütun isimlerini küçük harfe çevirip temizle
df.columns = df.columns.str.strip().str.lower()

# Sütun tespiti veya ROAS hesabı
# Eğer roas sütunu yoksa gelir / harcama ile hesapla
if "roas" in df.columns:
    df["roas_val"] = df["roas"]
elif "harcama_tl" in df.columns and "gelir_tl" in df.columns:
    df["roas_val"] = df["gelir_tl"] / df["harcama_tl"]
elif "harcama" in df.columns and "gelir" in df.columns:
    df["roas_val"] = df["gelir"] / df["harcama"]
else:
    # Son sütun hariç roas içeren veya sayısal sütun bul
    roas_cols = [c for c in df.columns if "roas" in c]
    if roas_cols:
        df["roas_val"] = df[roas_cols[0]]
    else:
        df["roas_val"] = df.iloc[:, -2]

# Hafta ve Gelir Sütunları
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
plt.figure(figsize=(11, 5))
df_weekly = df.groupby(week_col, as_index=False)[revenue_col].sum()

plt.plot(
    range(len(df_weekly)),
    df_weekly[revenue_col],
    marker="o",
    markersize=4,
    linewidth=2,
    color="#1f77b4",
)

plt.title("Haftalık Toplam Gelir Trendi", fontsize=14, fontweight="bold", pad=15)
plt.suptitle(
    "5 kanal · 52 hafta · 6 Ekim 2025 – 28 Eylül 2026",
    fontsize=10,
    color="gray",
    y=0.92,
)

# Etiketleri her 4 haftada bir (ayda bir) göstererek temizle
weeks = df_weekly[week_col].astype(str).tolist()
step = max(1, len(weeks) // 13)  # Yaklaşık ayda bir etiket
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
plt.figure(figsize=(10, 5))
df_channel = df.groupby(channel_col, as_index=False)["roas_val"].mean()

bars = plt.bar(
    df_channel[channel_col],
    df_channel["roas_val"],
    color="#2ca02c",
    width=0.55,
)

plt.title(
    "Pazarlama Kanalına Göre Ortalama ROAS", fontsize=14, fontweight="bold", pad=15
)
plt.suptitle(
    "5 kanal · 52 hafta · 6 Ekim 2025 – 28 Eylül 2026",
    fontsize=10,
    color="gray",
    y=0.92,
)

plt.xlabel("Kanal", fontsize=11, labelpad=10)
plt.ylabel("Ortalama ROAS (x)", fontsize=11)

# Çubukların üzerine ROAS değerlerini yaz (ör. 12.45x)
max_y = df_channel["roas_val"].max()
for bar in bars:
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        yval + (max_y * 0.02),
        f"{yval:.2f}x",
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight="bold",
    )

plt.ylim(0, max_y * 1.15)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("visuals/kanal-kirilim.png", dpi=300)
plt.close()

print(
    "Düzeltilmiş grafikler 'visuals/' klasörüne başarıyla kaydedildi!"
)