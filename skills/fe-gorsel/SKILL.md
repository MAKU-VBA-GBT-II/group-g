# FE Görselleştirme Becerisi (Skill)

## Rol ve Sorumluluk
- **Rol:** FE (Ön Yüz / Görselleştirici)
- **Görev:** `data/kampanya-performans.csv` verilerini ve `docs/analiz-g1.md` raporundaki metrikleri kullanarak standartlara uygun, açıklayıcı 2 adet PNG formatında veri görseli üretmek ve `visuals/` dizinine kaydetmek.

## Girdi ve Bağımlılıklar
- **Veri Dosyası:** `data/kampanya-performans.csv`
- **Analiz Dokümanı:** `docs/analiz-g1.md`

## Çıktılar
- `visuals/gelir-zaman-serisi.png` (Haftalık toplam gelir zaman serisi)
- `visuals/kanal-kirilim.png` (Kanala göre ortalama ROAS kırılımı)

## İş Akışı ve Adımlar
1. `data/kampanya-performans.csv` veri setini oku.
2. Gelir verilerini haftalık bazda gruplayarak zaman serisi çizgi grafiği oluştur (`visuals/gelir-zaman-serisi.png`).
3. ROAS verilerini kanal bazında gruplayarak sütun grafiği oluştur (`visuals/kanal-kirilim.png`).
4. Her iki grafikte de eksen etiketlerini, başlıkları ve birimleri (`TL`, `x`) eksiksiz ekle.

## Çalıştırma Komutu
```bash
python generate_visuals.py