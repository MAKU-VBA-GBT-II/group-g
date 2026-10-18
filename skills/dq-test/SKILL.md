---
name: dq-test
description: "Use when preparing or updating G1 campaign performance data-quality test scenarios from the data dictionary, including file, row-count, schema, type, range, and category checks."
---

# DQ Test Senaryoları

## Ne yapar?

`docs/veri-sozlugu-g1.md` şemasını ve `data/kampanya-performans.csv` veri kümesini esas alarak `tests/test-cases.md` içinde veri kalitesi senaryoları hazırlar. Test senaryoları; dosyanın varlığını, kayıt sayısını, sütun adlarını, tip ve aralık kurallarını, kategori değerlerini kapsar.

## Adımlar

1. Depo kökündeki `AGENTS.md` yönergelerini ve `docs/veri-sozlugu-g1.md` şemasını oku.
2. Veri dosyasının yolu, beklenen 8 sütun, hedef satır sayısı, tarih aralığı ve diğer kuralları güncel veri sözlüğünden belirle. Sayıları (ör. 130 veya 260) sabit kodlama. Kanal kategorilerini sözlükteki sabit değerlerden al. `src/kampanya_simulasyon.py` doğrulamalarını ince ve sözlük ile tutarlılığını karşılaştır.
3. `tests/test-cases.md` dosyasını altı zorunlu sütunlu bir Markdown tablosu olarak hazırla: `No`, `Senaryo`, `Adımlar`, `Beklenen sonuç`, `Gerçekleşen sonuç`, `Durum`.
4. En az şu kontroller için ayrı ve tekrarlanabilir senaryolar yaz: CSV'nin bulunması; başlık hariç en az 100 satır (hedef güncel sözlükten alınır); doğru 8 sütun; veri tipleri ve `tiklama <= gosterim`, `donusum <= tiklama`, `harcama_tl > 0`, `gelir_tl >= 0` dahil şema aralıkları; yalnızca izin verilen 5 kanalın kullanılması ve en az 4 farklı kanal bulunması.
5. Şema gerektiriyorsa ek kuralları da dikkate al: kampanya kimliği biçimi ve benzersizliği; tarih biçimi, aralığı ve haftanın günü; gösterim aralığı 5.000–250.000; tıklama en az 1; dönüşüm en az 0; tutarların pozitif/sıfır alt sınırları ve CSV'de tam iki ondalık basamakla yazılması; kategori başına kayıt sayısı. Beklenen sonuçları güncel veri sözlüğüne göre yaz; sözlük, veri ve üretici betiği arasında çelişki bulursan bunu açıkça belirt.
6. Senaryoların adımlarını ve beklenen sonuçlarını yaz; dosyaları gerçekten çalıştırıp doğrulamadan `Gerçekleşen sonuç` hücrelerini doldurma. Yürütme henüz yapılmadıysa `Durum` değerini beklemede olarak belirt.
7. Tablonun Markdown biçimini, en az beş senaryo içerdiğini ve bütün zorunlu sütunların bulunduğunu kontrol et. `AGENTS.md` skill envanterinde `dq-test` satırının doğru yol, sahip ve kullanım bilgisiyle yer aldığını doğrula.

## Kullanılan dosyalar

- `AGENTS.md` — depo kuralları ve skill envanteri
- `docs/veri-sozlugu-g1.md` — veri şeması ve doğrulama kuralları
- `data/kampanya-performans.csv` — test edilecek CSV
- `tests/test-cases.md` — oluşturulacak test senaryoları

## Nasıl çalıştırılır?

VS Code ajanına şu isteği ver:

> `dq-test` skill'ini kullanarak `docs/veri-sozlugu-g1.md` şemasına göre `tests/test-cases.md` dosyasını hazırla veya güncelle.

Bu skill test senaryoları dokümantasyonunu üretir; testlerin fiilen yürütülmesini veya sonuç uydurulmasını istemez. Testleri çalıştırırken veri dosyasını depo kökündeki Python veya CSV araçlarıyla incele ve gerçek sonuçları ancak yürütme sonrasında kaydet.
