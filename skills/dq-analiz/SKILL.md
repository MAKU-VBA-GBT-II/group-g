---
name: dq-analiz
description: Doğrulanmış G2 parametreli kampanya simülasyonu CSV dosyasından 5 temel metriği hesaplayıp analiz raporunu ve bulguları hazırlarken kullan. DQ rolünün Görev 2 analitik değerlendirme görevi için kullanılır.
---

# dq-analiz: Görev 2 Metrik Hesabı ve Analitik Bulgular (DQ)

## Amaç
`data/kampanya-simulasyon-g2.csv` dosyasındaki 260 satırlık doğrulanmış simülasyon verisini okuyarak `docs/veri-sozlugu.md` şemasında tanımlanan 5 temel metriği (M1–M5) hesaplamak; bu metrikleri 1–2 cümlelik yorumlar, 3 somut veri gözlemi ve 1 uygulanabilir bütçe eylem önerisiyle birlikte `docs/analiz-g2.md` raporuna dönüştürmektir.

## Ne Zaman Kullanılır?
- BE simülasyon PR'ı birleştirildikten ve Issue #43'e `Veri hazır — commit <hash>` devir yorumu yazıldıktan sonra.
- Simülasyon parametreleri değiştirilerek yeni veri üretildiğinde analizi ve raporu yeniden üretmek gerektiğinde.
- FE görselleştirme sayılarıyla analiz raporu metriklerinin çapraz doğrulamasında.

## Kullanılan Dosyalar
| Dosya | Rol |
|---|---|
| `data/kampanya-simulasyon-g2.csv` | Girdi: 260 satır, 8 sütunluk doğrulanmış kampanya verisi |
| `docs/veri-sozlugu.md` | Şema, kurallar ve M1–M5 metrik tanımları |
| `src/analiz_g2.py` | Analizi yürüten ve raporu üreten Python betiği |
| `docs/analiz-g2.md` | Çıktı: 5 metrik, yorumlar, 3 gözlem ve 1 eylem önerisi içeren analiz dokümanı |
| `docs/requirements.md` | Ürünün amacı, yaptıkları ve yapmadıkları (1 sayfa) |
| `visuals/` | FE tarafından üretilen 3 grafikle tutarlılık kontrolü |

## Metrik Tanımları ve Formülleri
1. **M1 — Toplam Harcama ve Gelir:** $\sum \text{harcama\_tl}$ ve $\sum \text{gelir\_tl}$ (TL cinsinden, 2 ondalıklı).
2. **M2 — Bileşik ROAS ve Ortalama CPC:** $\frac{\sum \text{gelir\_tl}}{\sum \text{harcama\_tl}}$ (oran, x) ve $\frac{\sum \text{harcama\_tl}}{\sum \text{tiklama}}$ (TL/tıklama).
3. **M3 — Haftalık Trend:** 52 haftalık zaman serisinde haftalık toplam gelir ve harcama seyri.
4. **M4 — Kanal Kırılımı:** 5 kanal için kanal bazında birleşik ROAS ($\frac{\sum \text{gelir}}{\sum \text{harcama}}$) ve CTR ($\frac{\sum \text{tiklama}}{\sum \text{gosterim}} \times 100$).
5. **M5 — Top-3 Zirve Kampanya:** Satır bazında $\frac{\text{gelir\_tl}}{\text{harcama\_tl}}$ oranına göre en yüksek getiri sağlayan 3 kayıt.

## Çıktı Format Kuralları
- **Veri Commit Bilgisi:** Raporun en üstünde kullanılan veri dosyasının commit hash'i yer almalıdır (`47cf641d611512a5ed84b36a1620e13af61c753b`).
- **Para Formatı:** Tutarlar Türkçe formatta yazılır: binlik ayracı nokta, ondalık ayracı virgül (`1.891.414,54 TL`).
- **Oran ve Sayılar:** ROAS iki ondalıklı çarpan olarak (`5,57x`), CTR yüzde olarak (`%2,42`) ifade edilir.
- **Bulgular Bölümü:** Mutlaka **3 adet somut gözlem** ve **1 adet uygulanabilir eylem önerisi** içermelidir.
- **Sentetiklik Notu:** Verilerin sentetik simülasyon ürünü olduğu ve KVKK/PII içermediği açıkça belirtilmelidir.

## Çalıştırma Komutu
Depo kökünden şu komut çalıştırılır:
```bash
python src/analiz_g2.py
```
Betik veri doğrulaması yapar, metrikleri hesaplar ve `docs/analiz-g2.md` dosyasını otomatik olarak oluşturur/günceller.

## Örnek Girdi ve Çıktı
### Örnek Girdi (`data/kampanya-simulasyon-g2.csv` satırı):
```csv
kampanya_id,tarih,kanal,gosterim,tiklama,donusum,harcama_tl,gelir_tl
K079,2026-01-19,E-posta,6088,198,38,119.27,19162.72
```

### Örnek Çıktı (`docs/analiz-g2.md` M5 kesiti):
```markdown
| Sıra | Kampanya ID | Tarih (Hafta) | Kanal | Harcama | Gelir | ROAS |
|---|---|---|---|---|---|---|
| 1 | `K079` | 2026-01-19 | **E-posta** | 119,27 TL | 19.162,72 TL | **160.67x** |
```

## Reddetme Durumları
1. **Gerçek Kişisel Veri Talebi:** İstekte veya girdi verisinde gerçek kişi adı, e-posta, telefon, T.C. kimlik numarası, kredi kartı veya IP adresi gibi KVKK/GDPR kapsamında tanımlayıcı veri bulunması durumunda işlem derhal reddedilir.
2. **Eksik / Doğrulanmamış Veri:** Veri dosyası 260 satırdan az veya fazlaysa, sütun adları uyuşmuyorsa veya `harcama_tl <= 0` hataları varsa analiz yapılmaz.
3. **BE Devir Yorumu Yoksa:** BE rolü ilgili Issue'ya `Veri hazır` devir yorumu yazmadan analize başlanmaz.
