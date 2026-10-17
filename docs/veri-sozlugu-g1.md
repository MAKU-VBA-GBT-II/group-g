# Veri Sözlüğü — Kampanya Performansı (G1)
**Sürüm:** v1 · **BE:** Özge Nur Doğu · **DQ:** Nuri Enes Seyhan · **Tarih:** 2026-10-17

## Veri Kümesi: data/kampanya-performans.csv
Dijital pazarlama kanallarının haftalık performansını gösteren **sentetik** veri. Her satır, bir kanalın bir haftalık sonucudur. Gerçek kişi veya şirket verisi içermez.

| Alan | Tip | Kural/Aralık | Birim | Örnek |
|---|---|---|---|---|
| kampanya_id | Metin | `K` + 3 haneli sıra no, benzersiz (K001–K130) | — | K001 |
| tarih | Tarih | yyyy-mm-dd, haftanın Pazartesi günü (2026-03-02 ile 2026-08-24 arası, 26 hafta) | tarih | 2026-03-02 |
| kanal | Metin (kategorik) | 5 sabit değerden biri: Google Ads, Meta Ads, TikTok Ads, E-posta, SEO | — | Google Ads |
| gosterim | Tam sayı | 5.000 – 250.000 | adet | 54592 |
| tiklama | Tam sayı | 1 ≤ tiklama ≤ gosterim | adet | 1146 |
| donusum | Tam sayı | 0 ≤ donusum ≤ tiklama | adet | 35 |
| harcama_tl | Ondalık | > 0, 2 ondalık basamak | TL | 4717.00 |
| gelir_tl | Ondalık | ≥ 0, 2 ondalık basamak | TL | 26888.25 |

## Kategori Değerleri
`kanal`: Google Ads, Meta Ads, TikTok Ads, E-posta, SEO (her biri 26 satır).

## Kurallar
- `tiklama` hiçbir satırda `gosterim`'den büyük olamaz.
- `donusum` hiçbir satırda `tiklama`'dan büyük olamaz.
- `harcama_tl` her satırda sıfırdan büyüktür (ROAS = gelir_tl / harcama_tl bölmesi güvenli olsun diye).
- Üretim sabit tohumla (SEED = 42) yapılır; aynı betik aynı dosyayı verir.

## Hedef Boyut
5 kanal × 26 hafta = **130 satır** + 1 başlık satırı. CSV biçimi: UTF-8, ayraç virgül (`,`), ondalık ayracı nokta (`.`).

## Üretim
`src/kampanya_simulasyon.py` betiği (`python src/kampanya_simulasyon.py`).

## Değişiklik Günlüğü
- v1 — ilk sürüm (2026-10-17)
