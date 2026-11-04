# Dönem Raporu 1 (Görev 1 ve Görev 2 Dönemi)

**Grup:** G — PrimeBee (Dijital Pazarlama Karar Destek Sistemi)  
**PM (Proje Yöneticisi):** Dilara Başer (@baserdilara94-ui)  
**Hazırlanma Tarihi:** 04 Kasım 2026  
**Teslim Tarihi:** 08 Kasım 2026 Pazar, 23:59  
**İlgili Duyuru:** [Duyuru 7 — İşleri Neticelendirin + Dönem Raporu 1 (PM)](https://github.com/MAKU-VBA-GBT-II/ders/blob/main/Duyuru-7_2026-11-01.md)  
**Sürüm:** [`gorev2-final`](https://github.com/MAKU-VBA-GBT-II/group-g/releases/tag/gorev2-final)

---

## 1. Yönetici Özeti

PrimeBee (Grup G) ekibi olarak Görev 2 dönemini (Hafta 5–6), planlanan tüm kabul kriterlerini eksiksiz sağlayarak, sıfır açık hata ve tam zamanında teslimat ile tamamlamış bulunmaktayız. Rol rotasyonunun başarıyla uygulandığı bu dönemde; parametreli ve deterministik simülasyon motoru (`src/simulasyon.py`), veri şeması ve sözlüğü (`docs/veri-sozlugu.md`), 3 parçalı görselleştirme seti (`visuals/`) ve 5 ana metriği kapsayan analiz dokümantasyonu (`docs/analiz-g2.md`) başarıyla teslim edilmiştir. Süreç boyunca karşılaşılan teknik kısıtlar (CLI parametre eksikliği ve kanal seçim kısıtı) takım içi etkin geri bildirim, hata kartları ve PR inceleme döngüleriyle çözülmüş; repo `gorev2-final` etiketiyle sürümleştirilmiş ve proje panosunda açık kart bırakılmamıştır. Ekip olarak Görev 3'te partner şirketimiz Grup B ile gerçekleştirilecek B2B veri entegrasyonuna hazır durumdayız.

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

---

## 3. Sayılarla Dönem (Süreç KPI'ları)

Dönem verileri GitHub CLI (`gh api`, `gh issue`, `gh pr`) ve yerel `git` analiz betikleriyle derlenmiştir:

| KPI Göstergesi | Görev 2 Dönemi | Depo Geneli (Tüm Dönem) | Not / Açıklama |
|---|:---:|:---:|---|
| **Açılan Issue Sayısı** | 11 | 47 | Görev 2 kapsamındaki tüm rol, hata ve koordinasyon kartları |
| **Kapatılan Issue Sayısı** | 11 | 47 | Depoda 5 Kasım itibarıyla **0 açık Issue** bırakılmıştır |
| **Merge Edilen PR Sayısı** | 12 | 15 | PR #46–#51, #54–#56, #59–#61 (Hafta 5 kuralı: main'e yalnızca PR ile giriş) |
| **Açık Kalan PR Sayısı** | 0 | 0 | Tüm açılan PR'lar incelenmiş ve birleştirilmiştir |
| **Ortalama İlk İnceleme/Yorum Süresi** | ~10.9 saat (654.0 dk) | ~10.9 saat | İnceleme yorumu alan PR'lar (en hızlı: PR #49 - 37 dk; PR #59 - 225 dk) |
| **Geciken / Son Tarihi Geçen İş Sayısı** | **0** | **0** | Tüm kabul kriterleri planlanan sprint takviminde tamamlanmıştır |

### Üye Bazında Dağılım

| Üye | Görev 2 Rolü | G2 Commit | Toplam Commit | G2 Kapatılan / Sorumlu Olunan Ana İşler |
|---|---|:---:|:---:|---|
| **Dilara Başer** (@baserdilara94-ui) | PM (Lider - sabit) | 7 | 29 | Koordinasyon, PR #46, `report-w05.md`, #57, #58, #62, release |
| **Tuana Gürkan** (@tuanagurkan77) | DQ (Analiz & Kalite) | 12 | 26 | #40 (şema), #43 (analiz), #44 (test), PR inceleme/onayları |
| **Nuri Enes Seyhan** (@seyhannurienes-afk) | BE (Simülasyon) | 3 | 20 | #41 (simülasyon), #53 (kanal kısıtı), 7 birim test |
| **Özge Nur Doğu** (@Ozge-nur) | FE (Görselleştirici) | 5 | 14 | #42 (3 grafik seti), #52 (CLI desteği), taslaklar |
| **Ceren Doğrul** (@cerendogrul120-byte) | Junior (Ön İnceleme) | 2 | 20 | #45 (ön inceleme & determinizm), #58 otomasyon önerisi |

---

## 4. Tıkananlar ve Çözümleri

Sprint sürecinde tespit edilen teknik engeller gizlenmemiş, ilgili GitHub Issue'ları açılarak şeffaf bir şekilde yönetilmiş ve çözülmüştür:

1. **FE Sabit Yol Bağımlılığı (Hata Kartı [#52](https://github.com/MAKU-VBA-GBT-II/group-g/issues/52)):**
   - *Engel:* FE görsel üretim betiği `src/grafik_uret.py`, sabit bir CSV yoluna bağlı çalışıyordu ve komut satırından parametre kabul etmiyordu. Bu durum betiğin farklı test veri setleriyle çalıştırılmasını zorlaştırıyordu.
   - *Çözüm:* DQ'nun entegrasyon testlerinde açtığı hata kartı doğrultusunda FE tarafından betiğe `--veri` ve `--cikti_dizini` CLI argümanları eklendi ([PR #55](https://github.com/MAKU-VBA-GBT-II/group-g/pull/55)) ve sorun giderildi.
2. **BE Kanal Seçim Kısıtı (Hata Kartı [#53](https://github.com/MAKU-VBA-GBT-II/group-g/issues/53)):**
   - *Engel:* `kampanya_sayisi` 5'ten küçük seçildiğinde simülatör varsayılan olarak yalnızca listenin ilk N kanalını üretiyor, kullanıcının istediği kanalları belirlemesine olanak tanımıyordu.
   - *Çözüm:* BE tarafından simülatöre `--kanallar` parametresi, geçersiz veya mükerrer kanal kontrolleri ve `tests/test_simulasyon.py` regresyon birim testleri (7 senaryo) eklendi ([PR #59](https://github.com/MAKU-VBA-GBT-II/group-g/pull/59)).
3. **Junior Ön İnceleme Yol Belirsizliği (İnceleme Kartı [#57](https://github.com/MAKU-VBA-GBT-II/group-g/issues/57)):**
   - *Engel:* Junior üyenin ilk incelemesinde Görev 1 dosya adlarıyla Görev 2 dosya adları arasında karışıklık yaşandı.
   - *Çözüm:* PM tarafından repo genelindeki dosya yapısı `main` dalında teyit edildi, isimlendirme standartları netleştirilerek kart kapatıldı.

---

## 5. Kim Ne Yaptı (Ekip Geri Bildirimleri — Issue #62 Referanslı)

Duyuru 7 (Bölüm 2) uyarınca Issue [#62](https://github.com/MAKU-VBA-GBT-II/group-g/issues/62) altında tüm ekip üyelerinden toplanan olgusal beyanlar aşağıda özetlenmiştir:

| Üye | Rolü | Ne Teslim Etti? (Kanıtlı) | Neye Takıldı ve Nasıl Aştı? | Görev 3 Hedefi / Önerisi |
|---|---|---|---|---|
| **Dilara Başer** (@baserdilara94-ui) | PM (Lider) | PR #46, #60, #61, `report-w05.md`, `gorev2-final` release, #57 ve #58 inceleme ve kapanışları, #62 veri toplama | Rol rotasyonu sonrası devir zinciri koordinasyonu; `AGENTS.md` ve açık iletişim ile devir adımları netleştirildi | Grup B ile B2B sözleşme standartlarını baştan netleştirmek; devir teslim kontrollerini CI ile otomatize etmek |
| **Nuri Enes Seyhan** (@seyhannurienes-afk) | BE (Simülasyon) | PR #49 (`da6f979`), PR #59 (`3782821`), `src/simulasyon.py`, `kampanya-simulasyon-g2.csv`, `be-simulasyon` skill'i, 7 regresyon birim testi (#41, #53) | Kampanya sayısı azaldığında ilk kanalların seçilmesi kısıtı; `--kanallar` seçeneği ve regresyon testleri eklenerek aşıldı | Simülasyonun B2B analiz ihtiyaçlarına uyumu; parametre değişikliklerini CI regresyon testleriyle erken doğrulamak |
| **Tuana Gürkan** (@tuanagurkan77) | DQ (Analiz & Kalite) | PR #47 (`c466124`), PR #48 (`abac5de`), PR #51 (`e354786`), PR #54 (`023c139`), `veri-sozlugu.md`, `test-cases.md`, `test-log.md` (TC-1–TC-8), `analiz_g2.py`, `requirements.md`, `user-manual.md` (#40, #43, #44) | FE betiğinin CLI almaması ve BE kanal kısıtı; doğrudan onay yerine #52 ve #53 hata kartları açılarak regresyonla doğrulandı | Kalite ve determinizm test senaryolarının GitHub Actions (CI) üzerinde her PR'da otomatik koşulması |
| **Özge Nur Doğu** (@Ozge-nur) | FE (Görselleştirici) | PR #50 (`a50e80f`), PR #55 (`195f56b`), `src/grafik_uret.py`, 3 adet 200 DPI PNG (`visuals/`), `fe-gorsel` skill'i (#42, #52) | Veri henüz birleşmeden grafik geliştirme ihtiyacı; taslak çizip G1 yedekli iskelet kod yazıldı, veri birleşince main dallanıp doğrulandı | Partner şirketle B2B veri sözleşmesini (alanlar, biçimler) yazılı netleştirmek ve teslim öncesi şema kontrolü |
| **Ceren Doğrul** (@cerendogrul120-byte) | Junior (Ön İnceleme) | PR #56 (`0ccdcb3`), `test-log.md` ön inceleme tablosu, tohum determinizm denemeleri, `junior-kontrol` skill'i (#45), #58 otomasyon önerisi | İlk kontrolde G1 dosyalarıyla ilerleme hatası; G2 teslimi ve DQ onayı beklenerek gerçek dosyalarla test tekrarlandı | Şema, yol ve determinizm kontrollerinin tek bir otomatik CI ön kontrol adımında toplanması |

---

## 6. Dersler (Retrospektif)

1. **Arayüz ve Sözleşme Önceliği (Contract-First Design):** FE ve DQ geliştiricilerinin BE verisi `main` dalına girmeden çalışmalarına başlayabilmesi için veri şemasının en başta dondurulması gerektiği görülmüştür. Özge Nur Doğu'nun mockup ve fallback veri yapısıyla ilerlemesi takvim gecikmelerini önlemiştir.
2. **Hata Kartı Odaklı Süreç Disiplini:** Tuana Gürkan'ın test sırasında bulduğu eksiklikleri kendisi kodlamak yerine #52 ve #53 hata kayıtları açarak ilgili uzmanlara devretmesi, izlenebilirliği sağlamış ve kod sahipliğini korumuştur.
3. **Otomasyon ve CI İhtiyacı:** Ekip üyelerinin neredeyse tamamı, determinizm ve şema uyum testlerinin yerel makineler yerine GitHub Actions üzerinden otomatik koşulması gerektiğinde birleşmiştir.

---

## 7. Görev 3 Hazırlığı (B2B Veri Değişimi Planı)

- **Partner Şirket Eşleşmesi:** Duyuru 5 uyarınca Grubumuz (PrimeBee — Grup G), **Grup B** ile eşleşmiştir.
- **Veri Değişimi Kapsamı:** PrimeBee dijital pazarlama simülasyonundan elde edilen performans çıktıları (kanal bazlı harcama, gelir, ROAS ve dönüşüm metrikleri), Grup B'nin ihtiyaç duyduğu veri formatına dönüştürülecek ve onlardan gelecek iş verileri analiz hattımıza dahil edilecektir.
- **Protokol ve Standartlar:** Görev 3 başında iki takımın PM ve DQ liderleri arasında ortak bir `docs/b2b-sozlesme.md` hazırlanacak; tarih formatları (ISO 8601), para birimleri, numerik hassasiyet ve UTF-8 karakter seti bağlayıcı olarak kararlaştırılacaktır.
- **Entegrasyon Doğrulama:** Gelen verilerin geçerliliği için önleyici DQ doğrulama testleri yazılacak ve B2B test döngüsü uygulanacaktır.

---

## Araç ve Model Bilgisi (Prompt Özeti)

Bu dönem raporu, PrimeBee ekibinin `pm-rapor` skill'i ([`skills/pm-rapor/SKILL.md`](skills/pm-rapor/SKILL.md)) yönergeleri ve dersin [Duyuru 7](https://github.com/MAKU-VBA-GBT-II/ders/blob/main/Duyuru-7_2026-11-01.md) şablonu esas alınarak **Antigravity (Gemini 3.8 Flash)** asistanı ile üretilmiştir. Rapordaki tüm sayılar ve iddialar GitHub API (`gh api`), Issue/PR kayıtları ve Git geçmişi (`git log`) üzerinden olgusal olarak doğrulanmıştır.
