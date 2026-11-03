# G2 — Parametreli Kampanya Simülasyonu Veri Kalitesi Test Senaryoları

- **Sürüm:** v2.0 (Görev 2)
- **Şema Referansı:** [`docs/veri-sozlugu.md`](../docs/veri-sozlugu.md)
- **Hedef Veri Dosyası:** `data/kampanya-simulasyon-g2.csv`
- **Hazırlayan (DQ):** Tuana GÜRKAN
- **Tarih:** 2026-11-02
- **İlgili Issue:** [#44 (G2-test)](https://github.com/MAKU-VBA-GBT-II/group-g/issues/44)

---

## 1. Genel Bilgilendirme ve Test Yaklaşımı

Bu doküman, PrimeBee (Grup G) dijital pazarlama veri şirketi mini ürününün veri güvenilirliğini, şema uyumunu ve simülasyon dinamiklerini doğrulamak amacıyla hazırlanmış bağımsız kabul senaryolarını içerir.

- **Hedef Boyut (Varsayılan):** Varsayılan simülasyon parametreleriyle ($5 \text{ kanal} \times 52 \text{ hafta}$) başlık hariç tam **260 veri satırı** hedeflenir.
- **Parametreli Simülasyon Kuralı:** Simülasyon betiği (`src/simulasyon.py`), çalışma zamanında parametre değişimlerine uygun olarak dinamik satır üretimi yapabilmeli ve sabit tohum (`tohum=42`) ile deterministik sonuç vermelidir.
- **Test Koşum İlkesi:** Testler veri üretildikten ve BE PR'ı açıldıktan sonra fiilen yürütülür; yürütülmeyen testlerin gerçekleşen sonuçları boş bırakılır ve durumları `Beklemede` olarak tutulur. Gerçek test yürütme sonuçları ve bulguları tarihleriyle birlikte `tests/test-log.md` günlüğüne işlenir.

---

## 2. Veri Kalitesi ve Parametre Kabul Senaryoları

| No | Senaryo | Adımlar | Girdi | Beklenen Sonuç | Gerçekleşen Sonuç | Durum |
|---:|---|---|---|---|---|---|
| **1** | **Dosya Varlığı ve Erişilebilirlik** | Depo kökünden `data/kampanya-simulasyon-g2.csv` dosya yolunu denetle; dosyanın mevcut olduğunu, UTF-8 biçiminde kodlandığını ve okunabilir olduğunu doğrula. | `data/kampanya-simulasyon-g2.csv` | Dosya mevcut olmalı, sıfır bayttan büyük olmalı ve UTF-8 kodlamasıyla hatasız okunabilmelidir. | | Beklemede — BE veri teslimi bekleniyor |
| **2** | **Varsayılan Boyut ve Satır Sayısı** | CSV dosyasını oku; başlık satırını hariç tutarak toplam veri kaydı adedini say. | Varsayılan parametrelerle üretilen veri (`tohum=42`, `hafta_sayisi=52`, `kampanya_sayisi=5`) | Tam olarak 260 veri satırı bulunmalıdır ($52 \times 5 = 260$). Eksik veya fazla satır bulunmamalıdır. | | Beklemede — BE veri teslimi bekleniyor |
| **3** | **Sütun Adları, Sırası ve Veri Tipleri** | CSV başlık satırını `docs/veri-sozlugu.md` ile karşılaştır. Her sütundaki değerlerin veri tipini (tam sayı, ondalık, metin, tarih) doğrula. | CSV başlığı ve veri satırları | Başlık tam olarak şu 8 sütunu bu sırayla içermelidir: `kampanya_id`, `tarih`, `kanal`, `gosterim`, `tiklama`, `donusum`, `harcama_tl`, `gelir_tl`. `gosterim`, `tiklama`, `donusum` tam sayı; `harcama_tl`, `gelir_tl` float; `tarih` ve `kampanya_id` string olmalıdır. Boş hücre (NaN/NULL) bulunmamalıdır. | | Beklemede — BE veri teslimi bekleniyor |
| **4** | **Değer Aralıkları, Mantıksal Kurallar ve Biçim** | 1) `kampanya_id` tekil ve `K\d{3}` biçiminde (`K001`–`K260`) mi?<br>2) `tarih` Pazartesi ve `2025-10-06` – `2026-09-28` aralığında mı?<br>3) $5.000 \le \text{gosterim} \le 250.000$ aralığında mı?<br>4) $1 \le \text{tiklama} \le \text{gosterim}$ ve $0 \le \text{donusum} \le \text{tiklama}$ mı?<br>5) $\text{harcama\_tl} > 0.00$ ve $\text{gelir\_tl} \ge 0.00$ mı?<br>6) $\text{donusum} == 0 \implies \text{gelir\_tl} == 0.00$ kuralı sağlanıyor mu?<br>7) Para tutarları tam 2 ondalık basamakla mı yazılmış? | 260 satırlık tüm simülasyon verisi | Tüm kayıtlarda mantıksal sıralama ve sınır kurallarına %100 uyulmalıdır. Kural ihlali sayısı 0 olmalıdır. Tutarlar tam iki ondalıklı basamak formatında olmalıdır. | | Beklemede — BE veri teslimi bekleniyor |
| **5** | **Kanal Kategori Değerleri ve Dağılım Eşitliği** | `kanal` sütunundaki benzersiz kategorileri çıkar; izin verilen 5 kategori ile karşılaştır. Her kategori için satır adedini say. | `kanal` sütunu değerleri | Yalnızca şu 5 kanal bulunmalıdır: `Google Ads`, `Meta Ads`, `TikTok Ads`, `E-posta`, `SEO`. Varsayılan ayarlarda 5 kanalın her biri için tam olarak 52'şer satır bulunmalıdır. | | Beklemede — BE veri teslimi bekleniyor |
| **6** | **Parametre Davranışı (Dinamik Satır Üretimi ve Kanal Seçimi)** | Simülasyon betiğini varsayılandan farklı parametrelerle çalıştırarak satır sayısının $\text{satir} = \text{hafta\_sayisi} \times \text{seçilen kanal sayısı}$ formülüne göre dinamik değiştiğini doğrula:<br>a) `hafta_sayisi=10`, `kampanya_sayisi=3`<br>b) `hafta_sayisi=26`, `kampanya_sayisi=5`<br>c) `hafta_sayisi=2`, `--kanallar "E-posta" SEO`<br>d) `hafta_sayisi=2`, `kampanya_sayisi=2`, `--kanallar "E-posta" SEO` | Farklı CLI parametre girdileri | a) 30, b) 130, c) ve d) 4 veri satırı üretilmelidir. c/d çıktılarında yalnızca `E-posta` ve `SEO` bulunmalı; seçilen kanal sırası korunmalıdır. Kanal sayısı ile `--kanallar` uzunluğu uyuşmuyorsa betik açıklayıcı hatayla durmalıdır. | | Beklemede — regresyon koşumu bekleniyor |
| **7** | **Sabit Tohum Determinizmi (Tekrarlanabilirlik)** | Simülasyon betiğini aynı tohum değeri (`tohum=42`) ile iki kez bağımsız olarak çalıştır ve üretilen CSV'lerin içerik hash'lerini karşılaştır. | `tohum=42` sabit parametresi | İki koşum sonucunda üretilen veri dosyaları bayt seviyesinde ve değer bazında birebir aynı olmalıdır (MD5/SHA256 eşleşmeli). | | Beklemede — BE simülasyon kodu teslimi bekleniyor |
| **8** | **Hata Yönetimi ve Parametre Doğrulama (Sınır Testi)** | Simülasyon betiğine geçersiz parametreler ver (örn. negatif tohum: `--tohum -5`, geçersiz hafta sayısı: `--hafta_sayisi 0`, Pazartesi olmayan tarih: `--baslangic_tarihi 2025-10-07`). | Hatalı/geçersiz parametre argümanları | Betik sessizce çökmemeli; anlamlı bir `ValueError` ve açıklayıcı hata mesajı fırlatarak çalışmayı durdurmalıdır. | | Beklemede — Hafta 6 hata yönetimi aşamasında yürütülecek |

---

## 3. Kabul Kriterleri Doğrulama ve Devir Protokolü

1. **BE PR İncelemesi (#44):** BE (@seyhannurienes-afk) simülasyon kodunu ve verisini içeren PR'ı açtığında, bu test senaryoları çerçevesinde PR'ın `Files changed` sekmesi üzerinden **en az 2 somut inceleme yorumu** yapılacak ve düzeltmeler tamamlandıktan sonra `Approve` verilecektir.
2. **Hafta 6 Tam Test Turu:** Veri `main` dalına merge edildikten sonra tüm senaryolar yerel olarak çalıştırılacak, gerçekleşen sonuçlar ve tarih `tests/test-log.md` dosyasına işlenecektir. Tespit edilen her kusur için `bug` etiketli Issue açılacaktır.
