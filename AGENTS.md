# AGENTS.md — PrimeBee (Grup G) skill envanteri

Bu dosya, PrimeBee ekibinin skill envanteridir: hangi skill nerede, kime ait ve ne işe yarar. Her üye kendi skill’ini eklediğinde veya devraldığında bu tabloya bir satır ekler ya da günceller.

## Depo bağlamı

- **Şirket:** PrimeBee — Grup G · **Sektör:** Dijital pazarlama
- **Teknoloji:** Python · pandas · matplotlib (görselleştirme: PNG)
- **Dönem planı:** [ders/AGENTS.md](https://github.com/MAKU-VBA-GBT-II/ders/blob/main/AGENTS.md)
- **Klasörler:** `src/` kod · `data/` veri · `visuals/` grafikler · `docs/` sözlük ve analiz · `tests/` test senaryoları ve kayıtları · `reports/` sprint raporları · `skills/` ajan skill'leri

## Görev 2 Rol Dağılımı ve Rotasyon (Dönem Planı §1.3)

| Üye | Görev 1 Rolü | Görev 2 Rolü | Sorumluluk Alanı |
|---|---|---|---|
| **Dilara Başer** | PM (Lider) | **PM (Lider - sabit)** | Sprint koordinasyonu, pano hijyeni, sprint raporu, release |
| **Nuri Enes Seyhan** | DQ | **BE (Backend / Simülasyon)** | Parametreli dijital pazarlama kampanya simülasyonu, veri üretimi, PR |
| **Tuana Gürkan** | FE | **DQ (Veri Kalitesi & Analiz)** | Veri şeması (`docs/veri-sozlugu.md`), test senaryoları, PR inceleme, metrik analizi |
| **Özge Nur Doğu** | BE | **FE (Frontend / Görselleştirici)** | Grafik taslakları, 3'lü görselleştirme seti (zaman serisi, kırılım, dağılım) |
| **Ceren Doğrul** | Junior | **Junior (Kontrol & Ön İnceleme)** | Şema kontrolü, simülasyon parametre denemeleri, test ön incelemesi |

## Skill envanteri

| Skill | Yol | Sahibi (rol) | Ne işe yarar | Nasıl kullanılır |
|---|---|---|---|---|
| pm-rapor | [`skills/pm-rapor/SKILL.md`](skills/pm-rapor/SKILL.md) | Dilara Başer (PM) | Haftalık sprint raporunu (`reports/report-wXX.md`) GitHub'daki Issue, yorum, PR ve commit izlerinden derler. | Ajana: "pm-rapor skill'ini kullanarak sprint raporu yaz" |
| dq-sozluk | [`skills/dq-sozluk/SKILL.md`](skills/dq-sozluk/SKILL.md) | Tuana Gürkan (DQ, Görev 2) | Görev 2 veri sözlüğünü (`docs/veri-sozlugu.md`) üretir: alanlar, tipler, kurallar, parametreler ve 5 metrik formülü (#40). | Ajana: "dq-sozluk skill'ini kullanarak docs/veri-sozlugu.md yaz" |
| be-simulasyon | [`skills/be-simulasyon/SKILL.md`](skills/be-simulasyon/SKILL.md) | Nuri Enes Seyhan (BE, Görev 2) | Görev 2 kampanya verisini (`data/`) şemaya birebir, parametreli ve sabit tohumlu simülasyonla üretir (#41). | Ajana: "be-simulasyon skill'ini kullanarak kampanya verisi üret" · Elle: `python src/simulasyon.py` |
| fe-gorsel | [`skills/fe-gorsel/SKILL.md`](skills/fe-gorsel/SKILL.md) | Tuana Gürkan (FE, Görev 1) · Özge Nur Doğu (FE, Görev 2) | Simülasyon verisinden 3 PNG grafik üretir (zaman serisi + kanal kırılımı + dağılım); taslak koddan önce eklenir (#42). | Ajana: "fe-gorsel skill'ini kullanarak 3 grafiği üret" · Elle: `python src/grafik_uret.py` |
| dq-analiz | [`skills/dq-analiz/SKILL.md`](skills/dq-analiz/SKILL.md) | Nuri Enes Seyhan (DQ, Görev 1) · Tuana Gürkan (DQ, Görev 2) | Nihai veri üzerinden 5 metriği hesaplar; bulgulara 3 gözlem + 1 eylem önerisi yazar (`docs/analiz-g2.md`) (#43). | Ajana: "dq-analiz skill'ini kullanarak metrikleri hesapla ve bulguları yaz" |
| dq-test | [`skills/dq-test/SKILL.md`](skills/dq-test/SKILL.md) | Nuri Enes Seyhan (DQ, Görev 1) · Tuana Gürkan (DQ, Görev 2) | Görev 2 için test senaryolarını (`tests/test-cases.md`) yazar, BE PR'ını inceler ve test günlüğünü doldurur (#44). | Ajana: "dq-test skill'ini kullanarak test senaryolarını hazırla ve PR'ı incele" |
| junior-kontrol | [`skills/junior-kontrol/SKILL.md`](skills/junior-kontrol/SKILL.md) | Ceren Doğrul (Junior) | Veri sözlüğü şemasını inceler, simülasyon parametrelerini test eder, gözlem ve bulguları raporlar (#45). | Ajana: "junior-kontrol skill'ini kullanarak veri ve parametreleri test et" |
| be-veri (Arşiv) | [`skills/be-veri/SKILL.md`](skills/be-veri/SKILL.md) | Özge Nur Doğu (BE, Görev 1) | Görev 1 haftalık kampanya performans verisini sabit tohumla üreten arşiv skill'i. | Görev 1 referansı |

## Devir teslim zinciri (Görev 2)

DQ şema/sözlük (`#40`) → BE parametreli simülasyon (`#41`) & FE taslaklar (`#42`) & Junior kontrol (`#45`) → DQ BE PR inceleme/onay (`#44`) → DQ analiz (`#43`) & FE nihai grafikler (`#42`) → DQ test koşumu (`#44`) & PM sprint kapanış hijyeni / raporu.
Her adım ilgili Issue'ya commit hash'li kanıt yorumu ile biter.

> **Kural:** Roller görevden göreve döner (plan §1.3); skill'ler rolle birlikte el değiştirir. Yeni sahibi skill'i günceller ve bu tablodaki "Sahibi" sütununu değiştirir.

## Ajanlar için çalışma kuralları

1. "GitHub'da yoksa, yapılmamıştır": her iş bir Issue'ya bağlıdır; bitince Issue'ya kanıt yorumu (commit hash + dosya) yazılır.
2. Gerçek kişi verisi asla depoya girmez; tüm veriler simülasyon ürünüdür.
3. Veri üretimi sabit tohumla tekrarlanabilir olmalıdır.
4. Hafta 5'ten itibaren `main`'e yalnızca PR ile girilir; kod/veri PR'ları DQ onayı olmadan merge edilmez.
5. Bir adım bitince devir teslim yorumu yazılır; bu yorum bir sonraki kişinin başlama iznidir.
6. FE, `G2-gorsel` Issue'suna 3 grafik taslağını eklemeden grafik üretmeye başlamaz.
