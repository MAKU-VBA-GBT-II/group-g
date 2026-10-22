# Sprint Raporu - Hafta 4 (20.10–27.10.2026)

**Grup:** G — PrimeBee (Dijital Pazarlama) · **PM:** Dilara Başer

**Hazırlanma tarihi:** 22.10.2026 · **Son tarih:** 27 Ekim 2026 Salı, 23:59

---

## Planlanan

| Issue | Başlık | Atanan | Kabul kriteri | Son tarih |
|---|---|---|---|---|
| #10 | G1-Sektör Veri | Özge Nur Doğu (BE) | `data/kampanya-performans.csv` depoda; en az 100 satır, 6 alan, sabit tohumlu betik, şema `docs/veri-sozlugu-g1.md` | 20 Eki 23:59 |
| #11 | G1-Analiz | Nuri Enes Seyhan (DQ) | `docs/analiz-g1.md` depoda; toplam gelir, ortalama ROAS, kanal kırılımları, top-3, 3 gözlem, 1 eylem önerisi | 20 Eki 23:59 |
| #12 | G1-Görsel | Tuana Gürkan (FE) | 2 PNG `visuals/`'da: zaman serisi + kanal kırılımı; başlık, eksen etiketi, birim; BE verisinden üretilmiş | 20 Eki 23:59 |
| #13 | G1-Test | Nuri Enes Seyhan (DQ) | `tests/test-cases.md` en az 5 senaryo | 20 Eki 23:59 |
| #14 | G1-Junior | Ceren Doğrul (Junior) | PM tarafından Issue üzerinden verilecek junior görevi | 20 Eki 23:59 |

Ek PM görevleri: pano günlük kontrolü, `report-w04.md` commit'i, kök dizinde `AGENTS.md`, `skills/pm-rapor/SKILL.md`.

---

## Yapılan

| Issue | Kanıt (commit / dosya) | Durum |
|---|---|---|
| #10 G1-Sektör Veri | `6d29ccd` — `data/kampanya-performans.csv` (260 satır, SEED=42, şema v2) | ✅ TAMAMLANDI |
| #11 G1-Analiz | `dffd634` — `docs/analiz-g1.md` (toplam gelir 10.541.572,97 TL; ort. ROAS 17,43x; 5 kanal kırılımı; top-3) | ✅ TAMAMLANDI |
| #12 G1-Görsel | `42c779c` — `visuals/gelir-zaman-serisi.png`, `visuals/kanal-kirilim.png` (birleşik ROAS metoduyla, analizle uyumlu) | ✅ TAMAMLANDI |
| #13 G1-Test | `f268f45` — `tests/test-cases.md` (5 senaryo) | ✅ TAMAMLANDI |
| #14 G1-Junior | `b732568` (merge PR #15) — `tests/test-cases.md` güncellendi, `skills/junior-kontrol/SKILL.md` eklendi | ✅ TAMAMLANDI |

---

## Devir teslim zinciri

- **BE → DQ** (G1-Analiz #11): ✅ Özge Nur Doğu "Veri hazır — commit `4617f2a`, 260 satır" yorumunu yazdı.
- **BE → FE** (G1-Görsel #12): ✅ Özge Nur Doğu devir teslim yorumunu G1-Görsel'e yazdı; veri uyumsuzluğu sonradan tespit edildi ve `6d29ccd` ile düzeltildi.
- **DQ → FE** (grafik doğrulama): ✅ Nuri Enes Seyhan grafik değerlerini inceleyerek FE'ye revize yorumları yazdı; FE son sürümü `42c779c` ile kapattı.
- **DQ onayı** (nihai analiz): ✅ "Analiz nihai veri üzerinde doğrulandı — onaylıyorum." yorumu G1-Analiz #11'de mevcut.

---

## Tıkanan / riskler

- **Grafik ROAS uyumsuzluğu:** FE (`generate_visuals.py`) başlangıçta yanlış sütunu ROAS olarak hesapladı; `gelir_tl` değerleri kanal ROAS'ı gibi gösterildi. DQ'nun tespiti üzerine birleşik ROAS metoduna geçildi ve grafikler yeniden üretildi. Çözüldü: `42c779c`.
- **Veri dosyası üstüne yazma:** Ara bir commit'te `kampanya-performans.csv`, 17 satırlık farklı bir dosyayla değişti. BE `6d29ccd` ile orijinal 260 satırlık veriyi geri yükledi.
- **Junior PR gecikmesi:** Junior'ın `junior-kontrol-g1` dalı, DQ onayı alınana kadar main'e alınmadı. PR #15 `b732568` ile merge edildi.
- **PM skill dizin adı:** `skills/PM - rapor/PM rapor.md` doğru adlandırma kuralını (`skills/pm-rapor/SKILL.md`) karşılamıyordu. Bu rapor commit'i ile birlikte düzeltildi.

---

## Kim ne yaptı

| Üye | Rol | Öne çıkan commit | Kapattığı Issue |
|---|---|---|---|
| Dilara Başer | PM | `dc4acab` `204d84e` `5992fda` | — (pano yönetimi, rapor, AGENTS.md, keşif raporu) |
| Özge Nur Doğu | BE | `6d29ccd` `536f5b5` `edca440` | #10 |
| Nuri Enes Seyhan | DQ | `dffd634` `ecfad88` `690cc07` | #11 #13 |
| Tuana Gürkan | FE | `42c779c` `0f19f94` `950fa5f` | #12 |
| Ceren Doğrul | Junior | `b732568` (PR #15 merge) | #14 |

---

## Gelecek hafta (Hafta 5)

- **DQ (Hafta 4 görevi):** `tests/test-cases.md` senaryolarını gerçek veri üzerinde çalıştır; sonuçları `tests/test-log.md`'ye tarihli olarak işle. En az 2 bug veya enhancement Issue'su aç.
- **BE + FE:** Atanan hataları düzelt; commit mesajında `Fixes #<no>` kullan.
- **DQ — kapanış onayı:** Nihai veri/şema uyumunu doğrula; `G1-analiz` Issue'suna kapanış yorumu yaz.
- **PM:** Tüm G1 Issue'larının kanıt yorumuyla kapandığını doğrula; `gorev1-final` release'ini oluştur; AGENTS.md'nin güncel olduğunu kontrol et.
- **Yan Görev 3 — Çapraz Skill İncelemesi:** Grup G → Grup B'yi inceler. PM (Dilara Başer), Grup B'nin `pm-rapor` skill'ini ve `AGENTS.md`'sini okuyup Grup B reposunda `enhancement` etiketli bir Issue açar.
- **Hafta 5'ten itibaren:** `main`'e yalnızca PR ile girilir; kod/veri PR'ları DQ onayı olmadan merge edilmez.

---

*Bu rapor pm-rapor skill'i (`skills/pm-rapor/SKILL.md`) kullanılarak Antigravity (Claude Sonnet 4.6 Thinking) tarafından hazırlanmıştır. Issue geçmişi, commit logları ve Issue yorumları GitHub CLI ile okunarak derlenmiştir.*
