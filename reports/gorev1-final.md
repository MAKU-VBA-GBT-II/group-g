# Release: gorev1-final — PrimeBee Dijital Pazarlama Mini Veri Hattı

**Sürüm Etiketi:** `gorev1-final`  
**Şirket:** PrimeBee (Grup G) — Dijital Pazarlama  
**Proje Yöneticisi (PM):** Dilara Başer  
**Teslim Tarihi:** 27 Ekim 2026  
**Depo:** `MAKU-VBA-GBT-II/group-g`  

---

## 1. Yönetici Özeti (Executive Summary)

Görev 1 (Hafta 3–4) kapsamında, PrimeBee dijital pazarlama şirketi için uçtan uca tekrarlanabilir bir **Mini Veri Hattı (Data Pipeline)** başarıyla kurulmuş, test edilmiş ve belgelenmiştir. 

Süreç boyunca backend veri üretiminden veri kalitesi doğrulamasına, analitik modellemeden görselleştirmeye kadar tüm devir teslim adımları GitHub Issue'ları, kanıt yorumları ve commit izleriyle doğrulanmıştır. Hat üzerinde 5 farklı dijital pazarlama kanalı (Google Ads, Meta Ads, TikTok Ads, SEO, E-posta) üzerinden 52 haftalık (2025-10-06 – 2026-09-28) toplam **260 kampanya-hafta** kaydı simüle edilmiş; 10,54 milyon TL'lik hacim analitik olarak incelenmiştir.

---

## 2. Mini Veri Hattı Mimarisi ve Devir Teslim Zinciri

Veri hattı, yapay zekâ ajan skill'leri ile güçlendirilmiş 5 aşamalı devir teslim zinciriyle işletilmiştir:

```
[BE: Veri Simülasyonu] ──(v3 CSV + Şema)──> [DQ: Veri Kalitesi & Analiz]
                                                   │
          ┌────────────────────────────────────────┴────────────────────────────────────────┐
          ▼                                                                                 ▼
[FE: Görselleştirme] ──(Zaman Serisi & Kırılım)──> [Junior & DQ: Doğrulama] ──(Test Log)──> [PM: Sprint Raporu & Release]
```

1. **BE (Backend — Özge Nur Doğu):**
   - **Veri Üretimi:** `src/kampanya_simulasyon.py` betiği ile sabit tohumlu (`SEED = 42`) 260 satırlık sentetik veri seti (`data/kampanya-performans.csv`) üretildi.
   - **Veri Sözlüğü:** `docs/veri-sozlugu-g1.md` (v3 şeması) altında 8 alan, tip tanımları, mantıksal aralıklar ve simülasyon parametreleri eksiksiz belgelendi.
   - **Devir Teslim:** Issue #10 üzerinden DQ ve FE'ye kanıtlı devir teslim yorumları yazıldı.

2. **DQ (Veri Analisti & Kalite — Nuri Enes Seyhan):**
   - **Analitik Modelleme:** `src/analiz_g1.py` betiği çalıştırılarak `Decimal` hassasiyetinde 6 metrik ve 52 haftalık zaman serisi trendi hesaplandı (`docs/analiz-g1.md`).
   - **Formül Standardizasyonu:** Birleşik ROAS ($\sum \text{Gelir} / \sum \text{Harcama}$) formülü tanımlanarak FE ekibine devredildi.
   - **Nihai Onay:** Issue #11 ve #23 altında şema v3 ve 260 satırlık veri incelenerek resmi kabul onayı verildi.

3. **FE (Frontend / Görselleştirici — Tuana Gürkan):**
   - **Grafik Üretimi:** `src/generate_visuals.py` betiği ile analizle tam uyumlu 2 adet yüksek çözünürlüklü PNG grafik üretildi:
     - `visuals/gelir-zaman-serisi.png`: 52 haftalık toplam gelir trendi ve haftalık ortalama kesikli referans çizgisi (202.722,56 TL).
     - `visuals/kanal-kirilim.png`: Kanalların toplam gelir payları ve birleşik ROAS barları.
   - **Tasarım:** Issue #12'ye taslak ekran görüntüleri eklendi, DQ revize talepleri doğrultusunda dinamik etiketleme yapıldı.

4. **Junior & DQ Doğrulama (Ceren Doğrul & Nuri Enes Seyhan):**
   - **Test Tasarımı:** `tests/test-cases.md` dosyasında TC-01'den TC-09'a kadar 9 kapsamlı test senaryosu yapılandırıldı.
   - **Test Koşumu:** `tests/test-log.md` üzerinde tüm test adımları gerçek veriyle işletilerek tarihli olarak belgelendi (Tüm senaryolar: **GEÇTİ**).
   - **İyileştirme Yönetimi:** DQ tarafından açılan #37 (Haftalık kanal kapsamı) ve #38 (Şema ayrıştırma) geliştirme kartları tamamlandı.

5. **PM (Proje Yöneticisi — Dilara Başer):**
   - **Pano Hijyeni:** 39 adet Issue ve Pull Request incelenerek tüm süreçler kapatıldı; panoda 0 açık kart bırakıldı.
   - **Sprint Raporlaması:** `reports/report-w03.md` ve `reports/report-w04.md` GitHub izlerine dayalı olarak şablonla hazırlandı.
   - **Mühürleme:** Görev 1 final teslimatı `gorev1-final` tag ve release'i ile tamamlandı.

---

## 3. Temel Metrikler ve Analiz Bulguları

| Metrik | Değer | Açıklama |
|---|---|---|
| **Toplam Gelir** | **10.541.572,97 TL** | 52 haftalık dönemdeki toplam ciro |
| **Toplam Harcama** | **1.891.414,54 TL** | 5 kanal üzerinden yapılan toplam reklam harcaması |
| **Birleşik ROAS** | **5,57x** | Toplam Gelir / Toplam Harcama oranı |
| **Haftalık Ort. Gelir** | **202.722,56 TL** | 5 kanalın haftalık ortalama gelir toplamı |
| **Ortalama Kampanya ROAS** | **17,43x** | 260 kaydın eşit ağırlıklı aritmetik ortalaması |

### Kanal Kırılımı ve Verimlilik Sıralaması

| Kanal | Harcama (TL) | Gelir (TL) | Gelir Payı | Birleşik ROAS | Verimlilik Sırası |
|---|---:|---:|---:|---:|:---:|
| **E-posta** | 34.050,15 | 1.549.173,49 | %14,70 | **45,50x** | 1 |
| **SEO** | 92.331,52 | 2.147.542,59 | %20,37 | **23,26x** | 2 |
| **Google Ads** | 1.037.415,58 | 4.365.311,40 | **%41,41** | **4,21x** | 3 |
| **Meta Ads** | 439.779,86 | 1.650.586,71 | %15,66 | **3,75x** | 4 |
| **TikTok Ads** | 287.837,43 | 828.958,78 | %7,86 | **2,88x** | 5 |
| **TOPLAM** | **1.891.414,54** | **10.541.572,97** | **%100,00** | **5,57x** | — |

### Stratejik Bulgular ve Öneriler
1. **Hacim Lideri:** Google Ads toplam gelirin %41,41'ini üreterek ana gelir motoru olmuştur; 4,21x birleşik ROAS ile karlı seviyededir.
2. **Yüksek Verimlilik Fırsatı:** E-posta (45,50x) ve SEO (23,26x) olağanüstü yüksek yatırım getirisi üretmiştir. Düşük harcama bütçelerine karşılık yüksek dönüşüm sağlamaktadır.
3. **Eylem Planı:** E-posta otomasyonları ve SEO içerik bütçelerinde kademeli/kontrollü bir pilot bütçe artışı uygulanmalı; TikTok Ads kanalında ise kreatif optimizasyonu yapılmadan bütçe artırılmamalıdır.

---

## 4. Kalite Güvence ve Doğrulama (Test Özeti)

Tüm senaryolar `tests/test-log.md` kütüğünde kayıt altına alınmıştır:

- **TC-01 (Satır Sayısı):** 260 satır tam sağlandı.
- **TC-02 (Tarih Sınırları & Adım):** 2025-10-06 – 2026-09-28 (52 hafta, her Pazartesi) doğrulandı.
- **TC-03 (Metrik Formülü):** Birleşik ROAS formülü test edildi, tutarlılık onaylandı.
- **TC-04–TC-08 (Alan & Şema Doğrulama):** Tıklama $\le$ Gösterim, Dönüşüm $\le$ Tıklama, 2 ondalıklı para alanları doğrulandı.
- **TC-09 (Kanal-Hafta Kapsamı):** Her hafta 5 kanalın benzersiz varlığı (52 × 5 = 260) eksiksiz doğrulandı.

---

## 5. Teslim Edilen Depo Varlıkları (Deliverables)

- **Veri ve Şema:** `data/kampanya-performans.csv`, `docs/veri-sozlugu-g1.md`
- **Analiz ve Kod:** `docs/analiz-g1.md`, `src/analiz_g1.py`, `src/kampanya_simulasyon.py`
- **Görseller:** `visuals/gelir-zaman-serisi.png`, `visuals/kanal-kirilim.png`, `src/generate_visuals.py`
- **Test Belgeleri:** `tests/test-cases.md`, `tests/test-log.md`
- **Sprint ve Yan Görev Raporları:** `reports/report-w03.md`, `reports/report-w04.md`, `reports/Yan-görev-1/` (5 açık kaynak keşif raporu)
- **Ajan Skill Envanteri:** `AGENTS.md` + 5 adet `skills/*/SKILL.md` (`pm-rapor`, `be-veri`, `dq-analiz`, `fe-gorsel`, `junior-kontrol`)

---

## 6. Görev 2 Hazırlıkları (Next Steps)

1. **Pull Request Zorunluluğu:** Hafta 5 itibarıyla `main` korumaya alınacak; tüm teslimatlar feature branch + PR + DQ onayı ile birleştirilecektir.
2. **Rol Rotasyonu:** Dönem planı §1.3 uyarınca şirket içi roller devredilecek ve skill sahiplikleri güncellenecektir.
3. **Mini Ürün Geliştirme:** PrimeBee için parametreli simülasyon ve etkileşimli ürün mimarisine geçilecektir.
