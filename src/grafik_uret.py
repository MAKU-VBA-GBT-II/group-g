"""G2 - FE: Mini ürünün 3 grafiği (zaman serisi, kategorik kırılım, dağılım).

Çıktılar (visuals/ klasörüne PNG):
  1) gelir-harcama-trendi.png : Haftalık gelir ve harcama trendi      (M3, çizgi)
  2) kanal-roas-ctr.png       : Kanal bazlı birleşik ROAS ve CTR      (M4, çubuk)
  3) roas-dagilimi.png        : Kampanya-hafta ROAS dağılımı          (M5 ile ilişkili, histogram)

Çalıştırma (deponun kök klasöründe):
    python src/grafik_uret.py
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # pencere açmadan doğrudan dosyaya çiz
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FuncFormatter

KOK = Path(__file__).resolve().parent.parent
VISUALS = KOK / "visuals"
VISUALS.mkdir(parents=True, exist_ok=True)

# Görev 2 verisi hazır olunca otomatik onu kullanır; yoksa G1 verisiyle iskeleti çalıştırır.
VERI_G2 = KOK / "data" / "kampanya-simulasyon-g2.csv"
VERI_G1 = KOK / "data" / "kampanya-performans.csv"
VERI_YOLU = VERI_G2 if VERI_G2.exists() else VERI_G1
if VERI_YOLU == VERI_G1:
    print("UYARI: G2 verisi yok, iskelet G1 verisiyle çalışıyor. Son hâl için G2 verisi gerekli.")

MAVI, TURUNCU, YESIL = "#2b6cb0", "#d9622b", "#2f855a"
DPI = 200


def tl_bicimi(x, _pos=None):
    """12345678 -> 12.345.678 (Türkçe binlik ayracı)."""
    return f"{x:,.0f}".replace(",", ".")


def alt_baslik(df):
    return (f"{df['kanal'].nunique()} kanal · {df['tarih'].nunique()} hafta · "
            f"{df['tarih'].min()} – {df['tarih'].max()}")


def trend_grafigi(df):
    """1) Haftalık gelir ve harcama trendi (zaman serisi)."""
    haftalik = df.groupby("tarih", as_index=False)[["gelir_tl", "harcama_tl"]].sum()
    fig, ax = plt.subplots(figsize=(11, 5.5))
    ax.plot(haftalik["tarih"], haftalik["gelir_tl"], color=MAVI, linewidth=2, label="Gelir")
    ax.plot(haftalik["tarih"], haftalik["harcama_tl"], color=TURUNCU, linewidth=2, label="Harcama")
    ax.set_title("Haftalık Gelir ve Harcama Trendi", fontsize=14, fontweight="bold", pad=28)
    ax.text(0.5, 1.02, alt_baslik(df), transform=ax.transAxes, ha="center", fontsize=9.5, color="gray")
    ax.set_xlabel("Hafta (haftanın Pazartesi tarihi)", fontsize=11)
    ax.set_ylabel("Tutar (TL / hafta)", fontsize=11)
    ax.yaxis.set_major_formatter(FuncFormatter(tl_bicimi))
    adim = max(1, len(haftalik) // 12)
    ax.set_xticks(range(0, len(haftalik), adim))
    ax.set_xticklabels(haftalik["tarih"].iloc[::adim], rotation=45, ha="right", fontsize=9)
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend()
    fig.tight_layout()
    fig.savefig(VISUALS / "gelir-harcama-trendi.png", dpi=DPI)
    plt.close(fig)


def kanal_grafigi(df):
    """2) Kanal bazlı birleşik ROAS ve CTR (kategorik kırılım)."""
    k = df.groupby("kanal", as_index=False)[["gelir_tl", "harcama_tl", "tiklama", "gosterim"]].sum()
    k["roas"] = k["gelir_tl"] / k["harcama_tl"]
    k["ctr"] = k["tiklama"] / k["gosterim"] * 100
    k = k.sort_values("roas", ascending=False).reset_index(drop=True)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))
    for ax, sutun, renk, baslik, etiket, bicim in (
        (ax1, "roas", MAVI, "Birleşik ROAS (Σ gelir / Σ harcama)", "Birleşik ROAS (oran, x)", "{:.2f}x"),
        (ax2, "ctr", YESIL, "CTR (Σ tıklama / Σ gösterim)", "CTR (%)", "%{:.2f}"),
    ):
        cubuklar = ax.bar(k["kanal"], k[sutun], color=renk, width=0.55)
        ax.set_title(baslik, fontsize=12, fontweight="bold")
        ax.set_xlabel("Kanal", fontsize=11)
        ax.set_ylabel(etiket, fontsize=11)
        ax.tick_params(axis="x", rotation=20)
        ax.set_ylim(0, k[sutun].max() * 1.18)
        ax.grid(axis="y", linestyle="--", alpha=0.5)
        for c, deger in zip(cubuklar, k[sutun]):
            ax.text(c.get_x() + c.get_width() / 2, deger, bicim.format(deger),
                    ha="center", va="bottom", fontsize=9, fontweight="bold")
    fig.suptitle("Kanal Bazlı ROAS ve CTR Karşılaştırması", fontsize=14, fontweight="bold")
    fig.text(0.5, 0.925, alt_baslik(df), ha="center", fontsize=9.5, color="gray")
    fig.tight_layout(rect=[0, 0, 1, 0.92])
    fig.savefig(VISUALS / "kanal-roas-ctr.png", dpi=DPI)
    plt.close(fig)


def roas_dagilimi(df):
    """3) Kampanya-hafta ROAS dağılımı (histogram)."""
    roas = df["gelir_tl"] / df["harcama_tl"]
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.hist(roas, bins=20, color=MAVI, edgecolor="white")
    ax.axvline(roas.median(), color=TURUNCU, linestyle="--", linewidth=1.8,
               label=f"Medyan: {roas.median():.2f}x")
    ax.axvline(roas.mean(), color=YESIL, linestyle="--", linewidth=1.8,
               label=f"Ortalama: {roas.mean():.2f}x")
    ax.set_title("Kampanya-Hafta ROAS Dağılımı", fontsize=14, fontweight="bold", pad=28)
    ax.text(0.5, 1.02, f"{len(roas)} kampanya-hafta kaydı · ROAS = gelir / harcama",
            transform=ax.transAxes, ha="center", fontsize=9.5, color="gray")
    ax.set_xlabel("ROAS (oran, x)", fontsize=11)
    ax.set_ylabel("Kampanya-hafta sayısı (adet)", fontsize=11)
    ax.grid(axis="y", linestyle="--", alpha=0.5)
    ax.legend()
    fig.tight_layout()
    fig.savefig(VISUALS / "roas-dagilimi.png", dpi=DPI)
    plt.close(fig)


def main():
    df = pd.read_csv(VERI_YOLU)
    trend_grafigi(df)
    kanal_grafigi(df)
    roas_dagilimi(df)
    print(f"3 grafik üretildi ({len(df)} satır, kaynak: {VERI_YOLU.name}) -> {VISUALS}")


if __name__ == "__main__":
    main()
