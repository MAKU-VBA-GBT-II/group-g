# G1 — Kampanya Performansı Veri Kalitesi Test Senaryoları

Şema referansı: [`docs/veri-sozlugu-g1.md`](../docs/veri-sozlugu-g1.md)
Test verisi: `data/kampanya-performans.csv`

Beklenen sonuçlar veri sözlüğüne dayanır. Üretim betiğinin doğrulama adımları sözlükteki tüm biçim kurallarını kontrol etmez; CSV'de tutarların iki ondalık basamakla yazılması ayrıca doğrulanmalıdır.

| No | Senaryo | Adımlar | Beklenen sonuç | Gerçekleşen sonuç | Durum |
|---:|---|---|---|---|---|
| 1 | Dosya var mı? | Depo kökünden `data/kampanya-performans.csv` yolunu kontrol et. | Dosya mevcut ve okunabilir olmalı. |  | Beklemede — Hafta 4'te yürütülecek |
| 2 | Veri satırı sayısı | CSV'yi başlığı ayrı tutarak oku ve veri kayıtlarını say. | En az 100 veri satırı olmalı; hedef sayı 130'dur (başlık hariç). |  | Beklemede — Hafta 4'te yürütülecek |
| 3 | Sütun adları ve sırası | CSV'nin ilk satırını `docs/veri-sozlugu-g1.md` içindeki alanlarla karşılaştır. | Başlık tam olarak şu 8 alanı bu sırayla içermeli: `kampanya_id`, `tarih`, `kanal`, `gosterim`, `tiklama`, `donusum`, `harcama_tl`, `gelir_tl`. |  | Beklemede — Hafta 4'te yürütülecek |
| 4 | Tipler, biçimler ve değer aralıkları | Her `kampanya_id` değerinin `K` ve 3 rakam biçiminde ve benzersiz olduğunu; `tarih` değerlerinin `yyyy-mm-dd` biçiminde, Pazartesi günü ve `2026-03-02`–`2026-08-24` aralığında olduğunu kontrol et. `gosterim`, `tiklama`, `donusum` alanlarının tam sayı; `harcama_tl`, `gelir_tl` alanlarının sayısal olduğunu doğrula. Her satırda `5000 <= gosterim <= 250000`, `1 <= tiklama <= gosterim`, `0 <= donusum <= tiklama`, `harcama_tl > 0`, `gelir_tl >= 0` koşullarını ve iki tutarın da CSV'de tam iki ondalık basamakla yazıldığını kontrol et. | Tüm kayıtlar veri sözlüğündeki tip, biçim ve aralık kurallarına uymalı; kural ihlali veya sayısal dönüşüm hatası bulunmamalı. |  | Beklemede — Hafta 4'te yürütülecek |
| 5 | Kanal kategori değerleri | `kanal` alanındaki farklı değerler kümesini çıkar ve izin verilen değerlerle karşılaştır: `Google Ads`, `Meta Ads`, `TikTok Ads`, `E-posta`, `SEO`. | Tüm değerler izin verilen 5 kategoriden biri olmalı ve en az 4 farklı kategori bulunmalı. |  | Beklemede — Hafta 4'te yürütülecek |
