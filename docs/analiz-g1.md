# G1 — Kampanya Performans Analizi

**Veri:** `data/kampanya-performans.csv` · **Şema:** [`veri-sozlugu-g1.md`](veri-sozlugu-g1.md) v2
**Kapsam:** 5 kanal × 52 hafta = 260 kampanya-hafta kaydı, 2025-10-06–2026-09-28
**Teslim:** Özge Nur Doğu'nun G1-Analiz Issue'sundaki v2 veri hazır yorumu ve `4617f2a` commit'i doğrulandı.
**Yöntem:** Para toplamlarında ondalık hassasiyet kullanıldı. Kanal ROAS'ı `kanal geliri / kanal harcaması`; ortalama kampanya ROAS'ı ise 260 satırdaki `gelir / harcama` oranlarının aritmetik ortalamasıdır. Birleşik ROAS ayrıca toplam gelir / toplam harcama olarak verilir. Veriler sentetiktir; gözlemler nedensellik kanıtlamaz.

## Metrikler

### 1. Toplam gelir

**10.541.572,97 TL**, tek haftanın veya tek kampanyanın değil, 5 kanalın 52 haftalık dönem boyunca elde ettiği toplam gelirdir. Haftalık ortalama toplam gelir **202.722,56 TL**'dir; aynı dönem için toplam harcama **1.891.414,54 TL**, birleşik ROAS (toplam gelir / toplam harcama) ise **5,57x** olarak hesaplanmıştır.

### 2. Ortalama kampanya-hafta ROAS

260 satırdaki ROAS değerlerinin eşit ağırlıklı aritmetik ortalaması **17,43x**'tir. Bu değer, yüksek ve düşük harcama tutarlı satırlara eşit ağırlık verir; bu nedenle toplam gelir/toplam harcama ile hesaplanan birleşik ROAS'tan (5,57x) belirgin biçimde yüksektir.

### 3. Kanala göre gelir

| Kanal | Toplam gelir (TL) | Toplam gelir payı |
|---|---:|---:|
| Google Ads | 4.365.311,40 | %41,41 |
| SEO | 2.147.542,59 | %20,37 |
| Meta Ads | 1.650.586,71 | %15,66 |
| E-posta | 1.549.173,49 | %14,70 |
| TikTok Ads | 828.958,78 | %7,86 |
| **Toplam** | **10.541.572,97** | **%100,00** |

Google Ads en yüksek toplam geliri üretmiştir; TikTok Ads'in toplam geliri beş kanal içinde en düşüktür. Gelir sıralaması tek başına verimliliği göstermez, bu nedenle ROAS ile birlikte değerlendirilmelidir.

### 4. Kanala göre birleşik ROAS

| Kanal | Toplam harcama (TL) | Toplam gelir (TL) | Birleşik ROAS |
|---|---:|---:|---:|
| E-posta | 34.050,15 | 1.549.173,49 | 45,50x |
| SEO | 92.331,52 | 2.147.542,59 | 23,26x |
| Google Ads | 1.037.415,58 | 4.365.311,40 | 4,21x |
| Meta Ads | 439.779,86 | 1.650.586,71 | 3,75x |
| TikTok Ads | 287.837,43 | 828.958,78 | 2,88x |

E-posta ve SEO, harcama başına gelir bakımından diğer kanallardan yüksek görünmektedir. ROAS gelir ve harcamaya dayalıdır; kâr marjı veya ek maliyetleri içermez.

### 5. ROAS'a göre ilk üç kanal

| Sıra | Kanal | Birleşik ROAS |
|---:|---|---:|
| 1 | E-posta | 45,50x |
| 2 | SEO | 23,26x |
| 3 | Google Ads | 4,21x |

İlk iki kanal olan E-posta ve SEO, bu veride kanal bazında en yüksek birleşik ROAS'a sahiptir. Bu sıralama geçmiş sentetik kayıtların özetidir; bütçe değişikliğinin gelecekte aynı sonucu vereceğini garanti etmez.

## Somut gözlemler

1. Google Ads **4.365.311,40 TL** ile gelirin **%41,41**'ini üretmiş; aynı zamanda **1.037.415,58 TL** ile en yüksek kanal harcamasına sahip olmuştur.
2. E-posta **34.050,15 TL** harcamayla **1.549.173,49 TL** gelir ve **45,50x** birleşik ROAS üretmiştir; beş kanalın en yüksek ROAS'ıdır.
3. TikTok Ads'in birleşik ROAS'ı **2,88x** ile en düşük, geliri **828.958,78 TL** ile en azdır; buna rağmen gelir/harcama oranı pozitiftir ve tek başına kanalı durdurma gerekçesi değildir.

## Eylem önerisi

Önce E-posta ve SEO için küçük, süreli bir bütçe artışını kontrollü pilot olarak test edin; Google Ads hacmini koruyun ve TikTok Ads için kanal hedeflemesi/yaratıcılarını gözden geçirin. Pilot boyunca haftalık harcama, gelir, ROAS ve dönüşümü izleyip marj ve kapasiteyi de hesaba katmadan bütçeyi genişletmeyin.
