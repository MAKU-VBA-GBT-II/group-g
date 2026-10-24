# G1 — Kampanya Performansı Veri Kalitesi Test Senaryoları

Şema referansı: [`docs/veri-sozlugu-g1.md`](../docs/veri-sozlugu-g1.md)
Test verisi: `data/kampanya-performans.csv`
Çalıştırma: `python src/dq_test.py`

Beklenen değerler güncel veri sözlüğünden ve `src/kampanya_simulasyon.py` içindeki şema sabitlerinden alınır. Sözlük ile betik arasında çelişki varsa koşumdan önce raporlanmalıdır. Bu dosya test tanımlarını içerir; gerçek sonuçların tek yetkili kaynağı `tests/test-log.md` dosyasındaki tarihli kayıtlardır.

| ID | Senaryo | Adımlar | Beklenen sonuç |
|---|---|---|---|
| TC-01 | Dosya var ve okunabilir | Depo kökünden varsayılan CSV dosyasını aç. | Dosya mevcut olmalı ve UTF-8 olarak okunabilmeli. |
| TC-02 | Tam veri satırı sayısı | Başlık hariç CSV kayıtlarını say. | Veri sözlüğünde tanımlanan 52 hafta × 5 kanal kadar, tam 260 kayıt bulunmalı. |
| TC-03 | Sütun adları ve sırası | CSV başlığını sözlükteki alanlarla ve üretici betiğinin başlığıyla karşılaştır. | Tam olarak `kampanya_id`, `tarih`, `kanal`, `gosterim`, `tiklama`, `donusum`, `harcama_tl`, `gelir_tl` sırası bulunmalı. |
| TC-04 | Kampanya kimlikleri | Tüm `kampanya_id` değerlerinin biçimini, sırasını ve benzersizliğini kontrol et. | Her kimlik `K` + üç rakam biçiminde olmalı; kayıtlar K001'den başlayarak sıralı ve benzersiz olmalı. |
| TC-05 | Tarihler | Tarihlerin ISO biçimini, Pazartesi olmasını ve sözlük aralığında bulunmasını doğrula. | Tüm tarihler `yyyy-mm-dd` olmalı; 2025-10-06–2026-09-28 aralığında Pazartesi olmalı. |
| TC-06 | Sayısal türler, sınırlar ve ilişkiler | Gösterim, tıklama ve dönüşüm alanlarını tam sayı olarak kontrol et; sınırları ve alanlar arası ilişkileri uygula. | `5000 <= gosterim <= 250000`, `1 <= tiklama <= gosterim`, `0 <= donusum <= tiklama` tüm satırlarda sağlanmalı. |
| TC-07 | Tutar biçimi ve tutarlılığı | Harcama/gelir metin biçimini, alt sınırları ve sıfır dönüşüm kuralını kontrol et. | Tutarlar tam iki ondalıkla yazılmalı; `harcama_tl > 0`, `gelir_tl >= 0`; dönüşüm sıfırsa gelir `0.00` olmalı. |
| TC-08 | İzinli kanal ve dağılım | Kanal değerlerini izinli kategorilerle ve kategori başına kayıt sayısıyla karşılaştır. | Yalnızca Google Ads, Meta Ads, TikTok Ads, E-posta ve SEO bulunmalı; her kanalda 52 kayıt olmalı. |
| TC-09 | Hafta-kanal çiftlerinin benzersizliği | Kayıtları tarih ve kanala göre grupla; çiftlerin yinelenmediğini ve beklenen tüm kombinasyonların bulunduğunu kontrol et. | Her hafta-kanal çifti tam bir kez bulunmalı; 260 benzersiz çift olmalı. |
| TC-10 | Boş hücreler | Başlık dışındaki tüm hücrelerin boş veya yalnızca boşluk olmadığını kontrol et. | CSV'de boş hücre bulunmamalı. |
| TC-11 | Tekrarlanabilirlik | Sabit tohumlu üretici fonksiyonunu iki kez bellekte çalıştır; oluşturulan baytları karşılaştır ve mevcut CSV ile eşitliğini doğrula. | İki üretim aynı olmalı ve mevcut CSV üretici çıktısıyla bayt düzeyinde eşleşmeli; kaynak CSV üzerine yazılmamalı. |
| TC-12 | Dosya kodlama ve satır sonları | Dosyayı UTF-8 olarak doğrula; BOM, ayraç ve satır sonlarını denetle. | UTF-8, BOM'suz, virgülle ayrılmış ve LF (`\n`) satır sonlu dosya olmalı. |
