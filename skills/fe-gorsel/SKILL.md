---
name: fe-gorsel
description: Kampanya verisinden 3 grafik üretir (haftalık gelir ve harcama trendi, kanal bazlı ROAS ve CTR, kampanya-hafta ROAS dağılımı) ve PNG olarak visuals/ klasörüne kaydeder. FE rolünün G2 görselleştirme görevi için kullanılır.
---

# fe-gorsel: Kampanya verisinden 3 grafik üretme (G2, FE)

## Amaç
`data/kampanya-simulasyon-g2.csv` verisinden, veri sözlüğündeki metriklere bağlı 3 grafik üretir: bir zaman serisi, bir kategorik kırılım ve bir dağılım. Her grafik başlık, eksen etiketi, birim ve doğru Türkçe karakterle PNG olarak `visuals/` klasörüne yazılır. Grafikteki sayılar `docs/analiz-g2.md` ile tutarlı olmalıdır.

## Ne zaman kullanılır?
- G2 görevinde FE olarak grafikleri ilk kez ya da veri değiştiğinde yeniden üretirken
- DQ ya da PR incelemesinden sonra bir grafiği düzeltirken

## Kullanılan dosyalar
| Dosya | Rol |
|---|---|
| `data/kampanya-simulasyon-g2.csv` | Girdi (G2 verisi yoksa iskelet `data/kampanya-performans.csv` ile çalışır ve uyarı yazar) |
| `docs/veri-sozlugu.md` | Alanlar, kurallar ve M1–M5 metrik tanımları |
| `docs/analiz-g2.md` | Grafik sayılarının karşılaştırılacağı analiz raporu |
| `src/grafik_uret.py` | Grafik üreten betik |
| `visuals/gelir-harcama-trendi.png` | Çıktı 1: haftalık gelir ve harcama trendi (çizgi, M3) |
| `visuals/kanal-roas-ctr.png` | Çıktı 2: kanal bazlı birleşik ROAS ve CTR (çubuk, M4) |
| `visuals/roas-dagilimi.png` | Çıktı 3: kampanya-hafta ROAS dağılımı (histogram, M5 ile ilişkili) |

Görev 1'in grafikleri (`visuals/gelir-zaman-serisi.png`, `visuals/kanal-kirilim.png`, betik: `src/generate_visuals.py`) bu görevle değişmez.

## Metrik tanımları
- **Birleşik ROAS** (kanal) = Σ `gelir_tl` / Σ `harcama_tl`. Satır ortalaması ALINMAZ.
- **CTR** (kanal) = Σ `tiklama` / Σ `gosterim` × 100 (birim: %).
- **Kampanya-hafta ROAS** (satır) = `gelir_tl` / `harcama_tl` (veri sözlüğü `harcama_tl > 0` garanti eder).
- **Haftalık gelir / harcama** = aynı `tarih` değerindeki tüm kanalların toplamı.

## Çıktı format kuralları
- Biçim: PNG, 200 dpi; pencere açılmaz (`matplotlib.use("Agg")`).
- Her grafikte: başlık, alt başlık (kanal sayısı · hafta sayısı · tarih aralığı), eksen etiketleri ve birim: TL, adet, oran (x), %.
- Tutarlarda binlik ayracı nokta: `12.345.678`.
- Türkçe karakterler (ş, ı, ğ, ö, ü, ç) düzgün görünmeli.
- Çubuk grafiklerde değer etiketi çubuğun üstünde yazılır; çubuklar ROAS'a göre büyükten küçüğe sıralanır.
- Eksen kesilmez, birimsiz ya da başlıksız grafik üretilmez.

## Adım adım talimat
1. `docs/veri-sozlugu.md` dosyasındaki alan adlarını ve metrik tanımlarını kontrol et.
2. Veriyi oku: G2 dosyası varsa onu, yoksa uyarı vererek G1 dosyasını kullan.
3. Veriyi doğrula: sütunlar tam mı, `tiklama ≤ gosterim`, `donusum ≤ tiklama`, `harcama_tl > 0`, `gelir_tl ≥ 0`. Biri bozuksa grafik üretme, DQ'ya bildir.
4. `python src/grafik_uret.py` ile 3 grafiği üret.
5. PNG'leri aç ve her birinde başlık, eksen etiketi, birim ve Türkçe karakteri gözle kontrol et.
6. Grafikteki sayıları `docs/analiz-g2.md` ile karşılaştır. Uyuşmuyorsa dur ve nedenini bul (veri mi, formül mü).
7. `feature/gorsel` dalında commit et. `main`'e doğrudan commit yapılmaz; PR aç, reviewer olarak DQ'yu ekle.
8. Kapanış yorumuna kanıtı yaz: commit hash + dosyalar + prompt özeti (aşağıdaki şablon).

## Çalıştırma
Deponun kök klasöründe:
```bash
python src/grafik_uret.py
python src/grafik_uret.py --veri data/senaryo_10_hafta.csv --cikti_dizini visuals/senaryo
```
Argümanlar (hepsi isteğe bağlı):
- `--veri`: okunacak CSV (varsayılan: `data/kampanya-simulasyon-g2.csv`, yoksa G1 verisi)
- `--cikti_dizini`: PNG'lerin yazılacağı klasör (varsayılan: `visuals/`)

Veri dosyası yoksa ya da gerekli sütunlar eksikse betik hata mesajı verip durur, grafik üretmez.
Gerekli paketler: `pandas`, `matplotlib` (`pip install pandas matplotlib`).

## Örnek giriş / çıktı
**Giriş:** `data/kampanya-performans.csv` (260 satır: 5 kanal × 52 hafta, 2025-10-06 – 2026-09-28)
**Komut:** `python src/grafik_uret.py`
**Çıktı (terminal):**
```
UYARI: G2 verisi yok, iskelet G1 verisiyle çalışıyor. Son hâl için G2 verisi gerekli.
3 grafik üretildi (260 satır, kaynak: kampanya-performans.csv) -> .../visuals
```
**Çıktı (grafikler, bu veride):** kanal grafiğinde birleşik ROAS: E-posta 45,50x, SEO 23,26x, Google Ads 4,21x, Meta Ads 3,75x, TikTok Ads 2,88x; E-posta CTR %5,02; histogramda medyan 5,26x, ortalama 17,43x. G2 verisiyle değerler değişebilir, her zaman `docs/analiz-g2.md` ile karşılaştır.

## Reddetme durumları
Şu isteklerde skill grafik üretmez ve nedenini söyler:
- **Gerçek kişisel veri talebi:** İsim, telefon, e-posta, T.C. kimlik no, IP gibi gerçek kişi ya da kurum bilgisi isteyen ya da içeren her talep reddedilir. Veri tamamen sentetiktir, depoya gerçek kişi verisi girmez.
- **Şemaya uymayan veri:** Eksik sütun, `tiklama > gosterim`, `harcama_tl ≤ 0` gibi sözlük kurallarını bozan veri için grafik üretilmez; DQ'ya bildirilir.
- **Tanımsız metrik:** Veri sözlüğünde olmayan bir metrik uydurulmaz.
- **Yanıltıcı grafik:** Eksen kesme, başlıksız ya da birimsiz grafik gibi kural dışı isteklere uyulmaz.
- **Analizle çelişen sayı:** `docs/analiz-g2.md` ile uyuşmayan grafik teslim edilmez, önce fark araştırılır.
- **`main`'e doğrudan commit:** Reddedilir; dal ve PR kullanılır.

## Kapanış yorumu şablonu
```
Kanıt: commit <hash> — src/grafik_uret.py, visuals/gelir-harcama-trendi.png, visuals/kanal-roas-ctr.png, visuals/roas-dagilimi.png, skills/fe-gorsel/SKILL.md.
Üretim: fe-gorsel skill'i ile, <araç> — prompt özeti: <ne istendi, hangi dosyalar girdi, hangi kontroller yapıldı>.
```
