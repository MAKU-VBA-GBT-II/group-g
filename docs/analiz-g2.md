# Görev 2 — Dijital Pazarlama Kampanya Analiz Raporu (PrimeBee)

**Veri Kaynağı:** `data/kampanya-simulasyon-g2.csv`  
**Veri Commit'i:** `47cf641d611512a5ed84b36a1620e13af61c753b`  
**Hazırlayan (DQ):** Tuana GÜRKAN  
**Tarih:** 2026-11-02  
**İlgili Issue:** [#43 (G2-analiz)](https://github.com/MAKU-VBA-GBT-II/group-g/issues/43)  

> **Not:** Bu rapordaki veriler tamamen sentetik simülasyon ürünüdür (`tohum=42`, 260 satır). Gerçek kişi veya kurumsal kimlik bilgisi (KVKK/PII) içermez.

---

## 1. Zorunlu 5 Temel Metrik ve Değerlendirme

### M1 — Toplam Harcama ve Toplam Gelir
- **Toplam Harcama:** 1.891.414,54 TL
- **Toplam Gelir:** 10.541.572,97 TL
- **Net Katma Değer (Gelir - Harcama):** 8.650.158,43 TL

**Yorum:** 52 haftalık dönemde PrimeBee genelinde 1,89 milyon TL pazarlama bütçesi harcanmış ve karşılığında 10,54 milyon TL brüt satış hasılatı elde edilmiştir. Toplam kampanya operasyonu net 8,65 milyon TL finansal katma değer yaratarak yüksek bir nakit akışı sağlamıştır.

### M2 — Bileşik ROAS ve Ortalama Tıklama Başı Maliyet (CPC)
- **Bileşik ROAS (Σ Gelir / Σ Harcama):** 5.57x
- **Ortalama CPC (Σ Harcama / Σ Tıklama):** 3,39 TL
- **Genel Ortalama CTR:** %2.42

**Yorum:** Portföy genelinde yatırılan her 1,00 TL reklam bütçesi ortalama **5,57 TL** ciro olarak geri dönmüştür. Ortalama tıklama başı maliyetin 3,39 TL seviyesinde dengelenmesi, organik ve düşük maliyetli kanalların genel maliyet tabanını optimize ettiğini göstermektedir.

### M3 — Haftalık Gelir ve Harcama Trendi (Zaman Serisi)
- **İncelenen Hafta Sayısı:** 52 hafta (2025-10-06 – 2026-09-28)
- **Haftalık Ortalama Harcama:** 36.373,36 TL
- **Haftalık Ortalama Gelir:** 202.722,56 TL
- **Görsel Referansı:** `visuals/gelir-harcama-trendi.png`

**Yorum:** 52 hafta boyunca haftalık harcama bandı 30.000 TL – 45.000 TL aralığında istikrarlı seyrederken, haftalık gelir 150.000 TL ile 260.000 TL arasında dalgalanma sergilemiştir. Hiçbir haftada operasyonel zarar yaşanmamış; dönemsel talep artışları gelire doğrudan pozitif yansımıştır.

### M4 — Kanal Bazlı CTR ve ROAS Kırılımı (Kategorik Kırılım)

| Kanal | Toplam Harcama | Toplam Gelir | Gelir Payı (%) | Bileşik ROAS | Ortalama CTR | Ortalama CPC |
|---|---|---|---|---|---|---|
| **E-posta** | 34.050,15 TL | 1.549.173,49 TL | %14.70 | **45.50x** | %5.02 | 0,69 TL |
| **SEO** | 92.331,52 TL | 2.147.542,59 TL | %20.37 | **23.26x** | %3.62 | 0,98 TL |
| **Google Ads** | 1.037.415,58 TL | 4.365.311,40 TL | %41.41 | **4.21x** | %4.18 | 5,98 TL |
| **Meta Ads** | 439.779,86 TL | 1.650.586,71 TL | %15.66 | **3.75x** | %1.98 | 3,37 TL |
| **TikTok Ads** | 287.837,43 TL | 828.958,78 TL | %7.86 | **2.88x** | %1.27 | 2,59 TL |

**Görsel Referansı:** `visuals/kanal-roas-ctr.png`

**Yorum:** E-posta (45,50x) ve SEO (23,26x) kanalları son derece düşük harcama maliyetleriyle olağanüstü kârlılık üretirken, toplam cironun %41,41'ini sırtlayan Google Ads (4,21x) ölçek büyüklüğü sağlamıştır. TikTok Ads (2,88x) ve Meta Ads (3,75x) ise nispeten düşük ROAS seviyeleriyle dönüşümden ziyade üst huni (farkındalık) işlevi görmüştür.

### M5 — En Yüksek ROAS Getiren Top-3 Kampanya Haftası (Top-N)

| Sıra | Kampanya ID | Tarih (Hafta) | Kanal | Harcama | Gelir | ROAS |
|---|---|---|---|---|---|---|
| 1 | `K079` | 2026-01-19 | **E-posta** | 119,27 TL | 19.162,72 TL | **160.67x** |
| 2 | `K049` | 2025-12-08 | **E-posta** | 424,15 TL | 58.676,29 TL | **138.34x** |
| 3 | `K164` | 2026-05-18 | **E-posta** | 257,18 TL | 33.880,39 TL | **131.74x** |

**Görsel Referansı:** `visuals/roas-dagilimi.png` (Histogram genelinde medyan 5,26x, ortalama 17,43x)

**Yorum:** Tüm veri kümesindeki 260 kampanya-hafta kaydı incelendiğinde, zirvedeki 3 kaydın tamamı **E-posta** kanalından çıkmıştır. 2026-01-19 haftasındaki `K079` kampanyası yalnızca 119,27 TL harcama ile 19.162,72 TL ciro yaratarak 160,67x ile yılın rekor verimliliğine ulaşmıştır.

---

## 2. Bulgular: 3 Gözlem ve 1 Eylem Önerisi

### Somut Gözlemler:
1. **Kanal Kutuplaşması (Asimetrik Verimlilik):** Bütçenin yalnızca %6,68'ini kullanan E-posta ve SEO kanalları, toplam cironun %35,07'sini üretmektedir. Buna karşın bütçenin %54,85'ini tüketen Google Ads kanalının ROAS'ı 4,21x düzeyinde kalmaktadır.
2. **Ücretli Sosyal Medya Huni Kaybı:** TikTok Ads (%1,27 CTR, 2,88x ROAS) ve Meta Ads (%1,98 CTR, 3,75x ROAS), portföy ortalaması olan 5,57x bileşik ROAS'ın belirgin şekilde altında kalarak birim bütçe başına en pahalı dönüşümü üretmektedir.
3. **E-posta Kanalının Yüksek Çarpanı:** E-posta kanalı %5,02 CTR ve 0,69 TL CPC ile en düşük edinim maliyetine sahip olup, ortalama sepet tutarı yüksek sadık kitle segmentlerini yakalayarak 45,50x bileşik getiri sağlamıştır.

### Eylem Önerisi (Aksiyon Planı):
> **Bütçe Yeniden Tahsisi ve Otomasyon:** TikTok Ads'e ayrılan haftalık bütçenin %30'luk kısmı kesilmeli; bu bütçe E-posta otomasyon altyapısına (yeniden hedefleme ve terk edilmiş sepet akışları) ve SEO teknik içerik yatırımlarına kaydırılmalıdır. Böylece genel portföy bileşik ROAS'ının 5,57x seviyesinden 6,80x seviyesine yükseltilmesi hedeflenmelidir.

---

## 3. Veri Kalitesi ve Tutarlılık Kontrol Listesi
- [x] Toplam satır sayısı: 260 (52 hafta x 5 kanal)
- [x] `tarih` aralığı: 2025-10-06 ile 2026-09-28 arası (52 ardışık Pazartesi)
- [x] Bütçe kontrolü: Sıfır veya negatif harcama bulunmamaktadır.
- [x] Dönüşüm / Gelir tutarlılığı: `donusum == 0` olan satırlarda gelir sıfırdır.
- [x] FE grafik değerleriyle tutarlılık: `visuals/` setindeki sayılar bu rapordaki sayılarla tam eşleşmektedir.
