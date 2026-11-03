# Kampanya Veri Kalitesi Test Sonuç Günlüğü (test-log.md)

**Şirket:** PrimeBee - Grup G (Dijital Pazarlama)  
**Referans:** `tests/test-cases.md`, `docs/veri-sozlugu.md`  
**Sorumlu (Görev 2 DQ):** Tuana GÜRKAN  
**İlgili Issue:** [#44 (G2-test)](https://github.com/MAKU-VBA-GBT-II/group-g/issues/44)  

---

## Hafta 6 Tam Test Koşumu — 2026-11-02 (Görev 2)

Görev 2 mini ürününün `main` dalındaki tüm bileşenleri (`data/kampanya-simulasyon-g2.csv`, `src/simulasyon.py`, `src/analiz_g2.py`, `src/grafik_uret.py`) üzerinde `tests/test-cases.md` dosyasındaki 8 kabul senaryosu bağımsız olarak koşulmuş ve doğrulanmıştır.

| No | Senaryo | Test Tarihi | Test Eden | Beklenen Sonuç | Gerçekleşen Sonuç | Durum | İlgili Issue / Not |
|---:|---|---|---|---|---|---|---|
| **TC-1** | Dosya Varlığı ve Erişilebilirlik | 2026-11-02 | Tuana Gürkan (DQ) | `data/kampanya-simulasyon-g2.csv` mevcut, okunabilir ve UTF-8 olmalı. | Dosya mevcut, 261 satır (1 başlık + 260 veri), UTF-8 kodlama hatasız okundu. | **Geçti** | PR #49 |
| **TC-2** | Varsayılan Boyut ve Satır Sayısı | 2026-11-02 | Tuana Gürkan (DQ) | Tam olarak 260 veri satırı ($52 \times 5$). | Başlık hariç tam 260 satır doğrulandı. Eksik/fazla satır yok. | **Geçti** | PR #49 |
| **TC-3** | Sütun Adları, Sırası ve Veri Tipleri | 2026-11-02 | Tuana Gürkan (DQ) | Şemadaki 8 sütun sırayla bulunmalı; boş hücre (NaN/NULL) olmamalı. | 8 sütun tam eşleşti (`kampanya_id`, `tarih`, `kanal`, `gosterim`, `tiklama`, `donusum`, `harcama_tl`, `gelir_tl`). Boş hücre sayısı 0. | **Geçti** | PR #49 |
| **TC-4** | Değer Aralıkları, Mantıksal Kurallar ve Biçim | 2026-11-02 | Tuana Gürkan (DQ) | $donusum \le tiklama \le gosterim$, harcama > 0, 2 ondalıklı para formatı ve Pazartesi tarihleri. | 260 satırın tamamında kural ihlali 0; tüm tutarlar tam 2 ondalıklı; tarihler 52 Pazartesi ile uyumlu. | **Geçti** | `src/analiz_g2.py` |
| **TC-5** | Kanal Kategori Değerleri ve Dağılım Eşitliği | 2026-11-02 | Tuana Gürkan (DQ) | 5 kanalın her biri için tam 52 kayıt bulunmalı. | Google Ads (52), Meta Ads (52), TikTok Ads (52), E-posta (52), SEO (52). Beklenmeyen kategori yok. | **Geçti** | PR #49 |
| **TC-6** | Parametre Davranışı (Dinamik Satır Üretimi) | 2026-11-02 | Tuana Gürkan (DQ) | Farklı parametrelerde satır sayısı dinamik üretilmeli (10x3=30 satır, 26x5=130 satır). | a) `--hafta_sayisi 10 --kampanya_sayisi 3` -> tam 30 satır üretildi.<br>b) `--hafta_sayisi 26 --kampanya_sayisi 5` -> tam 130 satır üretildi. | **Geçti** | `src/simulasyon.py` |
| **TC-7** | Sabit Tohum Determinizmi (Tekrarlanabilirlik) | 2026-11-02 | Tuana Gürkan (DQ) | Sabit `tohum=42` ile üretilen iki CSV dosyasının hash'leri birebir aynı olmalı. | İki bağımsız üretim sonucunda SHA-256 hash'i (`10459cdf5428...`) bayt seviyesinde tam eşleşti. | **Geçti** | `src/simulasyon.py` |
| **TC-8** | Hata Yönetimi ve Parametre Doğrulama (Sınır Testi) | 2026-11-02 | Tuana Gürkan (DQ) | Geçersiz parametrelerde (negatif tohum, 0 hafta, Pazartesi olmayan tarih) açıklayıcı ValueError verilmeli. | `--tohum -5` -> ValueError (tohum sıfır veya daha büyük olmalıdır)<br>`--hafta_sayisi 0` -> ValueError (hafta_sayisi 1 ile 104 arasında olmalıdır)<br>`--baslangic_tarihi 2025-10-07` -> ValueError (baslangic_tarihi bir Pazartesi olmalıdır). | **Geçti** | `src/simulasyon.py` |

---

## Issue #53 Kanal Seçimi Regresyon Koşumu — 2026-11-03 (BE)

| Kontrol | Girdi | Gerçekleşen Sonuç | Durum |
|---|---|---|---|
| Belirli kanalların seçimi | `--hafta_sayisi 2 --kanallar "E-posta" SEO` | 4 satır üretildi; yalnızca `E-posta` ve `SEO` çıktı, her hafta kanal sırası korundu. | **Geçti** |
| Eski adet parametresi | `--hafta_sayisi 2 --kampanya_sayisi 2` | 4 satır üretildi; eski kullanım ilk iki kanalı üretmeye devam etti. | **Geçti** |
| Kanal adedi uyumsuzluğu | `--kampanya_sayisi 1 --kanallar "E-posta" SEO` | Açıklayıcı `ValueError` ile reddedildi. | **Geçti** |
| Varsayılan veri geriye uyumluluğu | Varsayılan tohum ve parametrelerle iki üretim | 260 satır ve mevcut varsayılan CSV ile aynı SHA-256 üretildi. | **Geçti** |

İlgili hata kaydı: [#53](https://github.com/MAKU-VBA-GBT-II/group-g/issues/53). Testler `fix/channel-selection` dalındaki değişiklik üzerinde çalıştırılmıştır.

---

## Junior Ön İnceleme — 2026-11-03 (Görev 2)

| Kontrol | Girdi | Gerçekleşen Sonuç | Durum / Not |
|---|---|---|---|
| Teslim edilen CSV | `data/kampanya-simulasyon-g2.csv` | 260 veri satırı, sözlükle aynı 8 sütun; 5 kanalın her birinde 52 satır. Çalışma dosyasının git'teki içerikle aynı olduğu doğrulandı. | **Geçti** |
| Varsayılan simülasyon | `tohum=42`, `hafta_sayisi=52`, `kampanya_sayisi=5`, `baslangic_tarihi=2025-10-06` | Geçici çıktı dosyasında 260 satır üretildi ve betik içi doğrulamadan geçti. | **Geçti** |
| Alternatif parametreler | `tohum=7`, `hafta_sayisi=10`, `kampanya_sayisi=3`, `baslangic_tarihi=2026-11-02` | Geçici çıktı dosyasında 30 satır üretildi; başlangıç tarihi Pazartesi olarak kabul edildi. Üç kampanya sayısı ilk üç sabit kanalı üretti. | **Geçti; kanal seçimi kısıtı [#53](https://github.com/MAKU-VBA-GBT-II/group-g/issues/53) kapsamında açık.** |
| Tekrarlanabilirlik | Aynı alternatif parametrelerle iki üretim; ardından `tohum=123` | Aynı tohumlu dosyaların SHA-256 değerleri eşleşti; farklı tohumlu dosyanın hash'i farklı çıktı. | **Geçti** |

Deneme çıktıları sistem geçici dizininde tutuldu; depo içindeki varsayılan G2 CSV'sine yazılmadı.

---

## Hafta 6 Test Turunda Tespit Edilen Hatalar ve Açılan Issue'lar

Hafta 6 kapsamlı sistem testi sırasında tespit edilen işlevsel kısıt ve hata kayıtları:

1. **Hata 1 (Issue [#52](https://github.com/MAKU-VBA-GBT-II/group-g/issues/52)):** `fix(fe): src/grafik_uret.py CLI parametre desteği eksikliği ve sabit dosya yolu bağımlılığı`  
   - **Kategori:** `bug`  
   - **Atanan:** @Ozge-nur (FE)  
   - **Açıklama:** Simülasyon betiği esnek CLI argümanları alabilirken, görselleştirme betiğinin (`src/grafik_uret.py`) parametre desteği bulunmamaktadır; farklı veri yolları argüman olarak verilememektedir.
2. **Hata 2 (Issue [#53](https://github.com/MAKU-VBA-GBT-II/group-g/issues/53)):** `fix(be): src/simulasyon.py kampanya_sayisi < 5 durumunda sabit kanal seçimi kısıtı`  
   - **Kategori:** `bug`  
   - **Atanan:** @seyhannurienes-afk (BE)  
   - **Açıklama:** `kampanya_sayisi < 5` verildiğinde kanal seçimi Python sözlük sırasındaki ilk N kanalla sınırlıdır; kullanıcının özel kanal seçimi yapmasına izin verilmemektedir.

---

## Arşiv: Hafta 4 Tam Test Koşumu — 2026-10-24 (Görev 1)

| No | Senaryo | Test Tarihi | Test Eden | Beklenen Sonuç | Gerçekleşen Sonuç | Durum |
|---:|---|---|---|---|---|---|
| 1 | Dosya var mı? | 2026-10-24 | Nuri Enes Seyhan (DQ) | Dosya mevcut ve okunabilir olmalı. | `data/kampanya-performans.csv` mevcut; UTF-8 olarak açılıp okunabildi. | Geçti |
| 2 | Veri satırı sayısı | 2026-10-24 | Nuri Enes Seyhan (DQ) | En az 100 veri satırı; v3 sözlüğüne göre tam 260 veri satırı olmalı. | Başlık hariç 260 veri satırı bulundu. | Geçti |
| 3 | Sütun adları ve sırası | 2026-10-24 | Nuri Enes Seyhan (DQ) | Sözlükte belirtilen 8 sütun aynı ad ve sırada bulunmalı. | 8 sütun eşleşti: `kampanya_id`, `tarih`, `kanal`, `gosterim`, `tiklama`, `donusum`, `harcama_tl`, `gelir_tl`. | Geçti |
| 4 | Tipler, biçimler ve değer aralıkları | 2026-10-24 | Nuri Enes Seyhan (DQ) | Tüm kayıtlar v3 tip, biçim, tarih, kimlik ve değer aralıklarına uymalı; tıklama gösterimi, dönüşüm tıklamayı aşmamalı. | 260 kaydın tamamında benzersiz `K001`–`K260` kimlikleri, Pazartesi tarihleri (`2025-10-06`–`2026-09-28`), tam iki ondalıklı tutarlar, sayısal aralıklar ve tıklama/dönüşüm ilişkileri doğrulandı. | Geçti |
| 5 | Kanal kategori değerleri | 2026-10-24 | Nuri Enes Seyhan (DQ) | Yalnızca izin verilen 5 kanal bulunmalı; her kanalda 52 kayıt olmalı. | Google Ads (52), Meta Ads (52), TikTok Ads (52), E-posta (52), SEO (52); beklenmeyen/eksik kategori yok. | Geçti |

---

## Arşiv: Hafta 3 Test Sonuçları (Görev 1)

| Senaryo No | Senaryo | Test Tarihi | Test Eden | Beklenen Sonuç | Gerçekleşen Sonuç | Durum |
|---:|---|---|---|---|---|---|
| 2 | Veri satırı sayısı | 2026-10-18 | Nuri Enes Seyhan (DQ) | En az 100 veri satırı; v2 sözlüğüne göre hedef 260 veri satırı olmalı. | 260 veri satırı (başlıkla 261 satır). | Geçti |
| 5 | Kanal kategori değerleri | 2026-10-18 | Ceren Doğrul (Junior) | Yalnızca izin verilen 5 kanal bulunmalı; her kanalda 52 kayıt olmalı. | Google Ads (52), Meta Ads (52), TikTok Ads (52), E-posta (52), SEO (52); toplam 260 kayıt. | Geçti |
