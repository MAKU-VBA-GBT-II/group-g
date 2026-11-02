# Kullanım Kılavuzu (User Manual) — PrimeBee Mini Ürünü

**Ürün:** PrimeBee Dijital Pazarlama Simülasyonu ve Analitik Karar Destek Sistemi  
**Sürüm:** v1.0 (Görev 2)  
**Hazırlayan:** Tuana GÜRKAN (DQ)  
**Tarih:** 2026-11-02  
**İlgili Issue:** [#44 (G2-test)](https://github.com/MAKU-VBA-GBT-II/group-g/issues/44)  

---

## 1. Giriş ve Genel Bakış

PrimeBee Mini Ürünü; çok kanallı dijital pazarlama kampanyalarının performansını kontrollü, tekrarlanabilir ve sentetik olarak modelleyen, veri kalitesini denetleyen, 5 temel analitik metriği hesaplayan ve stratejik karar destek görselleri üreten entegre bir karar destek paketidir.

### Temel Bileşenler:
- **Simülasyon Motoru (`src/simulasyon.py`):** Parametrik veri üretim katmanı.
- **Kalite & Analiz Motoru (`src/analiz_g2.py`):** Şema doğrulama ve metrik hesaplama katmanı.
- **Görselleştirme Motoru (`src/grafik_uret.py`):** 3'lü analitik grafik üretim katmanı.
- **Raporlama Dokümanları (`docs/analiz-g2.md`, `docs/requirements.md`):** Analist ve yönetici çıktıları.

---

## 2. Sistem Gereksinimleri ve Kurulum

### Gereksinimler:
- Python 3.10 veya üzeri
- `pandas` (>= 1.5.0)
- `matplotlib` (>= 3.6.0)

### Bağımlılıkların Kurulumu:
Terminalden veya komut istemcisinden aşağıdaki komutla gerekli kütüphaneleri kurun:
```bash
pip install pandas matplotlib
```

---

## 3. Adım Adım Kullanım Rehberi

### Adım 1: Sentetik Kampanya Verisi Üretimi
Varsayılan parametrelerle ($52 \text{ hafta} \times 5 \text{ kanal} = 260 \text{ satır}$) veri üretmek için:
```bash
python src/simulasyon.py
```
Çıktı `data/kampanya-simulasyon-g2.csv` dosyasına yazılır ve otomatik şema doğrulamasından geçirilir.

#### İleri Düzey Parametre Seçenekleri (CLI):
Simülasyonu farklı senaryolar için özelleştirebilirsiniz:
| Parametre | Açıklama | Varsayılan | Örnek Kullanım |
|---|---|---|---|
| `--tohum` | Tekrarlanabilirlik tohumu (seed) | `42` | `python src/simulasyon.py --tohum 123` |
| `--hafta_sayisi` | Simüle edilecek hafta adedi (1-104) | `52` | `python src/simulasyon.py --hafta_sayisi 26` |
| `--kampanya_sayisi`| Aktif kanal adedi (1-5) | `5` | `python src/simulasyon.py --kampanya_sayisi 3` |
| `--baslangic_tarihi`| Başlangıç Pazartesi günü | `2025-10-06` | `python src/simulasyon.py --baslangic_tarihi 2026-01-05` |
| `--cikti` | Hedef CSV dosya yolu | `data/kampanya-simulasyon-g2.csv` | `python src/simulasyon.py --cikti data/ozel.csv` |

---

### Adım 2: Veri Kalitesi Doğrulama ve Analiz Raporu Üretimi
Üretilen verinin kalitesini denetlemek ve 5 analitik metriği hesaplayıp raporlamak için:
```bash
python src/analiz_g2.py
```
Bu komut:
1. CSV dosyasındaki tüm kayıtları şema kurallarına (`docs/veri-sozlugu.md`) göre denetler.
2. M1 (Hacim), M2 (Verimlilik/Bileşik ROAS & CPC), M3 (Zaman Trendi), M4 (Kanal Kırılımı) ve M5 (Top-3 Kampanya) metriklerini hesaplar.
3. Bulguları ve eylem önerisini `docs/analiz-g2.md` dosyasına otomatik olarak yazar.

---

### Adım 3: Görselleştirme Seti Üretimi
Analiz raporundaki metrikleri görselleştirmek için:
```bash
python src/grafik_uret.py
```
Bu komut `visuals/` klasörü altına 3 adet yüksek çözünürlüklü (200 DPI) grafik üretir:
- `visuals/gelir-harcama-trendi.png`: 52 haftalık gelir ve bütçe zaman serisi trendi (M3).
- `visuals/kanal-roas-ctr.png`: Kanal bazlı birleşik ROAS ve CTR karşılaştırması (M4).
- `visuals/roas-dagilimi.png`: Kampanya-hafta ROAS dağılım histogramı, medyan ve ortalama çizgileri (M5 ile ilişkili).

---

## 4. Çıktıların Yorumlanması

- **Bileşik ROAS ($\Sigma Gelir / \Sigma Harcama$):** 1 TL reklam bütçesinin kaç TL brüt hasılat getirdiğini ölçer. Portföy genelinde 5,57x seviyesindedir.
- **Kanal Verimliliği:** E-posta (45,50x) ve SEO (23,26x) yüksek getirili düşük maliyetli kanallardır. Google Ads (4,21x) ise en büyük ciro hacmini sağlayan ana kanaldır.
- **Top-3 Kampanyalar:** Zirve haftalık getiriler `docs/analiz-g2.md` tablosunda sıralanmıştır; en verimli kampanya 160,67x ile E-posta kanalına aittir.

---

## 5. Sorun Giderme (Troubleshooting)

| Hata Mesajı | Olası Neden | Çözüm |
|---|---|---|
| `ValueError: baslangic_tarihi bir Pazartesi olmalıdır` | Verilen tarih Pazartesi gününe denk gelmiyor. | Başlangıç tarihini bir Pazartesi günü olacak şekilde ayarlayın (`YYYY-MM-DD`). |
| `ValueError: hafta_sayisi 1 ile 104 arasında olmalıdır` | 1'den küçük veya 104'ten büyük hafta değeri girilmiş. | `--hafta_sayisi` değerini 1 ile 104 arasında belirtin. |
| `FileNotFoundError: data/kampanya-simulasyon-g2.csv` | Veri dosyası henüz üretilmemiş. | Önce `python src/simulasyon.py` komutunu çalıştırarak veriyi üretin. |
| `ValueError: CSV sütunları şemayla uyuşmuyor` | CSV üzerinde manuel değişiklik yapılmış veya başlıklar silinmiş. | `python src/simulasyon.py` komutunu çalıştırarak veriyi yeniden üretin. |
