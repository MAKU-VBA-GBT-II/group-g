# G1 — Kampanya Performansı Veri Kalitesi Test Senaryoları

Şema referansı: [`docs/veri-sozlugu-g1.md`](../docs/veri-sozlugu-g1.md)
Test verisi: `data/kampanya-performans.csv`

| No | Senaryo | Adımlar | Beklenen sonuç | Gerçekleşen sonuç | Durum |
|---:|---|---|---|---|---|
| 1 | Dosya var mı? | Depo kökünden `data/kampanya-performans.csv` yolunu kontrol et. | Dosya mevcut ve okunabilir olmalı. |  | Beklemede — Hafta 4'te yürütülecek |
| 2 | Veri satırı sayısı | CSV'yi başlığı ayrı tutarak oku ve veri kayıtlarını say. | En az 100 veri satırı olmalı; hedef sayı 130'dur (başlık hariç). |  | Beklemede — Hafta 4'te yürütülecek |
| 3 | Sütun adları ve sırası | CSV'nin ilk satırını `docs/veri-sozlugu-g1.md` içindeki alanlarla karşılaştır. | Başlık tam olarak şu 8 alanı bu sırayla içermeli: `kampanya_id`, `tarih`, `kanal`, `gosterim`, `tiklama`, `donusum`, `harcama_tl`, `gelir_tl`. |  | Beklemede — Hafta 4'te yürütülecek |
| 4 | Tipler ve değer aralıkları | Tüm kayıtları dolaş; `gosterim`, `tiklama`, `donusum` alanlarını tam sayı; `harcama_tl`, `gelir_tl` alanlarını ondalık sayı olarak doğrula. Her kayıt için `5000 <= gosterim <= 250000`, `1 <= tiklama <= gosterim`, `0 <= donusum <= tiklama`, `harcama_tl > 0` ve `gelir_tl >= 0` kontrollerini uygula. Tutarların iki ondalık basamaklı olduğunu da kontrol et. | Her satır belirtilen tipe ve aralıklara uymalı; kural ihlali veya sayısal dönüşüm hatası bulunmamalı. |  | Beklemede — Hafta 4'te yürütülecek |
| 5 | Kanal kategori değerleri | `kanal` alanındaki farklı değerler kümesini çıkar ve izin verilen değerlerle karşılaştır: `Google Ads`, `Meta Ads`, `TikTok Ads`, `E-posta`, `SEO`. | Tüm değerler izin verilen 5 kategoriden biri olmalı ve en az 4 farklı kategori bulunmalı. |  | Beklemede — Hafta 4'te yürütülecek |
