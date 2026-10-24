# G1 — Kampanya Performans Analizi

**Veri:** `data/kampanya-performans.csv` · **Şema:** [`veri-sozlugu-g1.md`](veri-sozlugu-g1.md) v3
**Kapsam:** 5 kanal × 52 hafta = 260 kampanya-hafta kaydı, 2025-10-06–2026-09-28
**Yöntem:** Para toplamları `Decimal` ile hesaplanmıştır. Ortalama kampanya ROAS'ı, satır bazındaki gelir/harcama oranlarının aritmetik ortalamasıdır. Kanal ROAS'ı kanal toplam geliri / kanal toplam harcamasıdır. Veriler sentetiktir; gözlemler nedensellik kanıtlamaz.

## Metrikler

### 1. Toplam gelir

Toplam gelir **10.541.572,97 TL**'dir. 52 haftalık dönem için haftalık ortalama toplam gelir **202.722,56 TL**; toplam harcama **1.891.414,54 TL** ve birleşik ROAS (toplam gelir / toplam harcama) **5,57x** olarak hesaplanmıştır.

### 2. Ortalama kampanya-hafta ROAS

260 kampanya-hafta kaydındaki ROAS değerlerinin eşit ağırlıklı aritmetik ortalaması **17,43x**'tir. Bu ölçü, her kayda eşit ağırlık verir; toplam gelir/toplam harcama ile bulunan birleşik ROAS'tan (**5,57x**) farklı olması bu nedenle beklenebilir.

### 3. Kanala göre gelir

| Kanal | Toplam gelir (TL) | Toplam gelir payı |
|---|---:|---:|
| Google Ads | 4.365.311,40 | %41,41 |
| SEO | 2.147.542,59 | %20,37 |
| Meta Ads | 1.650.586,71 | %15,66 |
| E-posta | 1.549.173,49 | %14,70 |
| TikTok Ads | 828.958,78 | %7,86 |
| **Toplam** | **10.541.572,97** | **%100,00** |

Google Ads, **4.365.311,40 TL** ile en yüksek toplam geliri üretmiştir; TikTok Ads kanalının geliri en düşüktür. Gelir sıralaması tek başına verimliliği göstermez; ROAS ile birlikte değerlendirilmelidir.

### 4. Kanala göre birleşik ROAS

| Kanal | Toplam harcama (TL) | Toplam gelir (TL) | Birleşik ROAS |
|---|---:|---:|---:|
| E-posta | 34.050,15 | 1.549.173,49 | 45,50x |
| SEO | 92.331,52 | 2.147.542,59 | 23,26x |
| Google Ads | 1.037.415,58 | 4.365.311,40 | 4,21x |
| Meta Ads | 439.779,86 | 1.650.586,71 | 3,75x |
| TikTok Ads | 287.837,43 | 828.958,78 | 2,88x |

ROAS gelir ve harcamaya dayanır; kâr marjını veya diğer ek maliyetleri içermez.

### 5. ROAS'a göre ilk üç kanal

| Sıra | Kanal | Birleşik ROAS |
|---:|---|---:|
| 1 | E-posta | 45,50x |
| 2 | SEO | 23,26x |
| 3 | Google Ads | 4,21x |

### 6. Haftalık toplam gelir

Aşağıdaki tabloda her hafta için beş kanalın gelirleri toplanmıştır.

| Hafta başlangıcı | Toplam gelir (TL) |
|---|---:|
| 2025-10-06 | 112.673,13 |
| 2025-10-13 | 220.769,79 |
| 2025-10-20 | 161.433,11 |
| 2025-10-27 | 185.696,07 |
| 2025-11-03 | 285.281,90 |
| 2025-11-10 | 230.589,61 |
| 2025-11-17 | 185.725,28 |
| 2025-11-24 | 188.187,03 |
| 2025-12-01 | 240.438,61 |
| 2025-12-08 | 243.466,81 |
| 2025-12-15 | 197.941,35 |
| 2025-12-22 | 151.615,38 |
| 2025-12-29 | 130.788,97 |
| 2026-01-05 | 233.600,81 |
| 2026-01-12 | 236.694,84 |
| 2026-01-19 | 137.161,25 |
| 2026-01-26 | 196.308,66 |
| 2026-02-02 | 195.248,94 |
| 2026-02-09 | 263.454,40 |
| 2026-02-16 | 208.490,53 |
| 2026-02-23 | 343.949,46 |
| 2026-03-02 | 246.140,97 |
| 2026-03-09 | 85.872,10 |
| 2026-03-16 | 242.575,41 |
| 2026-03-23 | 304.260,54 |
| 2026-03-30 | 189.289,75 |
| 2026-04-06 | 232.990,08 |
| 2026-04-13 | 74.119,59 |
| 2026-04-20 | 212.284,59 |
| 2026-04-27 | 136.751,79 |
| 2026-05-04 | 220.513,11 |
| 2026-05-11 | 191.105,98 |
| 2026-05-18 | 321.375,19 |
| 2026-05-25 | 236.335,19 |
| 2026-06-01 | 204.006,03 |
| 2026-06-08 | 291.006,87 |
| 2026-06-15 | 201.052,83 |
| 2026-06-22 | 262.480,15 |
| 2026-06-29 | 261.127,64 |
| 2026-07-06 | 199.760,90 |
| 2026-07-13 | 271.853,67 |
| 2026-07-20 | 171.991,74 |
| 2026-07-27 | 190.557,64 |
| 2026-08-03 | 110.196,38 |
| 2026-08-10 | 189.719,25 |
| 2026-08-17 | 148.951,26 |
| 2026-08-24 | 195.807,71 |
| 2026-08-31 | 218.162,29 |
| 2026-09-07 | 122.014,55 |
| 2026-09-14 | 115.147,69 |
| 2026-09-21 | 264.427,88 |
| 2026-09-28 | 80.178,27 |

## Somut gözlemler

1. Google Ads, **4.365.311,40 TL** ile toplam gelirin **%41,41**'sini üretmiştir.
2. E-posta, **34.050,15 TL** harcamaya karşılık **1.549.173,49 TL** gelir ve en yüksek kanal birleşik ROAS'ı olan **45,50x** değerini üretmiştir.
3. TikTok Ads, **828.958,78 TL** ile en düşük toplam gelire; TikTok Ads ise **2,88x** ile en düşük kanal birleşik ROAS'ına sahiptir. Bu sentetik dönem tek başına bir kanalı durdurma gerekçesi değildir.

## Eylem önerisi

E-posta ve SEO için küçük ve süreli bir bütçe artışını kontrollü pilot olarak değerlendirin. Pilot boyunca haftalık harcama, gelir, ROAS ve dönüşümü izleyin; kâr marjı ve kapasiteyi de hesaba katmadan bütçeyi genişletmeyin.
