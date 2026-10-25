# AGENTS.md — PrimeBee (Grup G) skill envanteri

Bu dosya, PrimeBee ekibinin skill envanteridir: hangi skill nerede, kime ait ve ne işe yarar. Her üye kendi skill’ini eklediğinde bu tabloya bir satır ekler.

## Depo bağlamı

- **Şirket:** PrimeBee — Grup G · **Sektör:** Dijital pazarlama
- **Teknoloji:** Python · pandas · matplotlib (görselleştirme: PNG)
- **Dönem planı:** [ders/AGENTS.md](https://github.com/MAKU-VBA-GBT-II/ders/blob/main/AGENTS.md)
- **Klasörler:** `src/` kod · `data/` veri · `visuals/` grafikler · `docs/` sözlük ve analiz · `tests/` test senaryoları ve kayıtları · `reports/` sprint raporları · `skills/` ajan skill'leri

## Skill envanteri

| Yetenek | Yol | Sahibi (rol) | Ne işe yarar | Nasıl kullanılır |
|---|---|---|---|---|
| pm-rapor | `skills/pm-rapor/SKILL.md` | Dilara Başer (PM) | Haftalık sprint raporunu (`reports/report-wXX.md`) GitHub'daki Issue, yorum ve commit izlerinden derler. | Ajana: "pm-rapor skill'ini kullanarak report-w03.md yaz" |
| be-veri | `skills/be-veri/SKILL.md` | Özge Nur Doğu (BE) | Haftalık kampanya performans verisini (kanal, gösterim, tıklama, harcama, dönüşüm, gelir) sabit tohumla üretir, şemayı yazar. | Ajana: "be-veri skill'ini kullanarak data/kampanya-performans.csv dosyasını üret" |
| dq-analiz | `skills/dq-analiz/SKILL.md` | Nuri Enes Seyhan (DQ) | Metrikleri (toplam gelir, ortalama ROAS, kanal kırılımları ve top-3) hesaplar, bulguları `docs/analiz-g1.md`'ye yazar. | Ajana: "dq-analiz skill'ini kullanarak G1 kampanya performansını analiz et" |
| fe-gorsel | `skills/fe-gorsel/SKILL.md` | Tuana Gürkan (FE) | Haftalık gelir zaman serisini ve kanal kırılımını PNG olarak üretir. | Ajana: "fe-gorsel skill'ini kullanarak grafik sorununu çöz ve PNG'leri üret" |
| dq-test | `skills/dq-test/SKILL.md` | Nuri Enes Seyhan (DQ) | Veri kalitesi test senaryolarını (`tests/test-cases.md`) veri şemasına göre yazar. | Ajana: "dq-test skill'ini kullanarak tests/test-cases.md dosyasını hazırla" |
| junior-kontrol | `skills/junior-kontrol/SKILL.md` | Ceren Doğrul (Junior) | Kampanya verisini veri sözlüğüyle karşılaştırır; satır sayısı, şema, kanal kategorileri ve dönüşüm kurallarını kontrol eder, bulguları raporlar. | Ajana: "junior-kontrol skill'ini kullanarak G1 kampanya verisini elle kontrol et" |

> **Kural:** Roller görevden göreve döner (plan §1.3); skill'ler rolle birlikte el değiştirir. Yeni sahibi skill'i günceller ve bu tablodaki "Sahibi" sütununu değiştirir.

## Ajanlar için çalışma kuralları

* Veri sentetiktir; gerçek kişi verisi yoktur ve depoya asla girmez. Tüm veriler simülasyon ürünüdür.
* Veri üretimi sabit tohum (42) ile tekrarlanabilir olmalıdır.
* Yeni skill eklenince bu dosya güncellenir.
* "GitHub'da yoksa, yapılmamıştır": her iş bir Issue'ya bağlıdır; bitince Issue'ya kanıt yorumu (commit hash + dosya) yazılır.
* Hafta 5'ten itibaren `main`'e yalnızca PR ile girilir; kod/veri PR'ları DQ onayı olmadan merge edilmez.
* Bir adım bitince devir teslim yorumu yazılır; bu yorum bir sonraki kişinin başlama iznidir.
* FE, `G1-gorsel` Issue'suna iki grafik taslağı eklemeden grafik üretmeye başlamaz.
