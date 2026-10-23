# Sprint Raporu - Hafta 03 (14.10–20.10.2026)

**Grup:** G — PrimeBee (Dijital Pazarlama) · **PM:** Dilara Başer

**Hazırlanma tarihi:** 20.10.2026 · **Son tarih:** 20 Ekim 2026 Salı, 23:59

---

## Planlanan

| Issue | Başlık | Atanan | Kabul kriteri | Son tarih |
|---|---|---|---|---|
| #10 | G1-Sektör Veri | Özge Nur Doğu (BE) | `data/kampanya-performans.csv` depoda: en az 100 satır, en az 6 alan, `kanal` alanında en az 4 değer; sabit tohumlu `src/kampanya_simulasyon.py`; şema `docs/veri-sozlugu-g1.md` içinde yazılı | 20 Eki 23:59 |
| #11 | G1-Analiz | Nuri Enes Seyhan (DQ) | `docs/analiz-g1.md` depoda: en az 5 metrik (1 toplam, 1 ortalama, 2 kırılım, top-3), her metriğe 1–2 cümle yorum, 3 gözlem, 1 eylem önerisi | 20 Eki 23:59 |
| #12 | G1-Görsel | Tuana Gürkan (FE) | 2 PNG grafik `visuals/` içinde (zaman serisi ve kırılım); başlık, eksen etiketi ve birim var; BE verisinden üretilmiş; taslak ekran görüntüleri Issue'da | 20 Eki 23:59 |
| #13 | G1-Test | Nuri Enes Seyhan (DQ) | `tests/test-cases.md` en az 5 senaryo içeriyor | 20 Eki 23:59 |
| #14 | G1-Junior Görev | Ceren Doğrul (Junior) | Veri kontrol bulguları Issue'da yorum olarak yazılı; `skills/junior-kontrol/SKILL.md` ve 2 test senaryosu depoda commit'li | 20 Eki 23:59 |

Ek PM görevleri: Pano günlük kontrolü, `report-w03.md` commit'i, kök dizinde `AGENTS.md`, `skills/pm-rapor/SKILL.md`.

---

## Yapılan

| Issue | Kanıt (commit / dosya) | Durum |
|---|---|---|
| #10 G1-Sektör Veri | Commit `4617f2a`, `6d29ccd` — `data/kampanya-performans.csv` (260 satır, SEED=42, şema v2), `docs/veri-sozlugu-g1.md`, `skills/be-veri/SKILL.md` | ✅ TAMAMLANDI |
| #11 G1-Analiz | Commit `dffd634` — `docs/analiz-g1.md` (toplam gelir 10.541.572,97 TL, ort. ROAS 17,43x, kanal kırılımları, top-3, 3 gözlem, 1 öneri), `skills/dq-analiz/SKILL.md` | ✅ TAMAMLANDI |
| #12 G1-Görsel | Commit `42c779c` — `visuals/gelir-zaman-serisi.png`, `visuals/kanal-kirilim.png`, `skills/fe-gorsel/SKILL.md` | ✅ TAMAMLANDI |
| #13 G1-Test | Commit `f268f45` — `tests/test-cases.md` (5 senaryo), `skills/dq-test/SKILL.md` | ✅ TAMAMLANDI |
| #14 G1-Junior Görev | PR #15 (commit `b732568`) — `tests/test-cases.md` (2 senaryo güncellendi), `skills/junior-kontrol/SKILL.md` | ✅ TAMAMLANDI |
| Yan Görev (Açık Kaynak Keşfi) | Rapor anında (20 Ekim 23:59 itibarıyla) depoda henüz teslim edilmiş dosya bulunmuyordu. Ekip üyelerinin keşif dosyaları 21–22 Ekim tarihlerinde repoya eklenmiştir. | ⏳ Hafta 3 raporu anında depoda yoktu (21–22 Ekim'de teslim edildi) |

---

## Devir teslim zinciri

- **BE → DQ** (G1-Analiz #11): ✅ Özge Nur Doğu "Veri hazır — commit `4617f2a`, 260 satır" devir teslim yorumunu yazdı.
- **BE → FE** (G1-Görsel #12): ✅ Özge Nur Doğu "Veri hazır" devir teslim yorumunu yazdı.
- **DQ → FE** (grafik doğrulama): ✅ Nuri Enes Seyhan taslak ve grafik revize yorumlarını yazdı; FE grafiklerini bu yorumlara göre güncelledi.
- **DQ onayı** (nihai analiz): ✅ Nuri Enes Seyhan nihai analiz doğrulamasını gerçekleştirdi.

---

## Tıkanan / riskler

- **Veri dosyası ve `AGENTS.md` ezilmesi olayı:** FE (Tuana Gürkan) tarafından yapılan `0f19f94` merge commit'i, Özge Nur Doğu'nun ürettiği 260 satırlık `data/kampanya-performans.csv` veri dosyasını 16 satırlık farklı bir dosyayla değiştirmiş ve kök dizindeki `AGENTS.md` dosyasını tek satıra indirmiştir. Durum fark edilerek BE (Özge Nur Doğu) `6d29ccd` commit'i ile 260 satırlık orijinal veriyi geri yüklemiş ve `AGENTS.md` dosyası kurtarılmıştır.
- **Grafik ROAS hesaplama uyumsuzluğu:** FE betiği (`generate_visuals.py`) ilk aşamada yanlış sütunu kullanarak hatalı ROAS değerleri çizmiştir. DQ'nun uyarısı ve revize talebiyle birleşik ROAS formülüne (toplam gelir / toplam harcama) geçilmiş ve grafikler `42c779c` commit'iyle düzeltilmiştir.
- **Junior PR entegrasyonu:** Ceren Doğrul'un junior görevi `junior-kontrol-g1` dalından PR #15 ile sunulmuş ve `b732568` ile merge edilmiştir.

---

## Kim ne yaptı

| Üye | Rol | Commit | Kapattığı Issue |
|---|---|---|---|
| Dilara Başer | PM | `dc4acab`, `204d84e` | — (pano yönetimi, 5 Issue açılışı, `AGENTS.md`, `report-w03.md`, `skills/pm-rapor/SKILL.md`) |
| Özge Nur Doğu | BE | `4617f2a`, `6d29ccd` | #10 |
| Nuri Enes Seyhan | DQ | `dffd634`, `f268f45`, `ecfad88` | #11, #13 |
| Tuana Gürkan | FE | `42c779c`, `0f19f94` | #12 |
| Ceren Doğrul | Junior | `b732568` (PR #15) | #14 |

---

## Gelecek hafta (Hafta 4)

- `tests/test-cases.md` senaryoları gerçek veri üzerinde çalıştırılacak ve sonuçlar tarihli olarak `tests/test-log.md` dosyasına işlenecek.
- `AGENTS.md` skill envanteri `junior-kontrol` dahil edilerek eksiksiz ve güncel tutulacak.
- Açık kaynak keşif yan görevleri ortak klasör altında tamamlanacak.
