# Dönem Raporu 1 (Görev 1 ve Görev 2 Dönemi)

**Grup:** G — PrimeBee (Dijital Pazarlama Karar Destek Sistemi)  
**PM (Proje Yöneticisi):** Dilara Başer (@baserdilara94-ui)  
**Hazırlanma / Güncelleme Tarihi:** 07 Kasım 2026  
**Teslim Tarihi:** 08 Kasım 2026 Pazar, 23:59  
**İlgili Duyuru:** [Duyuru 7 — İşleri Neticelendirin + Dönem Raporu 1 (PM)](https://github.com/MAKU-VBA-GBT-II/ders/blob/main/Duyuru-7_2026-11-01.md)  
**Sürüm:** [`gorev2-final`](https://github.com/MAKU-VBA-GBT-II/group-g/releases/tag/gorev2-final)

---

## 1. Yönetici Özeti

PrimeBee (Grup G) ekibi olarak Görev 1 ve Görev 2 dönemlerini (Hafta 1–6), planlanan tüm kabul kriterlerini eksiksiz sağlayarak, sıfır açık hata ve tam zamanında teslimat ile tamamlamış bulunmaktayız. Rol rotasyonunun başarıyla uygulandığı bu süreçte; sabit tohumlu ve parametreli simülasyon motorları (`src/kampanya_simulasyon.py`, `src/simulasyon.py`), veri şemaları ve sözlükleri (`docs/veri-sozlugu-g1.md`, `docs/veri-sozlugu.md`), 3'er parçalık profesyonel görselleştirme setleri (`visuals/`) ve 5 ana metriği kapsayan analiz dokümantasyonu (`docs/analiz-g2.md`) başarıyla üretilmiştir. Süreç boyunca karşılaşılan teknik kısıtlar (veri ezilmesi, CLI parametre eksikliği ve kanal seçim kısıtı) takım içi etkin geri bildirim, hata kartları ve PR inceleme döngüleriyle çözülmüş; repo `gorev2-final` etiketiyle sürümleştirilmiş ve proje panosunda açık kart bırakılmamıştır. Ekip olarak Görev 3'te partner şirketimiz Grup B ile gerçekleştirilecek B2B veri entegrasyonuna tam hazır durumdayız.

---

## 2. Teslim Edilenler (Görev 1 Kapanışından Bugüne)

| # | Başlık | İlgili Issue / PR | Teslim Edilen Dosyalar / Çıktılar | Durum |
|---|---|---|---|:---:|
| 1 | **Rol Rotasyonu & Skill Envanteri** | [PR #46](https://github.com/MAKU-VBA-GBT-II/group-g/pull/46) (`37b27db`) | `AGENTS.md` (Görev 2 rolleri, sorumluluk matrisi, devir teslim zinciri) | ✅ Tamamlandı |
| 2 | **G2 Veri Şeması ve Analiz Planı** | [#40](https://github.com/MAKU-VBA-GBT-II/group-g/issues/40), [PR #47](https://github.com/MAKU-VBA-GBT-II/group-g/pull/47) (`c466124`) | `docs/veri-sozlugu.md` (8 sütun şeması, kurallar, CLI parametreleri, M1–M5 formülleri), `skills/dq-sozluk/SKILL.md` | ✅ Tamamlandı |
| 3 | **G2 Parametreli Simülasyon Motoru** | [#41](https://github.com/MAKU-VBA-GBT-II/group-g/issues/41), [#53](https://github.com/MAKU-VBA-GBT-II/group-g/issues/53), [PR #49](https://github.com/MAKU-VBA-GBT-II/group-g/pull/49) (`da6f979`), [PR #59](https://github.com/MAKU-VBA-GBT-II/group-g/pull/59) (`3782821`) | `src/simulasyon.py`, `data/kampanya-simulasyon-g2.csv` (260 satır, seed: 42), `tests/test_simulasyon.py` (7 birim test), `skills/be-simulasyon/SKILL.md` | ✅ Tamamlandı |
| 4 | **G2 Grafik Seti ve Görselleştirici** | [#42](https://github.com/MAKU-VBA-GBT-II/group-g/issues/42), [#52](https://github.com/MAKU-VBA-GBT-II/group-g/issues/52), [PR #50](https://github.com/MAKU-VBA-GBT-II/group-g/pull/50) (`a50e80f`), [PR #55](https://github.com/MAKU-VBA-GBT-II/group-g/pull/55) (`195f56b`) | `src/grafik_uret.py` (`--veri`, `--cikti_dizini` CLI desteği), `visuals/gelir-harcama-trendi.png`, `visuals/kanal-roas-ctr.png`, `visuals/roas-dagilimi.png`, `skills/fe-gorsel/SKILL.md` | ✅ Tamamlandı |
| 5 | **G2 Metrik Hesabı ve Analiz Raporu** | [#43](https://github.com/MAKU-VBA-GBT-II/group-g/issues/43), [PR #51](https://github.com/MAKU-VBA-GBT-II/group-g/pull/51) (`e354786`) | `src/analiz_g2.py` (5 temel metrik), `docs/analiz-g2.md` (3 veri gözlemi, 1 aksiyon önerisi), `docs/requirements.md`, `skills/dq-analiz/SKILL.md` | ✅ Tamamlandı |
| 6 | **G2 Kalite Testleri & Kılavuz** | [#44](https://github.com/MAKU-VBA-GBT-II/group-g/issues/44), [PR #48](https://github.com/MAKU-VBA-GBT-II/group-g/pull/48) (`abac5de`), [PR #54](https://github.com/MAKU-VBA-GBT-II/group-g/pull/54) (`023c139`) | `tests/test-cases.md` (TC-1–TC-8 senaryoları), `tests/test-log.md` (tam test koşum günlükleri), `docs/user-manual.md`, `skills/dq-test/SKILL.md` | ✅ Tamamlandı |
| 7 | **G2 Junior Sözlük & Veri Ön İncelemesi** | [#45](https://github.com/MAKU-VBA-GBT-II/group-g/issues/45), [PR #56](https://github.com/MAKU-VBA-GBT-II/group-g/pull/56) (`0ccdcb3`) | `tests/test-log.md` (ön inceleme ve determinizm sonuçları tablosu), `skills/junior-kontrol/SKILL.md` | ✅ Tamamlandı |
| 8 | **Pano Hijyeni & Standartlaştırma** | [#57](https://github.com/MAKU-VBA-GBT-II/group-g/issues/57), [#58](https://github.com/MAKU-VBA-GBT-II/group-g/issues/58) | Dosya yolu/adlandırma standardizasyonu teyit edildi (#57), otomatik şema ön kontrol backlog değerlendirmesi yapıldı (#58) | ✅ Tamamlandı |
| 9 | **Sprint Raporu (Hafta 05)** | [PR #60](https://github.com/MAKU-VBA-GBT-II/group-g/pull/60), [PR #61](https://github.com/MAKU-VBA-GBT-II/group-g/pull/61) | `reports/report-w05.md` | ✅ Tamamlandı |
| 10 | **Mini Ürün Sürümü (Release)** | [`gorev2-final`](https://github.com/MAKU-VBA-GBT-II/group-g/releases/tag/gorev2-final) | PrimeBee Dijital Pazarlama Karar Destek Sistemi (Mini Ürün) etiketi ve sürüm paketi | ✅ Tamamlandı |
| 11 | **Dönem Raporu 1 & Ekip Geri Bildirimleri** | [#62](https://github.com/MAKU-VBA-GBT-II/group-g/issues/62), [#64](https://github.com/MAKU-VBA-GBT-II/group-g/issues/64), [PR #63](https://github.com/MAKU-VBA-GBT-II/group-g/pull/63) (`f3b98b5`) | `reports/donem-raporu-1.md`, tüm ekip geri bildirimleri derlemesi, resmi teslim | ✅ Tamamlandı |

---

## 3. Sayılarla Dönem (Süreç KPI'ları)

Dönem verileri GitHub CLI (`gh api`, `gh issue`, `gh pr`) ve yerel `git` analiz betikleriyle derlenmiştir:

| KPI Göstergesi | Görev 2 Dönemi | Depo Geneli (Tüm Dönem) | Not / Açıklama |
|---|:---:|:---:|---|
| **Açılan Issue Sayısı** | 12 | 48 | Görev 2 kapsamındaki tüm rol, hata, koordinasyon ve teslim kartları |
| **Kapatılan Issue Sayısı** | 12 | 48 | Depoda 5 Kasım ve teslim itibarıyla **0 açık Issue** bırakılmıştır |
| **Merge Edilen PR Sayısı** | 13 | 16 | PR #46–#51, #54–#56, #59–#61, #63 (main'e yalnızca PR ile giriş kuralı) |
| **Açık Kalan PR Sayısı** | 0 | 0 | Tüm açılan PR'lar incelenmiş ve ana dala birleştirilmiştir |
| **Ortalama İlk İnceleme/Yorum Süresi** | ~10.9 saat (654 dk) | ~10.9 saat | İnceleme yorumu alan PR'lar (en hızlı: PR #49 - 37 dk; PR #59 - 225 dk) |
| **Geciken / Son Tarihi Geçen İş Sayısı** | **0** | **0** | Tüm kabul kriterleri planlanan sprint takviminde tamamlanmıştır |

### Üye Bazında Dağılım

| Üye | G1 Rolü | G2 Rolü | G2 Commit | Toplam Commit | Kapatılan / Sorumlu Olunan Ana İşler (Tüm Dönem) |
|---|---|---|:---:|:---:|---|
| **Dilara Başer** (@baserdilara94-ui) | PM (Lider) | PM (Lider - sabit) | 9 | 31 | Prova #4, ilk repo mimarisi, README, AGENTS.md, Hafta 3-4-5 raporları, PR #46, #60, #61, #63, #57, #58, #62, #64, release |
| **Tuana Gürkan** (@tuanagurkan77) | FE | DQ (Analiz & Kalite) | 12 | 26 | Prova #3, FE grafik motoru & 3 görsel (#12, #32), #40 (şema), #43 (analiz), #44 (test), PR inceleme/onayları |
| **Nuri Enes Seyhan** (@seyhannurienes-afk) | DQ | BE (Simülasyon) | 3 | 20 | Prova #6, G1 analiz betiği & testleri (#11, #22, #23), #41 (simülasyon), #53 (kanal kısıtı), 7 birim test |
| **Özge Nur Doğu** (@Ozge-nur) | BE | FE (Görselleştirici) | 5 | 14 | Prova #7, G1 kampanya simülasyonu (#10), #42 (3 grafik seti), #52 (CLI desteği), taslaklar |
| **Ceren Doğrul** (@cerendogrul120-byte) | Junior | Junior (Ön İnceleme) | 2 | 20 | Prova #8, #9, G1 veri denetimi (#14, PR #15), #45 (ön inceleme & determinizm), #58 otomasyon önerisi |

---

## 4. Tıkananlar ve Çözümleri

Sprint sürecinde tespit edilen teknik engeller gizlenmemiş, ilgili GitHub Issue'ları açılarak şeffaf bir şekilde yönetilmiş ve çözülmüştür:

1. **G1 Veri Ezilmesi ve Format Uyumsuzluğu:**
   - *Engel:* Görev 1 sürecinde veri dosyasının başka bir commit'le 17 satıra ezilmesi ve tutarların tek ondalıklı yazılması sorunu yaşanmıştır.
   - *Çözüm:* BE (Özge Nur Doğu) tarafından `SEED = 42` ile veri yeniden üretilerek SHA-256 doğrulamasıyla geri yüklenmiş (`6d29ccd`); sözlük kurallarını denetleyen kontrol ve `f"{x:.2f}"` formatı eklenerek 260 satırlık v2 verisi teslim edilmiştir.
2. **FE Sabit Yol Bağımlılığı (Hata Kartı [#52](https://github.com/MAKU-VBA-GBT-II/group-g/issues/52)):**
   - *Engel:* FE görsel üretim betiği `src/grafik_uret.py`, sabit bir CSV yoluna bağlı çalışıyordu ve komut satırından parametre kabul etmiyordu. Bu durum betiğin farklı test veri setleriyle çalıştırılmasını zorlaştırıyordu.
   - *Çözüm:* DQ'nun entegrasyon testlerinde açtığı hata kartı doğrultusunda FE tarafından betiğe `--veri` ve `--cikti_dizini` CLI argümanları eklendi ([PR #55](https://github.com/MAKU-VBA-GBT-II/group-g/pull/55)) ve sorun giderildi.
3. **BE Kanal Seçim Kısıtı (Hata Kartı [#53](https://github.com/MAKU-VBA-GBT-II/group-g/issues/53)):**
   - *Engel:* `kampanya_sayisi` 5'ten küçük seçildiğinde simülatör varsayılan olarak yalnızca listenin ilk N kanalını üretiyor, kullanıcının istediği kanalları belirlemesine olanak tanımıyordu.
   - *Çözüm:* BE tarafından simülatöre `--kanallar` parametresi, geçersiz veya mükerrer kanal kontrolleri ve `tests/test_simulasyon.py` regresyon birim testleri (7 senaryo) eklendi ([PR #59](https://github.com/MAKU-VBA-GBT-II/group-g/pull/59)).
4. **Junior Ön İnceleme Yol Belirsizliği (İnceleme Kartı [#57](https://github.com/MAKU-VBA-GBT-II/group-g/issues/57)):**
   - *Engel:* Junior üyenin ilk incelemesinde Görev 1 dosya adlarıyla Görev 2 dosya adları arasında karışıklık yaşandı.
   - *Çözüm:* PM tarafından repo genelindeki dosya yapısı `main` dalında teyit edildi, isimlendirme standartları netleştirilerek kart kapatıldı.

---

## 5. Kim Ne Yaptı (Ekip Geri Bildirimleri — Issue #62 Referanslı)

Duyuru 7 (Bölüm 2) uyarınca Issue [#62](https://github.com/MAKU-VBA-GBT-II/group-g/issues/62) altında tüm ekip üyelerinin (junior dahil) proje başlangıcından itibaren tamamladıkları işler, takıldıkları noktalar ve Görev 3 önerileri derlenmiştir:

### Özet Tablo (Proje Başlangıcından İtibaren)

| Üye | Dönem Boyunca Rolleri | Ne Teslim Etti? (Proje Başından Bugüne Kanıtlı) | Neye Takıldı ve Nasıl Aştı? | Görev 3 Hedefi / Önerisi |
|---|---|---|---|---|
| **Dilara Başer** (@baserdilara94-ui) | PM (Lider - sabit) | **H1–H2:** Prova verisi (`data/prova-dilara.csv` - #4), keşif raporu (`reports/Yan-görev-1/kesif-Dilara.md`).<br>**G1 (PM):** İlk repo mimarisi, README, AGENTS.md (#5, commit `da76c18`, `72fa3ee`), Hafta 3-4 sprint raporları (`report-w03.md`, `report-w04.md`), `pm-rapor` skill'i.<br>**G2 (PM):** Rol rotasyonu koordinasyonu (PR #46), Hafta 5 sprint raporu (`report-w05.md` - PR #60, PR #61), `gorev2-final` release yayını, pano hijyeni (#57, #58), Dönem Raporu 1 hazırlığı (#62, PR #63, #64). | Rol rotasyonu sonrası devir teslim zincirinin senkronizasyonu; `AGENTS.md` devir teslim sırası netleştirilerek ve açık hata kartları takibiyle aşıldı. | Partner şirket Grup B ile B2B sözleşme standartlarını baştan netleştirmek; devir teslim kontrollerini CI ile otomatize etmek. |
| **Nuri Enes Seyhan** (@seyhannurienes-afk) | G1: DQ<br>G2: BE (Simülasyon) | **H1–H2:** Prova verisi (`data/prova-nuri.csv` - #6).<br>**G1 (DQ):** G1-Analiz (#11, #23, commit `028ee66`, `src/analiz_g1.py`, `docs/analiz-g1.md`, `skills/dq-analiz/SKILL.md`), 260 satır/8 sütun doğrulama; Hafta 4 DQ test (#22, commit `8ce74b2`, `tests/test-log.md`), #37 ve #38 enhancement önerileri; Grup B çapraz inceleme ([group-b #36](https://github.com/MAKU-VBA-GBT-II/group-b/issues/36), PR #34 onayı).<br>**G2 (BE):** Parametreli simülasyon motoru (#41, PR #49, commit `da6f979`, `src/simulasyon.py`, `kampanya-simulasyon-g2.csv`, `be-simulasyon` skill'i); kanal seçimi kısıtı çözümü (#53, PR #59, commit `3782821`, `--kanallar` desteği, 7 birim test). | G1 analizinin yeniden üretilememesi ve haftalık eksiklik için kendi DQ betiğini/raporunu oluşturdu. G2'de kanal seçiminin ilk kanallara kilitlenmesini `--kanallar` parametresi ve regresyon testleriyle çözdü. | Simülasyon, şema doğrulama, analiz ve testlerin birlikte ve tekrarlanabilir çalışmasını sağlamak; rol sahipliği ve veri devirlerini Issue/PR kanıtlarıyla izlemek. |
| **Tuana Gürkan** (@tuanagurkan77) | G1: FE<br>G2: DQ (Analiz & Kalite) | **H1–H2:** Prova verisi (`data/prova-tuana.csv` - #3), Streamlit keşif raporu (`reports/Yan-görev-1/kesif-Tuana-gurkan.md`).<br>**G1 (FE):** Görselleştirme motoru (`src/generate_visuals.py`), 3 parçalık grafik seti (`visuals/`), `fe-gorsel` skill dokümantasyonu (#12, #32).<br>**G2 (DQ):** 8 sütunlu veri şeması ve metrik formülleri (`docs/veri-sozlugu.md`, PR #47, #40); 5 metrik hesabı ve içgörü raporu (`src/analiz_g2.py`, `docs/analiz-g2.md`, `docs/requirements.md`, PR #51, #43); 8 senaryoluk tam kalite testi ve kılavuz (`tests/test-cases.md`, `tests/test-log.md`, `docs/user-manual.md`, PR #48, PR #54, #44); BE, FE ve Junior PR inceleme ve onayları (26 toplam commit). | G1'de Matplotlib eksen çakışması ve ROAS formül hatasını #32 ile çözdü. G2'de BE kanal kısıtı ve FE CLI eksikliğini doğrudan kod ezmek yerine #52 ve #53 hata kartları açarak koordine etti. | Partner şirket Grup B ile B2B veri değişimi (`exchange/`) sürecinde, şema doğrulama ve veri tutarlılığı kontrollerinin GitHub Actions (CI) üzerinde otomatik koşulması. |
| **Özge Nur Doğu** (@Ozge-nur) | G1: BE<br>G2: FE (Görselleştirici) | **H1–H2:** Rastgele sayı betiği ve prova CSV (`src/prova_ozge.py`, `data/prova-ozge.csv` - #7), gitignore keşif raporu (`reports/Yan-görev-1/kesif-Ozge-Nur.md`).<br>**G1 (BE):** Sabit tohumlu dijital pazarlama simülasyonu (`src/kampanya_simulasyon.py`, `data/kampanya-performans.csv` 260 satır, `docs/veri-sozlugu-g1.md`, `be-veri` skill'i - #10, commit `223be09`, v2 `4617f2a`, geri yükleme `6d29ccd`); Grup A Hilal'in inceleme önerileri (#27, commit `8091782`), Grup B be-veri incelemesi ([group-b #45](https://github.com/MAKU-VBA-GBT-II/group-b/issues/45)).<br>**G2 (FE):** 3 grafik seti (trend, kanal ROAS/CTR, dağılım - #42, PR #50, commit `a50e80f`, `src/grafik_uret.py`, `visuals/`, `fe-gorsel` skill'i); CLI desteği (#52, PR #55, commit `195f56b`). Yapay zekâ (Claude) destekli üretim ve yerel doğrulama. | Fork repo karışıklığını ayrı klonla aştı. Tek ondalık tutar hatasını `f"{x:.2f}"` ve ön denetimle çözdü. Ezilen veriyi SEED=42 ve SHA-256 ile geri yükledi. G2'de veri PR'da beklerken taslak ve fallback iskeletle takvimi korudu. | İşe başlamadan sözlük ve kabul kriterlerini dikkatle okumak; dosyayı şemaya göre denetlemek. Partner şirketle sözleşmeyi (alanlar, biçimler) baştan yazılı netleştirmek ve doğrulamak. |
| **Ceren Doğrul** (@cerendogrul120-byte) | G1: Junior<br>G2: Junior (Ön İnceleme) | **H1–H2:** Prova betiği ve CSV (`src/prova_ceren.py`, `data/prova-ceren.csv` - #8, #9), Matplotlib keşif raporu (`reports/Yan-görev-1/kesif-Ceren.md` - PR #35).<br>**G1 (Junior):** G1 veri denetimi, kanal testleri ve ön inceleme (#14, PR #15, commit `cf5875f`, `c43adae`), `junior-kontrol` skill'i (commit `cfe06a6`, `6b695cd`).<br>**G2 (Junior):** G2 sözlüğü ve simülasyon ön incelemesi (#45, PR #56, commit `0ccdcb3`, 260 satır/8 sütun, alternatif parametreler, determinizm doğrulaması, `tests/test-log.md`, `junior-kontrol` skill'i); otomatik şema ön kontrol önerisi (#58). | İlk kontrolde G1 dosyalarıyla ilerleme hatasını G2 teslimi ve DQ onayını bekleyip gerçek G2 dosyalarıyla aşarak tekrarladı; kampanya sayısı azalınca kanal sabitliğini tespit edip #53 ile ilişkilendirdi. | Şema, dosya yolu ve deterministik üretim kontrollerinin tek bir otomatik CI ön kontrol adımında toplanması ve her PR'da koşulması. |

---

## 6. Dersler (Retrospektif)

1. **Arayüz ve Sözleşme Önceliği (Contract-First Design):** FE ve DQ geliştiricilerinin BE verisi `main` dalına girmeden çalışmalarına başlayabilmesi için veri şemasının en başta dondurulması gerektiği görülmüştür. Özge Nur Doğu'nun taslak ve fallback veri yapısıyla ilerlemesi takvim gecikmelerini önlemiştir.
2. **Hata Kartı Odaklı Süreç Disiplini:** Tuana Gürkan'ın test sırasında bulduğu eksiklikleri kendisi kodlamak yerine #52 ve #53 hata kayıtları açarak ilgili uzmanlara devretmesi, izlenebilirliği sağlamış ve rol sınırlarını korumuştur.
3. **Veri Bütünlüğü ve Koruma:** Görev 1'de yaşanan veri ezilmesi tecrübesi, sabit tohum (SEED=42) ve SHA-256 parmak izi doğrulamasının önemini öğretmiş; Görev 2'de bu sayede sıfır veri kaybı yaşanmıştır.
4. **Otomasyon ve CI İhtiyacı:** Ekip üyelerinin tamamı, determinizm ve şema uyum testlerinin yerel kontrol yerine GitHub Actions üzerinde otomatik koşulması gerektiğinde birleşmiştir.

---

## 7. Görev 3 Hazırlığı (B2B Veri Değişimi Planı)

- **Partner Şirket Eşleşmesi:** Duyuru 5 uyarınca Grubumuz (PrimeBee — Grup G), **Grup B** ile eşleşmiştir.
- **Veri Değişimi Kapsamı:** PrimeBee dijital pazarlama simülasyonundan elde edilen performans çıktıları (kanal bazlı harcama, gelir, ROAS ve dönüşüm metrikleri), Grup B'nin ihtiyaç duyduğu veri formatına dönüştürülecek ve onlardan gelecek iş verileri analiz hattımıza dahil edilecektir (`exchange/` dizini).
- **Protokol ve Standartlar:** Görev 3 başında iki takımın PM ve DQ liderleri arasında ortak bir `docs/b2b-sozlesme.md` hazırlanacak; tarih formatları (ISO 8601), para birimleri, numerik hassasiyet (2 ondalık) ve UTF-8 karakter seti bağlayıcı olarak kararlaştırılacaktır.
- **Entegrasyon Doğrulama:** Gelen verilerin geçerliliği için önleyici DQ doğrulama testleri yazılacak ve B2B test döngüsü uygulanacaktır.

---

## Araç ve Model Bilgisi (Prompt Özeti)

Bu dönem raporu, PrimeBee ekibinin `pm-rapor` skill'i ([`skills/pm-rapor/SKILL.md`](skills/pm-rapor/SKILL.md)) yönergeleri ve dersin [Duyuru 7](https://github.com/MAKU-VBA-GBT-II/ders/blob/main/Duyuru-7_2026-11-01.md) şablonu esas alınarak **Antigravity (Gemini 3.8 Flash)** asistanı ile üretilmiştir. Rapordaki tüm sayılar ve iddialar GitHub API (`gh api`, `gh issue`, `gh pr`) ve Git geçmişi (`git log`, `git shortlog`) üzerinden olgusal olarak doğrulanmıştır.
