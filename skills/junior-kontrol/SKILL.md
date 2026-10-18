---
name: junior-kontrol
description: "Use when manually checking the G1 campaign-performance CSV after the BE handoff, reporting data-quality findings, or updating the selected row-count and channel-category scenarios."
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
| `data/kampanya-performans.csv` | Elle kontrol edilecek veri |
| `tests/test-cases.md` | Satır sayısı ve kanal kategorileri senaryolarının kaydı |
| G1-Analiz Issue'su (#11) | BE teslim yorumunu bekleme ve bulguları bildirme |
| G1-Junior Görev Issue'su (#14) | Kontrol tamamlanma ve commit kanıtı |

## Adım adım talimat

1. Depo kökündeki `AGENTS.md` ve `docs/veri-sozlugu-g1.md` dosyalarını oku. Skill örneği gerekiyorsa depoda mevcut bir `SKILL.md` dosyasını kullan; envanterde listelenen bir dosyanın bulunmadığını varsayma.
2. **Veri dosyasını açmadan önce** G1-Analiz Issue'sunda BE'nin güncel `Veri hazır — commit <hash>` teslim yorumunu bekle. Yorumdaki commit ve satır sayısının güncel teslimi belirlediğini doğrula. Teslim yoksa veriye bakma; önce G1-Junior Görev Issue'suna engeli ve teslim talebini yaz.
3. Teslim onaylandıktan sonra `data/kampanya-performans.csv` dosyasını Excel'de veya GitHub dosya görünümünde aç. Başlık hariç kayıt sayısını belirle. Geçerli hedefi veri sözlüğünün güncel sürümünden al; eski görev metnindeki satır sayısı güncel sözlükle çelişiyorsa ikisini de not et ve sözlüğü esas al.
4. Başlıktaki sütun adlarını ve sayısını veri sözlüğündeki şemayla karşılaştır. `kanal` sütunundaki farklı değerleri çıkar; sayısını ve her değeri kaydet.
5. Her kayıt için `tiklama > gosterim` ve `donusum > tiklama` durumlarını kontrol et. Excel'de örneğin `=D2<E2` ve `=E2<F2` koşullu kontrolleri kullan; sütun yerlerini CSV başlığıyla eşleştir.
6. Tüm veri hücrelerinde boş veya yalnızca boşluk içeren değer olup olmadığını kontrol et. Her kontrolün sonucunu ve varsa etkilenen kayıt/sütunları not et.
7. İstenen iki senaryoyu DQ ile belirle. Varsayılan kısa kapsam, **Satır sayısı** ve **Kanal kategori değerleri** senaryolarıdır. `tests/test-cases.md` içinde yalnızca bu senaryoların beklenen/gerçekleşen sonuçlarını güncelle; gerçekleşen sonucu kontrolü gerçekten yaptıktan sonra yaz.
8. G1-Junior Görev Issue'suna bulguları madde madde yaz. Sorun yoksa açıkça `sorun bulunmadı` de. Commit alındıktan sonra aynı Issue'ya `Veri kontrolü tamam — commit <hash>. Bulgular: <kısa özet>.` biçiminde kanıt bırak.

## Nasıl çalıştırılır?

Bu skill, otomatik analiz betiği değil; VS Code ajanına verilecek iş akışıdır. Depo kökünde ajana şu isteği ver:

> `junior-kontrol` skill'ini kullanarak G1 kampanya verisini, BE teslimini bekleyerek elle kontrol et; DQ ile seçilen iki senaryoyu tests/test-cases.md içinde güncelle ve bulguları G1-Junior Görev Issue'suna yaz.

CSV'yi incelemek için Excel veya GitHub dosya görünümü kullan. Veriyi açmadan önce Issue #11'de güncel BE teslimi bulunduğunu doğrula.
