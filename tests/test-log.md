# G1 Kampanya Performans Veri Kalitesi Test Sonuç Günlüğü (test-log.md)

**Şirket:** PrimeBee - Grup G (Dijital Pazarlama)  
**Test Edilen Dosya:** `data/kampanya-performans.csv`  
**Referans:** `tests/test-cases.md`, `docs/veri-sozlugu-g1.md`  
**Sorumlular:** Nuri Enes Seyhan (DQ), Ceren Doğrul (Junior)  

---

## Test Koşum Kayıtları

| No | Senaryo | Test Tarihi | Test Eden | Beklenen Sonuç | Gerçekleşen Sonuç | Durum (Geçti / Kaldı) | İlgili Issue / Not |
|---:|---|---|---|---|---|---|---|
| 5 | Kanal kategori değerleri ve dağılımı | 2026-10-23 | Ceren Doğrul | Yalnızca izin verilen 5 kanal bulunmalı; her kanalda 52 kayıt olmalı. | 5 kanal bulundu: Google Ads (52), Meta Ads (52), TikTok Ads (52), E-posta (52), SEO (52). Beklenmeyen/eksik kanal yok; 260 kayıt kontrol edildi. | Geçti | #21 |

## Hafta 4 Tam Test Koşumu — 2026-10-24

Beş senaryo, `data/kampanya-performans.csv` dosyasının mevcut sürümünde tek tek çalıştırıldı.

| No | Senaryo | Test Tarihi | Test Eden | Beklenen Sonuç | Gerçekleşen Sonuç | Durum |
|---:|---|---|---|---|---|---|
| 1 | Dosya var mı? | 2026-10-24 | Nuri Enes Seyhan (DQ) | Dosya mevcut ve okunabilir olmalı. | `data/kampanya-performans.csv` mevcut; UTF-8 olarak açılıp okunabildi. | Geçti |
| 2 | Veri satırı sayısı | 2026-10-24 | Nuri Enes Seyhan (DQ) | En az 100 veri satırı; v3 sözlüğüne göre tam 260 veri satırı olmalı. | Başlık hariç 260 veri satırı bulundu. | Geçti |
| 3 | Sütun adları ve sırası | 2026-10-24 | Nuri Enes Seyhan (DQ) | Sözlükte belirtilen 8 sütun aynı ad ve sırada bulunmalı. | 8 sütun eşleşti: `kampanya_id`, `tarih`, `kanal`, `gosterim`, `tiklama`, `donusum`, `harcama_tl`, `gelir_tl`. | Geçti |
| 4 | Tipler, biçimler ve değer aralıkları | 2026-10-24 | Nuri Enes Seyhan (DQ) | Tüm kayıtlar v3 tip, biçim, tarih, kimlik ve değer aralıklarına uymalı; tıklama gösterimi, dönüşüm tıklamayı aşmamalı. | 260 kaydın tamamında benzersiz `K001`–`K260` kimlikleri, Pazartesi tarihleri (`2025-10-06`–`2026-09-28`), tam iki ondalıklı tutarlar, sayısal aralıklar ve tıklama/dönüşüm ilişkileri doğrulandı. | Geçti |
| 5 | Kanal kategori değerleri | 2026-10-24 | Nuri Enes Seyhan (DQ) | Yalnızca izin verilen 5 kanal bulunmalı; her kanalda 52 kayıt olmalı. | Google Ads (52), Meta Ads (52), TikTok Ads (52), E-posta (52), SEO (52); beklenmeyen/eksik kategori yok. | Geçti |

## Hafta 3'ten Aktarılan Test Sonuçları

Hafta 3'te `tests/test-cases.md` içinde tutulan sonuçlar, önceki test tarihleri korunarak bu günlüğe taşınmıştır.

| Senaryo No (`test-cases.md`) | Senaryo | Test Tarihi | Test Eden | Beklenen Sonuç | Gerçekleşen Sonuç | Durum |
|---:|---|---|---|---|---|---|
| 2 | Veri satırı sayısı | 2026-10-18 | Nuri Enes Seyhan (DQ) | En az 100 veri satırı; v2 sözlüğüne göre hedef 260 veri satırı olmalı. | 260 veri satırı (başlıkla 261 satır). | Geçti |
| 5 | Kanal kategori değerleri | 2026-10-18 | Ceren Doğrul (Junior) | Yalnızca izin verilen 5 kanal bulunmalı; her kanalda 52 kayıt olmalı. | Google Ads (52), Meta Ads (52), TikTok Ads (52), E-posta (52), SEO (52); toplam 260 kayıt. | Geçti |

---

## Tespit Edilen Hatalar ve Açılan Kayıtlar
*(DQ ve Junior üyeler tarafından `bug` / `enhancement` etiketiyle açılan Issue'lar buraya listelenir)*

- **Hata 1:** *(Henüz açılmadı)*
- **Hata 2:** *(Henüz açılmadı)*
