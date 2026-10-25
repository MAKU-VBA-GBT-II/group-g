from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

# Proje kök dizini ve yol tanımları
ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "kampanya-performans.csv"
VISUALS_DIR = ROOT / "visuals"
VISUALS_DIR.mkdir(parents=True, exist_ok=True)

# Veri setini oku (sütun adları veri sözlüğünden: tarih, kanal, harcama_tl, gelir_tl)
df = pd.read_csv(DATA_PATH)

# Sütun adları doğrudan — veri sözlüğüne göre sabit
week_col = "tarih"
revenue_col = "gelir_tl"
spend_col = "harcama_tl"
channel_col = "kanal"

# Alt başlık için dinamik hesapla
n_kanal = df[channel_col].nunique()
n_hafta = df[week_col].nunique()
tarih_baslangic = pd.to_datetime(df[week_col]).min().strftime("%d %B %Y").lstrip("0")
tarih_bitis = pd.to_datetime(df[week_col]).max().strftime("%d %B %Y").lstrip("0")
alt_baslik = f"{n_kanal} kanal · {n_hafta} hafta · {tarih_baslangic} – {tarih_bitis}"

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

# Haftalık ortalama çizgisi (analiz §4 referansı için)
haftalik_ort = df_weekly[revenue_col].mean()
ax.axhline(haftalik_ort, color="orange", linestyle="--", linewidth=1.2,
           label=f"Haftalık Ort. {haftalik_ort:,.0f} TL")
ax.legend(fontsize=9)

plt.title(
    "Haftalık Toplam Gelir Trendi", fontsize=14, fontweight="bold", pad=25
)
plt.text(
    0.5, 1.02, alt_baslik,
    transform=ax.transAxes, ha="center", fontsize=9.5, color="gray",
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
plt.savefig(VISUALS_DIR / "gelir-zaman-serisi.png", dpi=300)
plt.close()

# ---------------------------------------------------------
# 2. GRAFİK: Kırılım (Kanala Göre Birleşik ROAS: Σ gelir_tl / Σ harcama_tl)
# ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.5))

# Birleşik ROAS = Toplam Gelir / Toplam Harcama (satır ortalaması değil)
df_channel = df.groupby(channel_col, as_index=False).agg(
    {revenue_col: "sum", spend_col: "sum"}
)
df_channel["roas_val"] = df_channel[revenue_col] / df_channel[spend_col]

# ROAS'a göre büyükten küçüğe sırala (analiz §5: ilk üç kanal)
df_channel = df_channel.sort_values("roas_val", ascending=False).reset_index(drop=True)

bars = ax.bar(
    df_channel[channel_col],
    df_channel["roas_val"],
    color="#2ca02c",
    width=0.5,
)

plt.title(
    "Pazarlama Kanalına Göre Birleşik ROAS (Σ Gelir / Σ Harcama)",
    fontsize=13, fontweight="bold", pad=25,
)
plt.text(
    0.5, 1.02, alt_baslik,
    transform=ax.transAxes, ha="center", fontsize=9.5, color="gray",
)

plt.xlabel("Kanal", fontsize=11, labelpad=10)
plt.ylabel("Birleşik ROAS (x)", fontsize=11)

max_y = df_channel["roas_val"].max()
for bar in bars:
    yval = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        yval + (max_y * 0.02),
        f"{yval:.2f}x",
        ha="center", va="bottom", fontsize=10, fontweight="bold",
    )

ax.set_ylim(0, max_y * 1.18)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig(VISUALS_DIR / "kanal-kirilim.png", dpi=300)
plt.close()

print("Grafikler analiz dokümanındaki birleşik ROAS hesabı ile güncellendi!")
