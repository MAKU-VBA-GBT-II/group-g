---
name: junior-kontrol
description: "Görev 2'de G2 veri sözlüğünü, kampanya simülasyonunu ve parametre davranışını ön inceleyen Junior kontrol skill'i."
---

# Junior Ön İnceleme (G2)

## Ne yapar?

G2 veri sözlüğünü ve BE'nin simülasyon betiğini inceler; teslim edilen CSV'yi ve farklı simülasyon parametrelerini doğrular. Sonuçları `tests/test-log.md` içinde tarihli olarak kaydeder ve bulguları G2 Junior Issue'suna kanıtla bildirir.

## Ne zaman kullanılır?

- G2 veri sözlüğü ve simülasyon betiği için ön inceleme yaparken
- Teslim edilen G2 verisini veya farklı parametrelerle üretilen çıktıları doğrularken

## Kullanılan dosyalar ve kaynaklar

| Kaynak | Rol |
|---|---|
| `AGENTS.md` | Görev 2 rol dağılımı ve depo kuralları |
| `docs/veri-sozlugu.md` | Beklenen alanlar, tipler, sınırlar ve simülasyon parametreleri |
| `src/simulasyon.py` | Parametreli veri üreticisi |
| `data/kampanya-simulasyon-g2.csv` | BE'nin teslim ettiği varsayılan veri |
| `tests/test-cases.md` | DQ kabul senaryoları |
| `tests/test-log.md` | Tarihli, fiilen çalıştırılmış test sonuçları |
| Issue [#41](https://github.com/MAKU-VBA-GBT-II/group-g/issues/41) | BE teslimi ve devir bilgisi |
| Issue [#45](https://github.com/MAKU-VBA-GBT-II/group-g/issues/45) | Junior bulguları ve tamamlanma kanıtı |

## Adım adım talimat

1. `AGENTS.md`, `docs/veri-sozlugu.md` ve `tests/test-cases.md` dosyalarını oku. G2 dosya adlarını kullan; G1 dosyalarını bu görev için veri veya şema kabul etme.
2. `data/kampanya-simulasyon-g2.csv` dosyasını incelemeden önce Issue #41'de BE teslimini ve PR #49'daki DQ onayını doğrula. Teslim/inceleme tamamlanmamışsa veriyi test etme; engeli Issue #45'e yaz.
3. Mevcut veriyi PowerShell `Import-Csv` ile oku. Başlık sırası ve satır sayısını sözlükle karşılaştır; kanal dağılımı, eksik hücreler, benzersiz kimlikler, tarihler ve temel aralıkları kontrol et.
4. Üretim denemelerinde her zaman `--cikti` vererek çıktıyı geçici bir dizine yönlendir. Betiğin varsayılan hedefi depo içindeki G2 CSV'dir; bu dosyanın üzerine yazma.
5. Varsayılan parametrelerle 260 satırın üretildiğini doğrula. Ayrıca farklı bir Pazartesi başlangıcı, tohum, hafta sayısı ve kampanya sayısı kullan; satır sayısının `hafta_sayisi * kampanya_sayisi` ile eşleştiğini kontrol et.
6. Aynı parametrelerle iki ayrı çıktı üretip SHA-256 değerlerini karşılaştır. Aynı tohum aynı çıktıyı, farklı tohum ise farklı çıktıyı vermelidir.
7. `kampanya_sayisi` 5'ten küçükken betiğin ilk N sabit kanalı seçtiğini gözlemlersen bunu yeni bir hata olarak çoğaltma: açık Issue #53'ü kontrol et ve bulgunda bu Issue'ya bağla.
8. Yalnızca fiilen çalıştırılan kontrolleri `tests/test-log.md` dosyasına tarih, girdi, sonuç ve durumla kaydet. Beklenen veya yürütülmemiş kontrolleri geçmiş gibi göstermeden bırak.
9. Issue #45'e test özetini ve varsa ilgili Issue bağlantısını yaz. Commit alındıktan sonra commit hash'ini, değişen dosyaları ve prompt özetini ekle. Değişiklikleri ayrı dalda PR olarak sun; DQ onayı olmadan birleştirme.

## Kullanım örneği

Depo kökünden PowerShell'de örnek parametre testi:

```powershell
$out = Join-Path $env:TEMP 'group-g-g2-junior-check.csv'
python .\src\simulasyon.py --tohum 7 --hafta_sayisi 10 --kampanya_sayisi 3 --baslangic_tarihi 2026-11-02 --cikti $out
$rows = @(Import-Csv -LiteralPath $out)
$rows.Count
```

Kontrolü başlatma isteği:

> `junior-kontrol` skill'ini kullanarak G2 sözlüğünü ve BE teslimini doğrula; G2 CSV'sini koruyarak simülasyonu farklı başlangıç tarihi, tohum, hafta ve kampanya sayısıyla geçici dosyalarda çalıştır. Sonuçları tarihli test günlüğüne ve Issue #45'e yaz; mevcut kanal seçimi kısıtını Issue #53 ile ilişkilendir.

Issue yorumunda kullanılan prompt biçimi:

> Üretim/Kontrol: junior-kontrol skill'i ile, PowerShell + Python — prompt özeti: G2 şema ve parametreli simülasyon ön incelemesi; mevcut CSV korundu, alternatif parametreler geçici çıktılarda doğrulandı.
