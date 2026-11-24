---
name: pm-rapor
description: "PrimeBee (Grup G - Dijital Pazarlama) haftalık sprint süreçlerini GitHub kayıtlarından (Issue, PR, commit, test günlüğü) derleyerek standart sprint raporu (reports/report-wXX.md) üretir."
---

# PrimeBee Sprint Raporlama Sistemi (pm-rapor)

## Amaç
Bu skill, PrimeBee (Grup G — Dijital Pazarlama) ekibinin haftalık sprint süreçlerini, ekip içi devir teslim zincirini ve geliştirme adımlarını GitHub üzerindeki somut kanıtlarla (Issue kayıtları, PR incelemeleri, commit özetleri ve test logları) belgeleyerek `reports/report-wXX.md` dosyasını üretir veya günceller. Raporlanan tüm bilgiler doğrulanabilir GitHub verilerine dayanır; tahmini veya kanıtsız bilgi içermez.

## Girdi ve Çıktı

### Girdiler
- **Hafta ve Dönem Bilgisi:** Hafta numarası (örn. `03`, `04`, `05`), sprint başlangıç ve bitiş tarihleri.
- **Depo ve İzler:** `MAKU-VBA-GBT-II/group-g` deposu altındaki açık/kapalı Issue'lar, PR'lar ve `git log` geçmişi.
- **Ekip Rolleri ve Görev Dağılımı:** `AGENTS.md` dosyasındaki güncel rol rotasyonu ve sorumluluk matrisi.
- **Devir Teslim Kanıtları:** BE (Simülasyon/Veri) → DQ (Analiz/Şema) → FE (Görselleştirme) devir teslim yorumları.
- **Test ve Hata Kayıtları:** `tests/test-log.md` dosyası ve açılan hata/iyileştirme kartları.

### Çıktı
- `reports/report-wXX.md` (Markdown formatında haftalık sprint raporu).

---

## Adım Adım İşleyiş

1. **Sprint Kapsamını Belirle:** İlgili haftaya ait planlanan tüm Issue'ları listele; numara, başlık, sorumlu üye ve kabul kriterlerini kaydet.
2. **Çıktıları ve Kanıtları Denetle:** 
   - Kapatılan her Issue için kanıt yorumunu (commit hash, dosya yolu, ekran görüntüsü veya test sonucu) doğrula.
   - PR ile birleştirilen işlerde DQ/akran inceleme onayının (`Approved`) bulunup bulunmadığını kontrol et.
3. **Devir Teslim Zincirini Doğrula:**
   - BE'den DQ ve FE'ye veri aktarımı ("Veri hazır — commit ...") yapıldı mı?
   - DQ'dan FE'ye analiz ve sözlük doğrulaması ("Analiz doğrulandı...") tamamlandı mı?
   - Zincirde gecikme veya tıkanma olup olmadığını tespit et.
4. **Teknik Risk ve Engelleri Belgele:** Yaşanan sürüm uyumsuzlukları, veri formatı uyuşmazlıkları, geciken onaylar veya kod çakışmalarını şeffaf şekilde listele.
5. **Bireysel Katkıları Özetle:** Her üyenin (PM, BE, DQ, FE, Junior) hafta boyunca gerçekleştirdiği commit sayısını, kapattığı Issue'ları ve incelediği PR'ları tabloya aktar.
6. **Raporu Üret ve Commit Et:** Derlenen bilgileri aşağıdaki şablona uygun olarak `reports/report-wXX.md` dosyasına yaz. Commit mesajı: `Hafta XX sprint raporu güncellendi`.

---

## Rapor Şablonu

```markdown
# Sprint Raporu — Hafta XX (GG.AA–GG.AA.YYYY)

**Şirket:** PrimeBee (Grup G — Dijital Pazarlama)  
**Proje Lideri (PM):** Dilara Başer  
**Tarih:** GG.AA.YYYY  

---

## 1. Planlanan Görevler
| Issue | Görev Tanımı | Sorumlu | Kabul Kriteri | Durum |
|:---:|:---|:---:|:---|:---:|
| #XX | ... | @kullanici | ... | Tamamlandı / Devam Ediyor |

## 2. Devir Teslim Zinciri ve İş Akışı
- **BE → DQ / FE (Veri Devri):** [Yapıldı / Beklemede] — *Kanıt: Issue #... / Commit ...*
- **DQ → FE (Şema ve Analiz Onayı):** [Yapıldı / Beklemede] — *Kanıt: Issue #... / PR #...*
- **Junior Ön Kontrolü:** [Tamamlandı / Yapılmadı] — *Kanıt: Issue #...*

## 3. Karşılaşılan Engeller ve Çözümler
- **Teknik Aksaklıklar:** ...
- **Süreç İyileştirmeleri:** ...

## 4. Ekip Katkı Matrisi
| Üye | Rol | Commit Sayısı | İncelediği PR / Kapattığı Issue |
|:---|:---:|:---:|:---|
| Dilara Başer | PM | ... | ... |
| Nuri Enes Seyhan | BE | ... | ... |
| Ayşe Tuana Gürkan | DQ | ... | ... |
| Özge Nur Doğu | FE | ... | ... |
| Ceren Doğrul | Junior | ... | ... |

## 5. Gelecek Sprint Hedefleri
- ...
```

---

## Nasıl Çalıştırılır

Ajana (Claude, Codex, Antigravity vb.) şu talimat verilir:
> *"pm-rapor skill'ini kullanarak Hafta XX için reports/report-wXX.md dosyasını GitHub commit ve issue kayıtlarına göre derle."*

Ajan, GitHub CLI (`gh`) veya `git log` araçlarını kullanarak depodaki gerçek izleri okur ve raporu şablona uygun olarak oluşturur. Kullanılan model ve komut özeti ilgili sprint kapanış Issue'suna eklenir.
