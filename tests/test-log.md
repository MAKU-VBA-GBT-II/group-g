# G1 Kampanya Performans Veri Kalitesi Test Sonuç Günlüğü (test-log.md)

**Şirket:** PrimeBee - Grup G (Dijital Pazarlama)  
**Test Edilen Dosya:** `data/kampanya-performans.csv`  
**Referans:** `tests/test-cases.md`, `docs/veri-sozlugu-g1.md`  
**Sorumlular:** Nuri Enes Seyhan (DQ), Ceren Doğrul (Junior)  

---

## Test Koşum Kayıtları

| No | Senaryo | Test Tarihi | Test Eden | Beklenen Sonuç | Gerçekleşen Sonuç | Durum (Geçti / Kaldı) | İlgili Issue / Not |
|---:|---|---|---|---|---|---|---|
| 1 | Satır sayısı ve sütun varlığı kontrolü | - | - | - | *Henüz koşulmadı* | - | #22 |
| 2 | Kanal kategori değerleri ve dağılımı | 2026-10-23 | Ceren Doğrul | Yalnızca izin verilen 5 kanal bulunmalı; her kanalda 52 kayıt olmalı. | 5 kanal bulundu: Google Ads (52), Meta Ads (52), TikTok Ads (52), E-posta (52), SEO (52). Beklenmeyen/eksik kanal yok; 260 kayıt kontrol edildi. | Geçti | #21 |
| 3 | Tıklama/Gösterim ve Dönüşüm/Tıklama oran mantığı | - | - | - | *Henüz koşulmadı* | - | #22 |
| 4 | Tarih formatı, aralık ve tutar format kontrolü | - | - | - | *Henüz koşulmadı* | - | #22 |
| 5 | Boş hücre ve eksik veri kontrolü | - | - | - | *Henüz koşulmadı* | - | #22 |

---

## Tespit Edilen Hatalar ve Açılan Kayıtlar
*(DQ ve Junior üyeler tarafından `bug` / `enhancement` etiketiyle açılan Issue'lar buraya listelenir)*

- **Hata 1:** *(Henüz açılmadı)*
- **Hata 2:** *(Henüz açılmadı)*
