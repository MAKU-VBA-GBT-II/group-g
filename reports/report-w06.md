# Sprint Raporu - Hafta 06 (28.10–03.11.2026)

**Grup:** G — PrimeBee (Dijital Pazarlama) · **PM:** Dilara Başer

**Hazırlanma tarihi:** 03.11.2026 · **Son tarih:** 03 Kasım 2026 Salı, 23:59

---

## Planlanan (Görev 2)

| Issue | Başlık | Atanan | Kabul kriteri | Son tarih |
|---|---|---|---|---|
| #40 | G2-sem — Veri şeması ve analiz planı | Tuana Gürkan (DQ) | `docs/veri-sozlugu.md` 8 sütun, veri tipleri, mantıksal kurallar, CLI parametreleri ve M1–M5 metrik formülleri ile hazırlanır; `dq-sozluk` skill'i güncellenir. | 01 Kas 23:59 |
| #41 | G2-veri — Parametreli simülasyon | Nuri Enes Seyhan (BE) | `src/simulasyon.py` parametreli ve sabit tohumlu (42) olarak yazılır; 260 satırlık `data/kampanya-simulasyon-g2.csv` üretilir; `be-simulasyon` skill'i eklenir. | 02 Kas 23:59 |
| #42 | G2-gorsel — Grafik seti | Özge Nur Doğu (FE) | `src/grafik_uret.py` ile 3 adet 200 DPI PNG görsel (zaman serisi trendi, kanal ROAS/CTR, ROAS dağılımı) üretilir; taslaklar önceden Issue'ya eklenir; `fe-gorsel` skill'i güncellenir. | 02 Kas 23:59 |
| #43 | G2-analiz — Metrik hesabı ve bulgular | Tuana Gürkan (DQ) | `src/analiz_g2.py` ile 5 metrik hesaplanır; `docs/analiz-g2.md` dosyasına 3 veri gözlemi ve 1 uygulanabilir eylem önerisi yazılır; `docs/requirements.md` hazırlanır. | 02 Kas 23:59 |
| #44 | G2-test — Test senaryoları ve PR incelemesi | Tuana Gürkan (DQ) | `tests/test-cases.md` hazırlanır; 8 kabul senaryosu (TC-1–TC-8) koşulup `tests/test-log.md` doldurulur; `docs/user-manual.md` hazırlanır ve BE PR'ı incelenir. | 02 Kas 23:59 |
| #45 | G2-junior — Sözlük ve Veri Ön İncelemesi | Ceren Doğrul (Junior) | Şema ve dosya kontrolleri yapılır; alternatif parametre/tohum denemeleri koşulur; gözlemler `tests/test-log.md` dosyasına işlenir. | 03 Kas 23:59 |
| #52 | fix(fe): grafik_uret.py CLI parametre desteği | Özge Nur Doğu (FE) | `src/grafik_uret.py` betiğine `--veri` ve `--cikti_dizini` CLI argüman desteği eklenir. | 03 Kas 23:59 |
| #53 | fix(be): kampanya_sayisi < 5 sabit kanal kısıtı | Nuri Enes Seyhan (BE) | `src/simulasyon.py` betiğine `--kanallar` parametresi eklenir; regresyon birim testleri `tests/test_simulasyon.py` ile doğrulanır. | 03 Kas 23:59 |
| #57 | G2-veri — Dosya yolu ve isim tutarsızlığı | Ceren Doğrul (Junior) | G1/G2 dosya yolları (`docs/veri-sozlugu.md`, `src/simulasyon.py`) ve adlandırma standartları teyit edilir. | 03 Kas 23:59 |
| #58 | G2-junior — Otomatik şema ve veri ön kontrolü | Ceren Doğrul (Junior) | Şema ve temel kural kontrollerinin otomatik betikle yapılmasına yönelik geliştirme önerisi değerlendirilir. | 03 Kas 23:59 |

---

## Yapılan

| Issue / Görev | Kanıt (commit / PR / dosya) | Durum |
|---|---|---|
| #46 Rol Rotasyonu | PR #46, Commit `37b27db` — `AGENTS.md` Görev 2 rolleri ve skill envanteri güncellendi | ✅ TAMAMLANDI |
| #40 G2 Şema ve Sözlük | PR #47, Commit `c466124`, `6ba5ca9` — `docs/veri-sozlugu.md`, `skills/dq-sozluk/SKILL.md` | ✅ TAMAMLANDI |
| #41 G2 Simülasyon Motoru | PR #49, Commit `da6f979`, `47cf641` — `src/simulasyon.py`, `data/kampanya-simulasyon-g2.csv`, `skills/be-simulasyon/SKILL.md` | ✅ TAMAMLANDI |
| #42 G2 Grafik Seti | PR #50, Commit `5604af0`, `98f0516`, `3aea495`, `a50e80f` — `src/grafik_uret.py`, `visuals/gelir-harcama-trendi.png`, `visuals/kanal-roas-ctr.png`, `visuals/roas-dagilimi.png` | ✅ TAMAMLANDI |
| #43 G2 Metrik ve Analiz | PR #51, Commit `e354786`, `85a4729` — `src/analiz_g2.py`, `docs/analiz-g2.md`, `docs/requirements.md`, `skills/dq-analiz/SKILL.md` | ✅ TAMAMLANDI |
| #44 G2 Kalite Testleri & Kılavuz | PR #48 (`abac5de`), PR #54 (`023c139`, `6d6711a`) — `tests/test-cases.md`, `tests/test-log.md` (TC-1–TC-8 koşumu), `docs/user-manual.md` | ✅ TAMAMLANDI |
| #45 G2 Junior Ön İnceleme | PR #56, Commit `93601cc`, `0ccdcb3`, `bb7a464` — `tests/test-log.md` ön inceleme tablosu, tohum determinizm testleri, `skills/junior-kontrol/SKILL.md` | ✅ TAMAMLANDI |
| #52 Grafik CLI Düzeltmesi | PR #55, Commit `195f56b`, `e03e5a3` — `src/grafik_uret.py` `--veri` ve `--cikti_dizini` argümanları eklendi | ✅ TAMAMLANDI |
| #53 Kanal Seçimi ve Birim Test | PR #59, Commit `3782821`, `b0cf4e7` — `src/simulasyon.py` `--kanallar` desteği, `tests/test_simulasyon.py` regresyon koşumu | ✅ TAMAMLANDI |
| #57 Yol ve İsim Standardizasyonu | Issue #57 kapanış yorumu — `docs/veri-sozlugu.md` ve `src/simulasyon.py` `main` dalında doğrulandı, kart kapatıldı | ✅ TAMAMLANDI |
| #58 Otomatik Doğrulama Önerisi | Issue #58 kapanış yorumu — Manuel kontrollerin başarıyla tamamlandığı, sürekli otomasyon önerisinin backlog'a alındığı açıklandı, kart kapatıldı | ✅ TAMAMLANDI |

---

## Devir teslim zinciri

- **DQ Şema $\rightarrow$ BE / FE / Junior:** ✅ DQ (Tuana Gürkan) `docs/veri-sozlugu.md` şemasını ve metrik formüllerini teslim etti (PR #47). BE (Nuri Enes Seyhan) simülasyon kodlamasına, FE (Özge Nur Doğu) grafik taslaklarına ve Junior (Ceren Doğrul) şema kontrolüne bu devir yorumuyla başladı.
- **BE $\rightarrow$ DQ / FE / Junior:** ✅ BE `src/simulasyon.py` ve 260 satırlık varsayılan veri setini üretti (PR #49). DQ veri kalitesi testlerine, FE gerçek veriyle grafik üretimine, Junior ise bağımsız parametre denemelerine başladı.
- **DQ Onayı & Birleştirme:** ✅ DQ (Tuana Gürkan), BE PR'ını (#49), FE PR'ını (#50), FE fix PR'ını (#55), Junior PR'ını (#56) ve BE fix PR'ını (#59) GitHub üzerinden inceleyerek onayladı (Approve) ve `main` dalına dahil etti.
- **PM Sprint Hijyeni:** ✅ PM (Dilara Başer), pano kontrollerini yaptı; açık kalan Issue #57 ve #58 için çözüm/değerlendirme kayıtlarını girerek kapattı. Panoda açık kart bırakılmadı (0 açık Issue).

---

## Tıkanan / riskler

1. **FE Sabit Yol Bağımlılığı (Issue #52):** Görselleştirme betiğinin CLI argümanı almaması nedeniyle tespit edilen kısıt, FE tarafından hızla çözülerek PR #55 ile giderildi.
2. **BE Kanal Seçim Kısıtı (Issue #53):** Kampanya sayısı 5'ten küçük seçildiğinde sadece ilk N kanalın üretilmesi kısıtı, BE tarafından `--kanallar` parametresi ve `tests/test_simulasyon.py` regresyon testleriyle giderildi (PR #59).
3. **Junior Dosya Yolu Tutarsızlığı Algısı (Issue #57):** G1 ve G2 dosya adları arasındaki karışıklık, PR'ların `main` dalına eksiksiz alınması ve standartlaştırılmasıyla çözüldü.

---

## Kim ne yaptı (Görev 2)

| Üye | Görev 2 Rolü | PR & Commit Katkısı | Kapattığı / Teslim Ettiği İşler | Açık Kalan Issue |
|---|---|---|---|:---:|
| **Dilara Başer** | PM (Lider) | `37b27db`, PR #46, `report-w06.md` | Sprint koordinasyonu, pano hijyeni, #57 ve #58 inceleme/kapanışı, sprint raporu | 0 |
| **Nuri Enes Seyhan** | BE | `da6f979`, `3782821`, PR #49, PR #59 | #41 (G2-veri), #53 (kanal seçimi kısıtı), `src/simulasyon.py`, `tests/test_simulasyon.py` | 0 |
| **Tuana Gürkan** | DQ | `c466124`, `abac5de`, `e354786`, `023c139`, PR #47, #48, #51, #54 | #40 (şema), #43 (analiz), #44 (test), `analiz_g2.py`, `requirements.md`, `user-manual.md`, PR onayları | 0 |
| **Özge Nur Doğu** | FE | `5604af0`, `98f0516`, `3aea495`, `195f56b`, PR #50, PR #55 | #42 (görsel), #52 (grafik CLI desteği), `src/grafik_uret.py`, 3 PNG grafik seti | 0 |
| **Ceren Doğrul** | Junior | `93601cc`, `0ccdcb3`, PR #56 | #45 (junior kontrol), alternatif parametre denemeleri, determinizm kontrolleri | 0 |

---

## Gelecek dönem (Görev 3 Hazırlığı)

- **Mini Ürün Sürümleme:** Görev 2 tamamlanmış olup depo üzerinde `gorev2-final` sürüm etiketi (release tag) oluşturulacaktır.
- **Otomasyon Genişletmesi:** Issue #58 kapsamında önerilen otomatik doğrulama betiğinin CI/CD veya git pre-commit kancalarına entegrasyonu değerlendirilecektir.
- **Yeni Rol Rotasyonu:** Dönem planı takvimi gereği Görev 3 için rol rotasyonu planlanacaktır.

---
*Bu rapor pm-rapor skill'i (`skills/pm-rapor/SKILL.md`) kullanılarak Antigravity tarafından hazırlanmıştır. GitHub CLI (`gh issue`, `gh pr`, `git log`) izleri ve depo dosyaları doğrulanarak derlenmiştir.*
