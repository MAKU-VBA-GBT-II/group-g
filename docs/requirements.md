# Gereksinim Dokümanı — PrimeBee Mini Ürünü

**Ürün:** PrimeBee Dijital Pazarlama Simülasyonu ve Analitik Karar Destek Sistemi  
**Sürüm:** v1.0 (Görev 2)  
**Tarih:** 2026-11-02  
**Hazırlayan:** Tuana GÜRKAN (DQ)  
**İlgili Issue:** [#43 (G2-analiz)](https://github.com/MAKU-VBA-GBT-II/group-g/issues/43)  

---

## 1. Ürünün Amacı

PrimeBee Mini Ürünü, e-ticaret ve dijital pazarlama şirketlerinin çok kanallı (Omni-channel) pazarlama harcamalarını simüle eden, veri kalitesini güvence altına alan ve analitik metrikler üzerinden stratejik bütçe tahsis kararları sunan hafif siklet (lightweight) bir karar destek sistemidir. 

Ürün, gerçek pazarlama risklerini sıfıra indirerek kontrollü ve sentetik bir ortamda kampanya performans dinamiklerini modellemeyi ve yöneticilere eyleme geçirilebilir içgörüler sunmayı amaçlar.

---

## 2. Ürünün Yaptıkları (Kapsam İçi / Fonksiyonel Nitelikler)

1. **Sentetik Veri Üretimi:** 5 ana dijital pazarlama kanalında (`Google Ads`, `Meta Ads`, `TikTok Ads`, `E-posta`, `SEO`) haftalık bazda bütçe, gösterim, tıklama, dönüşüm ve ciro verilerini deterministik matematiksel formüllerle üretir.
2. **Parametrik Yapı:** Simülasyon çalışma parametrelerini (`tohum`, `hafta_sayisi`, `kampanya_sayisi`, `baslangic_tarihi`) esnek şekilde alabilir; farklı senaryo ve boyutlarda veri üretebilir.
3. **Çift Aşamalı Veri Kalitesi (DQ) Doğrulaması:** Üretilen veriyi sıkı şema kurallarına (`docs/veri-sozlugu.md`), mantıksal hiyerarşilere ($\text{donusum} \le \text{tiklama} \le \text{gosterim}$) ve iki ondalıklı para formatına göre otomatik denetler.
4. **Metrik Hesaplama ve Analitik Motor:** Şemada tanımlanan 5 temel metrik setini (M1: Toplam Hasılat/Harcama, M2: Bileşik ROAS ve Ortalama CPC, M3: Haftalık Trend, M4: Kanal CTR ve ROAS Kırılımı, M5: Top-3 Verimli Kampanya) eksiksiz hesaplar.
5. **Standardize Görselleştirme:** Analitik çıktıları 3 temel grafik formatında (`visuals/gelir-harcama-trendi.png`, `visuals/kanal-roas-ctr.png`, `visuals/roas-dagilimi.png`) yüksek çözünürlüklü (200 DPI) PNG olarak görselleştirir.
6. **Karar Destek Raporlaması:** Analiz bulgularını 3 somut veri gözlemi ve 1 uygulanabilir bütçe optimizasyon eylemi ile yöneticilere raporlar (`docs/analiz-g2.md`).
7. **Otomasyon ve Yeniden Üretilebilirlik:** Depo kökünden tek bir komutla (`python src/analiz_g2.py` ve `python src/grafik_uret.py`) tüm analiz ve görsellerin sıfırdan yeniden üretilmesini sağlar.

---

## 3. Ürünün Yapmadıkları (Kapsam Dışı / Sınırlar)

- **Gerçek Kişisel Veri İşlemez:** Gerçek müşteri kimlikleri, IP adresleri, e-posta adresleri, telefon numaraları veya KVKK kapsamındaki kişisel tanımlayıcı bilgileri (PII) depolamaz ve işlemez.
- **Canlı Reklam Platformlarına Bağlanmaz:** Google Ads API, Meta Graph API veya TikTok Marketing API gibi üçüncü taraf canlı reklam platformlarına API entegrasyonu sağlamaz; canlı kampanya başlatmaz veya durdurmaz.
- **Finansal Ödeme ve Bütçe Transferi Gerçekleştirmez:** Banka veya sanal POS altyapılarıyla etkileşime girmez, doğrudan para transferi ya da kredi kartı harcaması yapmaz.
- **Kullanıcı Yönetimi ve Yetkilendirme (Auth/RBAC) Barındırmaz:** Giriş ekranı, kullanıcı rolleri, şifreleme veya çoklu kullanıcı oturum altyapısı içermez; yerel analist odaklı çalışır.
- **Makine Öğrenmesi (Predictive AI) Tahmini Yapmaz:** Derin öğrenme ya da regresyon tabanlı gelecek tahmini üretmez; sentetik parametreli modelleme ve tanımlayıcı (deskriptif) analiz sunar.
- **Gerçek Zamanlı Veri Tabanı (RDBMS) Yönetmez:** Ağ üzerinden çalışan ilişkisel veri tabanı sunucusu gerektirmez; dosya tabanlı (CSV/Markdown) girdi ve çıktılarla çalışır.
