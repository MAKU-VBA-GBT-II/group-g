# Veri Sözlüğü — Çok Ajanlı Şirket Programı Kampanya Simülasyonu

**Sürüm:** v2.0 (Duyuru 10 — Çok Ajanlı Şirket Programı)  
**Hazırlayan:** PrimeBee (Grup G)  
**Tarih:** 2026-11-21  
**Hedef Dosya:** `data/kampanya-simulasyon-g3.csv`  
**İlgili Duyuru:** [Duyuru 10 (2026-11-20)](https://github.com/MAKU-VBA-GBT-II/ders/blob/main/Duyuru-10_2026-11-20.md)  

---

## 1. Veri Kümesi Özeti ve Kapsamı

Bu doküman, PrimeBee (Grup G) dijital pazarlama şirketinin geliştirdiği ACP tabanlı çok ajanlı şirket programı için simülasyon veri modelini, dış piyasa (web) eşleme alanlarını, dinamik parametreleri ve veri kurallarını tanımlar.

* **Veri Türü:** Sentetik şirket verisi + dış web kaynaklarıyla (Meta Ad Library & Google Trends) eşleşen pazar alanları.
* **Kişisel Veri Kısıtı (KVKK/GDPR):** Veri kümesi hiçbir gerçek kişi, kurum veya kişisel kimlik bilgisi (isim, telefon, e-posta, T.C. kimlik no, profil bilgisi vb.) **içermez ve içeremez**.
* **Hedeflenen Boyut:** Varsayılan parametrelerle ($5 \text{ kanal} \times 52 \text{ hafta}$) **260 satır** + 1 başlık satırı.
* **Dosya Biçimi:** CSV (UTF-8 kodlaması, virgül `,` ayracı, ondalık ayracı nokta `.`, satır sonu `\n`).

---

## 2. Şema ve Alan Tanımları

| Alan | Tip | Kural / Değer Aralığı | Birim | Örnek | Açıklama |
|---|---|---|---|---|---|
| `kampanya_id` | Metin (String) | `K` + 3 haneli sıra numarası (`K001` - `K260`), benzersiz (Primary Key) | — | `K001` | Kampanya kayıt kimliği |
| `tarih` | Tarih (Date) | `YYYY-MM-DD` biçiminde, haftanın Pazartesi günü | Tarih | `2025-10-06` | Kampanya performans haftasının başlangıç tarihi |
| `kanal` | Metin (Kategorik) | 5 sabit değerden biri: `Google Ads`, `Meta Ads`, `TikTok Ads`, `E-posta`, `SEO` | — | `Google Ads` | Pazarlama kanalı adı |
| `kategori` | Metin (Kategorik) | Web reklam kütüphanesiyle eşleşen sektör/kategori: `Moda`, `Elektronik`, `Kozmetik`, `Ev-Yasam`, `Spor` (dışarıdan genişletilebilir) | — | `Moda` | Reklamı yapılan ürün/hizmet kategorisi |
| `hedef_bolge` | Metin (Kategorik) | Coğrafi pazar bölgesi: `TR-Marmara`, `TR-Ege`, `TR-Ic-Anadolu`, `TR-Akdeniz`, `TR-Genel` | — | `TR-Marmara` | Hedeflenen coğrafi pazar |
| `trend_kelime` | Metin (String) | Google Trends'ten toplanan yükselen arama anahtar kelimesi: `indirim`, `yeni-sezon`, `kampanya`, `firsat`, `trend-urun` | — | `yeni-sezon` | Reklam metni üretiminde temel alınan trend terimi |
| `gosterim` | Tam Sayı (Integer) | $5.000 \le \text{gosterim} \le 250.000$ | Adet | `64520` | Reklamın kullanıcılara gösterilme adedi |
| `tiklama` | Tam Sayı (Integer) | $1 \le \text{tiklama} \le \text{gosterim}$ | Adet | `1850` | Reklama tıklanma adedi |
| `donusum` | Tam Sayı (Integer) | $0 \le \text{donusum} \le \text{tiklama}$ | Adet | `42` | Satın alma / hedef tamamlama adedi |
| `harcama_tl` | Ondalık (Float) | $\text{harcama\_tl} > 0.00$, CSV'de tam **2 ondalık basamak** | TL | `5550.00` | Kanal için harcanan bütçe |
| `gelir_tl` | Ondalık (Float) | $\text{gelir\_tl} \ge 0.00$, CSV'de tam **2 ondalık basamak**; `donusum == 0` ise zorunlu `0.00` | TL | `27300.00` | Kampanyadan elde edilen brüt ciro |
| `rakip_cpa_tl` | Ondalık (Float) | Açık pazar referans edinme maliyeti ($35.00 - 110.00$), tam 2 ondalık basamak | TL | `62.50` | Rakiplerin sektördeki ortalama müşteri edinme maliyeti |
| `simule_cpa_tl` | Ondalık (Float) | Kampanyanın fiili edinme maliyeti ($\text{harcama\_tl} / \text{donusum}$), tam 2 ondalık basamak | TL | `71.20` | Ajan 3'ün denetleyeceği simüle edilen CPA değeri |

---

## 3. Dinamik Simülasyon Parametreleri (CLI Arayüzü)

Simülasyon betiği (`src/simulasyon.py`), Duyuru 10 gereksinimleri uyarınca dışarıdan liste ve sayısal aralık alabilmektedir:

| Parametre Adı | Tip | Varsayılan Değer | İzin Verilen Aralık / Örnek | Açıklama |
|---|---|---|---|---|
| `--tohum` | `int` | `42` | $\ge 0$ | Tekrarlanabilir rastgele sayı üreteci tohum değeri. |
| `--hafta_sayisi` | `int` | `52` | $1 - 104$ | Simülasyonun kaç hafta boyunca çalıştırılacağı. |
| `--kanallar` | `list[str]` | 5 kanalın tamamı | Örn: `--kanallar Google Ads Meta Ads` | Seçilen pazarlama kanalları listesi. |
| `--kategoriler` | `list[str]` | 5 ana kategori | Örn: `--kategoriler Moda Kozmetik` | Dışarıdan belirlenebilen hedef ürün/sektör listesi. |
| `--bolgeler` | `list[str]` | 5 bölge | Örn: `--bolgeler TR-Marmara TR-Ege` | Dışarıdan belirlenebilen coğrafi bölge listesi. |
| `--butce_araligi` | `float float` | Kanal sınırları | Örn: `--butce_araligi 1000 15000` | Simülasyon için asgari ve azami harcama aralığı. |
| `--hedef_cpa_max` | `float` | Sınırsız | Örn: `--hedef_cpa_max 90.00` | Ajan 3 için kabul edilebilir üst CPA eşiği (TL). |
| `--baslangic_tarihi` | `str` | `2025-10-06` | `YYYY-MM-DD` (Pazartesi) | Simülasyon başlangıç haftası tarihi. |
| `--cikti` | `Path` | `data/kampanya-simulasyon-g3.csv` | `.csv` dosya yolu | Çıktı dosyasının kaydedileceği konum. |
