# Veri Sözlüğü — Kampanya Performansı (G1)
**Sürüm:** v2 · **BE:** Özge Nur Doğu · **DQ:** Nuri Enes Seyhan · **Tarih:** 2026-10-18

## Veri Kümesi: data/kampanya-performans.csv
Dijital pazarlama kanallarının haftalık performansını gösteren **sentetik** veri. Her satır, bir kanalın bir haftalık sonucudur. Gerçek kişi veya şirket verisi içermez.

| Alan | Tip | Kural/Aralık | Birim | Örnek |
|---|---|---|---|---|
| kampanya_id | Metin | `K` + 3 haneli sıra no, benzersiz (K001–K260) | — | K001 |
| tarih | Tarih | yyyy-mm-dd, haftanın Pazartesi günü (2025-10-06 ile 2026-09-28 arası, 52 hafta) | tarih | 2025-10-06 |
| kanal | Metin (kategorik) | 5 sabit değerden biri: Google Ads, Meta Ads, TikTok Ads, E-posta, SEO | — | Google Ads |
| gosterim | Tam sayı | 5.000 – 250.000 | adet | 54592 |
| tiklama | Tam sayı | 1 ≤ tiklama ≤ gosterim | adet | 1146 |
| donusum | Tam sayı | 0 ≤ donusum ≤ tiklama | adet | 35 |
| harcama_tl | Ondalık | > 0, **CSV'de her zaman tam 2 ondalık basamak** (`4717.00`, `4717.0` değil) | TL | 4717.00 |
| gelir_tl | Ondalık | ≥ 0, **CSV'de her zaman tam 2 ondalık basamak** | TL | 26888.25 |

## Kategori Değerleri
`kanal`: Google Ads, Meta Ads, TikTok Ads, E-posta, SEO (her biri 52 satır).

## Kurallar
- `kampanya_id` benzersizdir ve `K` + 3 rakam biçimindedir.
- `tarih` yyyy-mm-dd biçiminde ve her zaman bir Pazartesidir.
- `tiklama` hiçbir satırda `gosterim`'den büyük olamaz.
- `donusum` hiçbir satırda `tiklama`'dan büyük olamaz.
- `harcama_tl` her satırda sıfırdan büyüktür (ROAS = gelir_tl / harcama_tl bölmesi güvenli olsun diye).
- `harcama_tl` ve `gelir_tl` dosyada daima tam iki ondalık basamakla yazılır.
- Her kanalda eşit sayıda (52) satır vardır.
- Üretim sabit tohumla (SEED = 42) yapılır; aynı betik aynı dosyayı verir.
- Bu kuralların **hepsi** betikte dosya yazılmadan önce kontrol edilir; biri bozuksa dosya yazılmaz.

## Hedef Boyut
5 kanal × 52 hafta = **260 satır** + 1 başlık satırı. CSV biçimi: UTF-8, ayraç virgül (`,`), ondalık ayracı nokta (`.`), satır sonu `\n`.

## Üretim
`src/kampanya_simulasyon.py` betiği (`python src/kampanya_simulasyon.py`).

## Değişiklik Günlüğü
- v1 — ilk sürüm (2026-10-17): 130 satır.
- v2 — DQ geri bildirimiyle (2026-10-18): tutarlar daima 2 ondalık basamakla yazılıyor; betik şemadaki tüm kuralları doğruluyor; veri 260 satıra çıkarıldı (52 hafta); tarihler geçmişe alındı (2025-10-06 başlangıç).
