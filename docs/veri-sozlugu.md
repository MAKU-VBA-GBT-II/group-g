# Veri Sözlüğü — Parametreli Kampanya Simülasyonu (Görev 2)

**Sürüm:** v1.0  
**Hazırlayan (DQ):** Tuana GÜRKAN  
**Tarih:** 2026-11-01  
**Hedef Dosya:** `data/kampanya-simulasyon-g2.csv`  
**İlgili Issue:** [#40 (G2-sem)](https://github.com/MAKU-VBA-GBT-II/group-g/issues/40)  

---

## 1. Veri Kümesi Özeti ve Kapsamı

Bu doküman, PrimeBee (Grup G) dijital pazarlama veri şirketi simülasyonunun Görev 2 mini ürünü için veri modelini, ayarlanabilir simülasyon parametrelerini ve analiz planını tanımlar.

- **Veri Türü:** Tamamen sentetik, matematiksel kurallara bağlı simülasyon verisi.
- **Kişisel Veri Kısıtı (KVKK/PII):** Veri kümesi hiçbir gerçek kişi, kurum veya kişisel kimlik bilgisi (isim, telefon, e-posta, T.C. kimlik no, IP vb.) **içermez ve içeremez**.
- **Hedeflenen Boyut:** Varsayılan parametrelerle ($5 \text{ kanal} \times 52 \text{ hafta}$) **260 satır** + 1 başlık satırı.
- **Dosya Biçimi:** CSV (UTF-8 kodlaması, virgül `,` ayracı, ondalık ayracı nokta `.`, satır sonu `\n`).

---

## 2. Şema ve Alan Tanımları

| Alan | Tip | Kural / Değer Aralığı | Birim | Örnek | Açıklama |
|---|---|---|---|---|---|
| `kampanya_id` | Metin (String) | `K` + 3 haneli sıra numarası (`K001` - `K260`), benzersiz (Primary Key) | — | `K001` | Kampanya kayıt kimliği |
| `tarih` | Tarih (Date) | `YYYY-MM-DD` biçiminde, haftanın Pazartesi günü (varsayılan: 2025-10-06 ile 2026-09-28 arası) | Tarih | `2025-10-06` | Kampanya performans haftasının başlangıç tarihi |
| `kanal` | Metin (Kategorik) | 5 sabit değerden biri: `Google Ads`, `Meta Ads`, `TikTok Ads`, `E-posta`, `SEO` | — | `Google Ads` | Pazarlama kanalı adı |
| `gosterim` | Tam Sayı (Integer) | $5.000 \le \text{gosterim} \le 250.000$ | Adet | `64520` | Reklamın kullanıcılara gösterilme adedi |
| `tiklama` | Tam Sayı (Integer) | $1 \le \text{tiklama} \le \text{gosterim}$ | Adet | `1850` | Reklama tıklanma adedi |
| `donusum` | Tam Sayı (Integer) | $0 \le \text{donusum} \le \text{tiklama}$ | Adet | `42` | Satın alma / hedef tamamlama adedi |
| `harcama_tl` | Ondalık (Float) | $\text{harcama\_tl} > 0.00$, CSV'de tam **2 ondalık basamak** (`f"{x:.2f}"`) | TL | `5550.00` | Kanal için harcanan bütçe |
| `gelir_tl` | Ondalık (Float) | $\text{gelir\_tl} \ge 0.00$, CSV'de tam **2 ondalık basamak**; `donusum == 0` ise zorunlu `0.00` | TL | `27300.00` | Kampanyadan elde edilen brüt ciro |

---

## 3. Simülasyon Parametreleri (BE Geliştiricisi İçin)

Simülasyon betiği (`src/simulasyon.py`), çalışma zamanında veya parametre olarak en az aşağıdaki ayarlanabilir değişkenleri alabilmelidir:

| Parametre Adı | Tip | Varsayılan Değer | İzin Verilen Aralık | Açıklama |
|---|---|---|---|---|
| `tohum` (seed) | `int` | `42` | $\ge 0$ | Tekrarlanabilir rastgele sayı üreteci tohum değeri. |
| `hafta_sayisi` | `int` | `52` | $1 - 104$ | Simülasyonun kaç hafta boyunca çalıştırılacağı (satır sayısını doğrudan belirler: $\text{satir} = \text{hafta\_sayisi} \times \text{kanal\_sayisi}$). |
| `kampanya_sayisi` | `int` | `5` | $1 - 5$ | Aktif simüle edilecek kanal adedi (varsayılan: 5 kanalın tamamı). |
| `baslangic_tarihi` | `str` | `2025-10-06` | `YYYY-MM-DD` (Pazartesi) | Simülasyonun başlayacağı takvim haftası Pazartesi tarihi. |

---

## 4. Kanal Performans Parametre Aralıkları

Her kanalın pazar dinamiklerini ve dönüşüm davranışını yansıtan metrik aralıkları şunlardır:

| Kanal | Haftalık Gösterim | CTR (Tıklama Oranı) | CVR (Dönüşüm Oranı) | CPC (TL / Tıklama) | Sepet Tutarı (TL / Dönüşüm) |
|---|---|---|---|---|---|
| **Google Ads** | 40.000 – 120.000 | 0,020 – 0,060 | 0,020 – 0,060 | 3,00 – 8,00 | 400 – 900 |
| **Meta Ads** | 60.000 – 180.000 | 0,010 – 0,030 | 0,010 – 0,040 | 2,00 – 5,00 | 300 – 700 |
| **TikTok Ads** | 80.000 – 250.000 | 0,005 – 0,020 | 0,005 – 0,025 | 1,50 – 4,00 | 250 – 600 |
| **E-posta** | 5.000 – 30.000 | 0,020 – 0,080 | 0,030 – 0,080 | 0,30 – 1,00 | 350 – 800 |
| **SEO** | 20.000 – 90.000 | 0,020 – 0,050 | 0,020 – 0,050 | 0,50 – 1,50 | 400 – 900 |

### Türetme Formülleri
Her simülasyon adımı için ilgili kanalın aralıklarından eşit olasılıklı rastgele değerler çekilir:
```python
tiklama = max(1, int(gosterim * ctr))
donusum = int(tiklama * cvr)
harcama_tl = round(tiklama * cpc, 2)
gelir_tl = round(donusum * sepet, 2) if donusum > 0 else 0.00
```

---

## 5. Analiz Planı: Zorunlu 5 Metrik Tanımı

Görev 2 kapsamında simülasyon verisi üzerinden hesaplanacak ve hem `docs/analiz-g2.md` raporunda hem de FE görselleştirme setinde kullanılacak 5 temel analitik metrik aşağıda tanımlanmıştır:

| No | Metrik Adı | Metrik Kategorisi | Matematiksel Formül | Birim | Neyi Ölçer? / Amacı |
|---|---|---|---|---|---|
| **M1** | **Toplam Harcama ve Toplam Gelir** | Toplam Metrik | $\text{Toplam Harcama} = \sum \text{harcama\_tl}$<br>$\text{Toplam Gelir} = \sum \text{gelir\_tl}$ | TL | Tüm kanallarda dönemsel kümülatif pazarlama bütçesi ve elde edilen brüt satış cirosu. Şirketin finansal hacmini gösterir. |
| **M2** | **Bileşik ROAS ve Ortalama Tıklama Başı Maliyet (CPC)** | Ortalama Metrik | $\text{Bileşik ROAS} = \frac{\sum \text{gelir\_tl}}{\sum \text{harcama\_tl}}$<br>$\text{Ortalama CPC} = \frac{\sum \text{harcama\_tl}}{\sum \text{tiklama}}$ | Oran / TL | Reklam yatırımlarının genel geri dönüş katsayısı (1 TL reklam harcamasının getirdiği ciro) ve ziyaretçi başına düşen ortalama maliyet. |
| **M3** | **Haftalık Gelir ve Harcama Trendi** | Zaman Serisi Kırılımı | Her hafta $t$ için:<br>$\text{Gelir}_t = \sum_{k \in \text{Kanal}} \text{gelir\_tl}_{t, k}$<br>$\text{Harcama}_t = \sum_{k \in \text{Kanal}} \text{harcama\_tl}_{t, k}$ | TL / Hafta | Pazarlama performansının 52 haftalık zaman serisi üzerindeki dalgalanmaları, büyüme trendi ve bütçe/ciro dengesinin zamansal değişimi. |
| **M4** | **Kanal Bazlı CTR ve ROAS Kırılımı** | Kategorik Kırılım | Her kanal $c$ için:<br>$\text{CTR}_c = \frac{\sum \text{tiklama}_c}{\sum \text{gosterim}_c} \times 100$<br>$\text{ROAS}_c = \frac{\sum \text{gelir\_tl}_c}{\sum \text{harcama\_tl}_c}$ | % / Oran | Kanalların kullanıcı etkileşim başarısı (tıklama oranı) ile sermaye verimliliğini (ROAS) çapraz karşılaştırır; bütçe tahsis kararlarına girdi sağlar. |
| **M5** | **En Yüksek ROAS Getiren Top-3 Kampanya Haftası** | Top-N Metrik | Her satır için $\text{ROAS}_i = \frac{\text{gelir\_tl}_i}{\text{harcama\_tl}_i}$ hesaplanıp azalan sırada sıralanır:<br>$\text{Top-3} = \operatorname{arg\,max}_{i=1,2,3}(\text{ROAS}_i)$ | Liste (Kanal, Tarih, ROAS) | Yıl boyunca en yüksek yatırım getirisi sağlayan 3 zirve kampanya kaydı. Yüksek verimlilik sağlayan dönem ve kanal dinamiklerini belirler. |

---

## 6. Veri Kalitesi (DQ) Doğrulama Kuralları

Simülasyon tamamlandığında veri setinin kabul edilebilmesi için aşağıdaki kuralların **tümünü** sağlaması zorunludur:

1. **Satır Sayısı:** Varsayılan parametrelerde başlık hariç tam **260 satır** olmalıdır ($\text{hafta\_sayisi} \times \text{kanal\_sayisi}$).
2. **Birincil Anahtar Benzersizliği:** `kampanya_id` sütunundaki tüm değerler tekil olmalı, formatı `K\d{3}` regex kuralına uymalıdır.
3. **Mantıksal Sıralama:** Hiçbir satırda $\text{tiklama} > \text{gosterim}$ veya $\text{donusum} > \text{tiklama}$ olamaz.
4. **Dönüşüm / Gelir Uyumu:** `donusum == 0` olan satırlarda `gelir_tl` mutlaka `0.00` olmalıdır.
5. **Pozitif Bütçe:** Sıfıra bölme hatasını önlemek için `harcama_tl > 0.00` kuralı tüm satırlarda geçerlidir.
6. **Hassasiyet:** `harcama_tl` ve `gelir_tl` tutarları CSV metninde daima tam 2 ondalık basamakla yazılmalıdır.
7. **Eksik Veri:** Veri kümesinde hiçbir hücrede `NULL`, `NaN` veya boş metin bulunamaz.
8. **Sentetiklik Onayı:** Veri setinde gerçek kişisel tanımlayıcı bilgi (PII) bulunamaz.
