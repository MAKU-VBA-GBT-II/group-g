---
name: fe-gorsel
description: Kampanya verisinden haftalık gelir trendi ve kanal birleşik ROAS grafiklerini üretir.
---

# FE Görselleştirme Becerisi (Skill)

## Rol ve Sorumluluk
- **Rol:** FE (Ön Yüz / Görselleştirici)
- **Görev:** `data/kampanya-performans.csv` verilerini ve `docs/analiz-g1.md` raporundaki metrikleri kullanarak standartlara uygun, açıklayıcı 2 adet PNG formatında veri görseli üretmek ve `visuals/` dizinine kaydetmek.

## Girdi ve Bağımlılıklar
- **Veri Dosyası:** `data/kampanya-performans.csv`
  - Kullanılan sütunlar: `tarih`, `kanal`, `gelir_tl`, `harcama_tl`
- **Analiz Dokümanı:** `docs/analiz-g1.md`

## Çıktılar
- `visuals/gelir-zaman-serisi.png` (Haftalık toplam gelir zaman serisi)
- `visuals/kanal-kirilim.png` (Kanala göre birleşik ROAS kırılımı)

## Metrik Tanımları
- **Birleşik ROAS** = Σ `gelir_tl` / Σ `harcama_tl` (kanal bazında toplam; satır ortalaması ALINMAZ)
- `docs/analiz-g1.md` §4 ile kontrol: E-posta ~45,50x, SEO ~23,26x, TikTok Ads ~2,88x
- Haftalık ortalama gelir ~202.722,56 TL — zaman serisi grafiğinde kesikli çizgi ile gösterilmeli

## İş Akışı ve Adımlar
1. `data/kampanya-performans.csv` veri setini oku.
2. Sütun adlarını doğrudan kullan: `tarih`, `kanal`, `gelir_tl`, `harcama_tl`.
3. Gelir verilerini `tarih` bazında gruplayarak zaman serisi çizgi grafiği oluştur (`visuals/gelir-zaman-serisi.png`). Haftalık ortalama geliri kesikli çizgiyle ekle.
4. ROAS verilerini `kanal` bazında **birleşik ROAS** (Σ gelir_tl / Σ harcama_tl) ile hesapla, ROAS'a göre büyükten küçüğe sırala, sütun grafiği oluştur (`visuals/kanal-kirilim.png`).
5. Her iki grafikte de eksen etiketlerini, başlıkları ve birimleri (`TL`, `x`) eksiksiz ekle.
6. Çıktılar `docs/analiz-g1.md` §4 değerleriyle örtüşmüyorsa dur ve kontrol et.

## Çalıştırma Komutu
```bash
python src/generate_visuals.py
```
