---
name: pm-rapor
description: PrimeBee (Grup G) haftalık sprint raporunu reports/report-wXX.md dosyasına GitHub izlerinden (Issue, commit, pano) derler. Haftalık rapor yazılacağı zaman kullan.
---

# pm-rapor — Haftalık Sprint Raporu

> *Not: Bu skill, Grup A'nın pm-rapor skill'inden PrimeBee (Grup G - Dijital Pazarlama) ihtiyaçlarına uyarlanmıştır.*

**Ne yapar:** Belirtilen hafta için sprint raporunu depodaki gerçek izlere (Issue'lar, kanıt yorumları, commit'ler) dayanarak `reports/report-wXX.md` dosyasına yazar. Uydurma bilgi yazmaz; her iddia bir Issue numarasına veya commit hash'ine bağlanır.

## Girdiler

- Hafta numarası (örn. `03`, `04`) ve hafta tarih aralığı
- Depo: `MAKU-VBA-GBT-II/group-g`
- O haftanın Issue'ları: G1-veri (#10), G1-analiz (#11), G1-görsel (#12), G1-test (#13), G1-junior (#14)
- Commit geçmişi: `git log` veya GitHub API

## Adımlar

1. **Planlananları topla:** Issue'ları listele (numara, başlık, atanan kişi, son tarih, kabul kriteri).
2. **Yapılanları doğrula:** Her Issue için kanıt yorumunu ve ilgili commit'i bul. Kabul kriterini dosyayı açıp gerçekten say ve kontrol et, tahmin etme.
3. **Devir teslim zincirini kontrol et:** BE→DQ/FE ("Veri hazır" yorumu) ve DQ→FE ("Analiz hazır" yorumu) var mı?
4. **Tıkananları yaz:** Açık kalan Issue'lar, kaçırılan son tarihler, bekleyen devir teslimler, yaşanan teknik aksaklıklar ve veri/kod ezilmeleri.
5. **Kim ne yaptı:** Her üye için commit sayısı ve kapattığı Issue'lar.
6. Raporu şablonla `reports/report-wXX.md` olarak yaz; commit mesajı: `Hafta XX sprint raporu eklendi`.

## Şablon

```markdown
# Sprint Raporu - Hafta XX (GG.AA–GG.AA.YYYY)

**Grup:** G — PrimeBee (Dijital Pazarlama) · **PM:** Dilara Başer

**Hazırlanma tarihi:** GG.AA.YYYY · **Son tarih:** GG.AA.YYYY

---

## Planlanan
| Issue | Başlık | Atanan | Kabul kriteri | Son tarih |
|---|---|---|---|---|

## Yapılan
| Issue | Kanıt (commit / dosya) | Durum |
|---|---|---|

## Devir teslim zinciri
- BE → DQ/FE: ✓/✗
- DQ → FE: ✓/✗
- DQ onayı: ✓/✗

## Tıkanan / riskler
- …

## Kim ne yaptı
| Üye | Rol | Commit | Kapattığı Issue |
|---|---|---|---|

## Gelecek hafta
- …
```

## Kullanılan dosyalar

- Okur: GitHub Issue'ları ve yorumları, `git log`, proje panosu
- Yazar: `reports/report-wXX.md`

## Nasıl çalıştırılır

Ajana (Claude, Codex vb.): **"pm-rapor skill'ini kullanarak Hafta XX için report-wXX.md yaz."**

Ajan GitHub'a erişebiliyorsa Issue'ları, yorumları ve commit'leri kendisi okuyup raporu yazar. Araç: GitHub CLI (`gh issue list`, `gh issue view`, `git log`). Kullandığı araç ve model Issue kapanış yorumuna eklenir.
