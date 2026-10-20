# Hafta 3 Sprint Raporu

**Grup:** G — PrimeBee (Dijital Pazarlama)

**Grup Lideri (PM):** Dilara Başer

**Hazırlanma tarihi:** 20.10.2026

**Son tarih:** 20 Ekim 2026 Salı, 23:59

---

## Planlanan

| Issue | Atanan | Kabul kriteri | Son tarih |
|---|---|---|---|
| G1-veri — Sektör verisini üret (#10) | BE | `data/kampanya-performans.csv` depoda: en az 100 satır, en az 6 alan, `kanal` alanında en az 4 değer; sabit tohumlu `src/uret_veri.py`; şema `docs/veri-sozlugu-g1.md` içinde yazılı | 20 Ekim 2026 Salı, 23:59 |
| G1-analiz — Metrikleri hesapla ve bulguları yaz (#11) | DQ | `docs/analiz-g1.md` depoda: en az 5 metrik (1 toplam, 1 ortalama, 2 kırılım, top-3), her birinin yorumu, 3 gözlem ve 1 eylem önerisi mevcut | 20 Ekim 2026 Salı, 23:59 |
| G1-gorsel — 2 grafik üret (#12) | FE | 2 PNG grafik `visuals/` içinde: biri zaman serisi, diğeri kırılım; başlık, eksen etiketi ve birim var; BE verisinden üretilmiş; taslak Issue'da | 20 Ekim 2026 Salı, 23:59 |
| G1-test — Veri kalitesi testleri (#13) | DQ | `tests/test-cases.md` en az 5 senaryo içeriyor | 20 Ekim 2026 Salı, 23:59 |
| G1-junior — Junior görevi (#14) | Ceren Doğrul (Junior) | Junior üyeye PM tarafından Issue üzerinden verilen görev | 20 Ekim 2026 Salı, 23:59 |

Ek PM görevleri: pano günlük kontrolü, `report-w03.md` commit'i, kök dizine `AGENTS.md`, `skills/pm-rapor/SKILL.md`.

Yan görev: Git keşfi yan görevi ekibe ayrıca verildi.

Skill şartı: Her üye kendi adımını `skills/<rol>-<iş>/SKILL.md` ile yaptı; skill ve çıktı birlikte commit'lendi.

---

## Yapılan

| Issue | Durum | Not |
|---|---|---|
| G1-veri (#10) | TAMAMLANDI | |
| G1-analiz (#11) | TAMAMLANDI | |
| G1-gorsel (#12) | TAMAMLANDI | |
| G1-test (#13) | TAMAMLANDI | |
| G1-junior | TAMAMLANDI | |
| Yan görev (Git keşfi) | TAMAMLANDI | Tüm üyeler yaptı |

---

## Tıkanan

- FE (Tuana Gürkan) dosyaları depoya yüklerken hata yaptı. PM (Dilara Başer) uyardı; BE (Özge Nur Doğu) ve DQ (Nuri Enes Seyhan) desteğiyle hata düzeltildi.
- DQ (Nuri Enes Seyhan) grafikler için FE'ye (Tuana Gürkan) revize yorumları yaptı; grafikler bu yorumlara göre güncellendi.

---

## Kim ne yaptı

| Üye | Rol | Yaptığı iş | Issue / Commit |
|---|---|---|---|
| Dilara Başer | PM | Dört Issue'yu açtı, panoyu yönetti; ekibi uyardı ve yönlendirdi; `AGENTS.md`, `skills/pm-rapor/SKILL.md` ve veri sözlüğü taslağını hazırladı; haftalık raporu commit/Issue geçmişinden hazırladı; junior üyeye görevini Issue ile verdi; yan görevi ekibe verdi | `AGENTS.md`, `report-w03.md` |
| Özge Nur Doğu | BE | Dijital pazarlama kampanya performansı için sabit tohumlu (SEED = 42) sentetik veri üretti; şemayı DQ ile kesinleştirdi; dosya yükleme hatasının düzeltilmesinde FE'ye destek verdi; yan görevi yaptı | #10 |
| Nuri Enes Seyhan | DQ | Veriden metrik, gözlem ve eylem önerisi çıkardı; veri için en az 5 manuel test senaryosu tanımladı, "Gerçekleşen sonuç" alanlarını Hafta 4 için boş bıraktı; grafikler için FE'ye revize yorumları yaptı; hatanın düzeltilmesinde destek verdi; yan görevi yaptı | #11 #13 |
| Tuana Gürkan | FE | Önce grafik taslaklarını Issue'ya ekledi; kampanya verisinden zaman serisi ve kanal kırılımı grafiklerini üretti; dosya yükleme hatasını ekip desteğiyle düzeltti; DQ'nun revize yorumlarına göre grafikleri güncelledi; yan görevi yaptı | #12 |
| Ceren Doğrul | Junior | Kendisine verilen junior görevini yaptı; yan görevi yaptı | #14 |

---

## Gelecek hafta (Hafta 4)

- `tests/test-cases.md` içindeki "Gerçekleşen sonuç" sütunu doldurulacak.
- `AGENTS.md` skill envanteri güncel tutulacak.
