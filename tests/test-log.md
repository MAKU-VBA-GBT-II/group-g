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
