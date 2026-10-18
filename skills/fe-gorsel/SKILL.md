# FE Görselleştirme Becerisi (Skill)

## Amaç
Bu skill, `data/kampanya-performans.csv` verilerini ve `docs/analiz-g1.md` metriklerini kullanarak iki adet standart veri görseli (PNG) üretir.

## Talimatlar
1. `data/kampanya-performans.csv` dosyasından haftalık gelir ve kanala göre ROAS verilerini oku ve grupla.
2. Grafiklerde eksen etiketleri, başlıklar ve birimleri (TL, x) tanımla.
3. Üretilen görselleri `visuals/` klasörü altına kaydet:
   - `visuals/gelir-zaman-serisi.png`
   - `visuals/kanal-kirilim.png`

## Kullanılan Dosyalar
- `data/kampanya-performans.csv`
- `docs/analiz-g1.md`

## Çalıştırma Komutu
```bash
python generate_visuals.py