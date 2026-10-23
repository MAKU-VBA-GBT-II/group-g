# Veri Sözlüğü — Kampanya Performansı (G1)
**Sürüm:** v3 · **BE:** Özge Nur Doğu · **DQ:** Nuri Enes Seyhan · **Tarih:** 2026-10-23

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
| gelir_tl | Ondalık | ≥ 0, **CSV'de her zaman tam 2 ondalık basamak**; donusum = 0 ise `0.00` | TL | 26888.25 |

## Kategori Değerleri
`kanal`: Google Ads, Meta Ads, TikTok Ads, E-posta, SEO (her biri 52 satır).

## Kurallar
- `kampanya_id` benzersizdir ve `K` + 3 rakam biçimindedir.
- `tarih` yyyy-mm-dd biçiminde ve her zaman bir Pazartesidir.
- `tiklama` hiçbir satırda `gosterim`'den büyük olamaz.
- `donusum` hiçbir satırda `tiklama`'dan büyük olamaz.
- `donusum` 0 ise `gelir_tl` de `0.00` olur (gelir = donusum × sepet olduğu için).
- `harcama_tl` her satırda sıfırdan büyüktür (ROAS = gelir_tl / harcama_tl bölmesi güvenli olsun diye).
- `harcama_tl` ve `gelir_tl` dosyada daima tam iki ondalık basamakla yazılır.
- Her kanalda eşit sayıda (52) satır vardır.
- Üretim sabit tohumla (SEED = 42) yapılır; aynı betik aynı dosyayı verir.
- Bu kuralların **hepsi** betikte dosya yazılmadan önce kontrol edilir; biri bozuksa dosya yazılmaz. Dosya yazıldıktan sonra başlık satırı ve satır sayısı da yeniden doğrulanır.

## Simülasyon parametreleri
Verinin karakterini (hangi kanal ne kadar verimli) belirleyen sayılar bunlardır. Betikteki `KANALLAR` sözlüğü bu tabloyla **birebir aynıdır**.

| Kanal | gosterim (haftalık) | ctr (tıklama oranı) | cvr (dönüşüm oranı) | cpc (TL/tıklama) | sepet (TL/dönüşüm) |
|---|---|---|---|---|---|
| Google Ads | 40.000 – 120.000 | 0,020 – 0,060 | 0,020 – 0,060 | 3,0 – 8,0 | 400 – 900 |
| Meta Ads | 60.000 – 180.000 | 0,010 – 0,030 | 0,010 – 0,040 | 2,0 – 5,0 | 300 – 700 |
| TikTok Ads | 80.000 – 250.000 | 0,005 – 0,020 | 0,005 – 0,025 | 1,5 – 4,0 | 250 – 600 |
| E-posta | 5.000 – 30.000 | 0,020 – 0,080 | 0,030 – 0,080 | 0,3 – 1,0 | 350 – 800 |
| SEO | 20.000 – 90.000 | 0,020 – 0,050 | 0,020 – 0,050 | 0,5 – 1,5 | 400 – 900 |

## Türetme formülleri
Her satır için, ilgili kanalın aralıklarından değerler çekilir (`gosterim` aralıktan rastgele tam sayı, `ctr`, `cvr`, `cpc`, `sepet` aralıktan eşit olasılıklı ondalık sayı):

```
tiklama    = max(1, int(gosterim × ctr))
donusum    = int(tiklama × cvr)
harcama_tl = round(tiklama × cpc, 2)
gelir_tl   = round(donusum × sepet, 2)
```

Tutarlar CSV'ye `f"{x:.2f}"` ile yazılır.

## Üretim sırası
- Üreteç: Python `random.Random(42)`.
- Satır sırası: önce hafta (2025-10-06'dan başlayarak 52 hafta), her haftada kanallar tabloda yazılı sırayla (Google Ads, Meta Ads, TikTok Ads, E-posta, SEO).
- Her satırda rastgele sayılar şu sırayla çekilir: `gosterim`, `ctr`, `cvr`, `cpc`, `sepet`.

## Hedef Boyut
5 kanal × 52 hafta = **260 satır** + 1 başlık satırı. CSV biçimi: UTF-8, ayraç virgül (`,`), ondalık ayracı nokta (`.`), satır sonu `\n`.

## Üretim
`src/kampanya_simulasyon.py` betiği (`python src/kampanya_simulasyon.py`).

## Değişiklik Günlüğü
- v1 — ilk sürüm (2026-10-17): 130 satır.
- v2 — DQ geri bildirimiyle (2026-10-18): tutarlar daima 2 ondalık basamakla yazılıyor; betik şemadaki tüm kuralları doğruluyor; veri 260 satıra çıkarıldı (52 hafta); tarihler geçmişe alındı (2025-10-06 başlangıç).
- v3 — Grup A (Hilal Elçin Şahin) incelemesiyle (2026-10-23): simülasyon parametreleri, türetme formülleri ve üretim sırası eklendi; `donusum = 0` ise `gelir_tl = 0.00` kuralı yazıldı; betikteki işlevsiz başlık kontrolü, yazılan dosyayı geri okuyan gerçek bir kontrolle değiştirildi. **Veri dosyası değişmedi** (SHA-256 aynı).
