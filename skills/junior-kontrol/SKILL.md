---
name: junior-kontrol
description: "BE tesliminden sonra VS Code yapay zekâ ajanının PowerShell ile G1 kampanya performansı CSV'sini kontrol etme, veri kalitesi bulgularını raporlama veya seçilen test senaryolarını güncelleme görevlerinde kullan."
---

# Junior Veri Kontrolü (G1)

## Ne yapar?

BE'nin teslim ettiği kampanya performansı CSV'sini veri sözlüğüyle karşılaştırır; kayıt sayısını, şemayı, kanal kategorilerini, tıklama/dönüşüm kurallarını ve boş hücreleri kontrol eder. Sonuçları G1-Junior Görev Issue'sunda raporlar ve DQ ile seçilen iki senaryonun gerçekleşen sonuçlarını `tests/test-cases.md` içinde günceller.

## Ne zaman kullanılır?

- G1 kampanya CSV'si için junior veri kalitesi kontrolü yaparken
- BE'nin yeni bir veri teslimini inceleyip Issue'da kanıt raporu hazırlarken

## Kullanılan dosyalar ve kaynaklar

| Kaynak | Rol |
|---|---|
| `AGENTS.md` | Depo kuralları ve skill envanteri |
| `docs/veri-sozlugu-g1.md` | Beklenen şema, kategori değerleri ve veri kuralları |
| `data/kampanya-performans.csv` | VS Code yapay zekâ ajanının PowerShell `Import-Csv` ile okuyup denetleyeceği veri |
| `tests/test-cases.md` | Satır sayısı ve kanal kategorileri senaryolarının kaydı |
| G1-Analiz Issue'su (#11) | BE teslim yorumunu bekleme ve bulguları bildirme |
| G1-Junior Görev Issue'su (#14) | Kontrol tamamlanma ve commit kanıtı |

## Adım adım talimat

1. Depo kökündeki `AGENTS.md` ve `docs/veri-sozlugu-g1.md` dosyalarını oku. Skill örneği gerekiyorsa depoda mevcut bir `SKILL.md` dosyasını kullan; envanterde listelenen bir dosyanın bulunmadığını varsayma.
2. **Veri dosyasını açmadan önce** G1-Analiz Issue'sunda BE'nin güncel `Veri hazır — commit <hash>` teslim yorumunu bekle. Yorumdaki commit ve satır sayısının güncel teslimi belirlediğini doğrula. Teslim yoksa veriye bakma; önce G1-Junior Görev Issue'suna engeli ve teslim talebini yaz.
3. Teslim onaylandıktan sonra VS Code yapay zekâ ajanı olarak depo kökünde PowerShell `Import-Csv` komutunu çalıştırıp CSV'yi incele: `$rows = @(Import-Csv .\data\kampanya-performans.csv)`. Bu iş akışında kontrolü yöneten ve sonuçları raporlayan araç yapay zekâ ajanı; CSV'yi okumak ve kayıtları süzmek için kullanılan araç PowerShell'dir. Excel kullanılmadı. `$rows.Count` başlık hariç kayıt sayısını verir. Geçerli hedefi veri sözlüğünün güncel sürümünden al; eski görev metnindeki satır sayısı güncel sözlükle çelişiyorsa ikisini de not et ve sözlüğü esas al.
4. CSV başlığındaki sütun adlarını ve sırasını veri sözlüğündeki şemayla karşılaştır. `$rows | Group-Object kanal` komutuyla farklı kanal değerlerini ve kayıt sayılarını çıkar; sonuçları kaydet.
5. Sayısal alanların geçerli olduğu doğrulandıktan sonra her kayıt için `tiklama > gosterim` ve `donusum > tiklama` ihlallerini PowerShell ile bul:
   - `$clickViolations = @($rows | Where-Object { [int]$_.tiklama -gt [int]$_.gosterim })`
   - `$conversionViolations = @($rows | Where-Object { [int]$_.donusum -gt [int]$_.tiklama })`

   Her iki filtre de tüm `$rows` kayıtlarına uygulanır. Her liste için `.Count` değerini ve `ForEach-Object kampanya_id` ile etkilenen kayıt kimliklerini bulgu raporuna yaz. İhlal yoksa ilgili kontrol için `0 ihlal` ve `Etkilenen kampanya: yok` olarak kaydet.
6. Tüm veri hücrelerinde boş veya yalnızca boşluk içeren değer olup olmadığını kontrol et. Her kontrolün sonucunu ve varsa etkilenen kayıt/sütunları not et.
7. İstenen iki senaryoyu DQ ile belirle. Varsayılan kısa kapsam, **Satır sayısı** ve **Kanal kategori değerleri** senaryolarıdır. `tests/test-cases.md` içinde yalnızca bu senaryoların beklenen/gerçekleşen sonuçlarını güncelle; gerçekleşen sonucu kontrolü gerçekten yaptıktan sonra yaz.
8. G1-Junior Görev Issue'suna bulguları madde madde yaz. Sorun yoksa açıkça `sorun bulunmadı` de. Commit alındıktan sonra aynı Issue'ya `Veri kontrolü tamam — commit <hash>. Bulgular: <kısa özet>.` biçiminde kanıt bırak.
9. Değişiklikleri ayrı bir dalda commit edip PR aç. `main` dalına alınmadan önce DQ'nun **Approve** incelemesini bekle; onay gelmeden PR'ı birleştirme.

## Nasıl çalıştırılır?

Bu skill, otomatik analiz betiği değil; VS Code ajanına verilecek iş akışıdır. Depo kökünde ajana şu isteği ver:

> VS Code yapay zekâ ajanı olarak `junior-kontrol` skill'ini kullan; BE teslimini bekle, G1 kampanya verisini PowerShell Import-Csv ile denetle, DQ ile seçilen iki senaryoyu tests/test-cases.md içinde güncelle ve bulguları G1-Junior Görev Issue'suna yaz. Değişiklikleri PR olarak sun ve DQ Approve vermeden birleştirme.

Bu iş akışında VS Code yapay zekâ ajanı incelemeyi yönlendirir, PowerShell `Import-Csv` CSV'yi okuma ve kayıtları süzme aracıdır; Excel kullanılmaz. Veriyi okumadan önce Issue #11'de güncel BE teslimi bulunduğunu doğrula.
