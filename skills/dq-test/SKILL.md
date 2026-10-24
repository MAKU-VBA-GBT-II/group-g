---
name: dq-test
description: "G1 kampanya verisi için test senaryolarını hazırlamak, src/dq_test.py ile veri sözlüğü kontrollerini çalıştırmak ve sonuçları tests/test-log.md'ye kaydetmek gerektiğinde kullan."
---

# Veri Kalitesi Test Senaryoları

## Ne yapar?

`docs/veri-sozlugu-g1.md` şemasını ve `data/kampanya-performans.csv` veri kümesini esas alarak `tests/test-cases.md` içinde veri kalitesi senaryoları hazırlar; `src/dq_test.py` ile bunları çalıştırır ve tarihli sonuçları `tests/test-log.md` içine kaydeder.

## Adımlar

1. Depo kökündeki `AGENTS.md` yönergelerini ve `docs/veri-sozlugu-g1.md` şemasını oku.
2. Beklenen boyutu, sütunları, kategorileri ve veri kurallarını veri sözlüğünden al; değerleri skill veya test senaryolarına sabitleme. `src/kampanya_simulasyon.py` sabitleriyle sözlük arasında çelişki varsa testleri çalıştırmadan önce bunu raporla.
3. `tests/test-cases.md` içinde `ID`, `Senaryo`, `Adımlar` ve `Beklenen sonuç` sütunlarıyla her kuralı ayrı ve tekrarlanabilir biçimde tanımla. Sabit kimlikler kullan: `TC-01`, `TC-02`…; en az dosya erişimi, tam kayıt sayısı, başlık, kimlik, tarih, sayısal tür/aralık/ilişki, tutar biçimi, izinli kategoriler ve kategori başına sayıyı kapsa.
4. Ek senaryolarla (tarih, kanal) benzersizliğini ve tam hafta-kanal kapsamını, boş hücreleri, UTF-8/BOM/virgül/LF biçimini ve sabit tohumla tekrar üretilebilirliği kontrol et. Her hafta-kanal çifti tam bir kez bulunmalıdır.
5. Testleri depo kökünden `python src/dq_test.py` komutuyla çalıştır. Betik her TC için `GEÇTİ` veya `KALDI` çıktısı verir ve bir test kaldığında sıfır olmayan kodla çıkar. Test üretici betiğini çalıştırıp CSV üzerine yazmaz; tekrarlanabilirliği bellekte oluşturulan iki çıktıyı ve mevcut CSV'yi karşılaştırarak kontrol eder.
6. Komutun gerçek çıktısını, test tarihini, test eden kişiyi/rolü, kullanılan araç ve Python sürümünü, test edilen veri commit'ini ve her senaryonun beklenen/gerçekleşen sonucunu `tests/test-log.md` dosyasına kaydet. Durum alanında yalnızca `Geçti`, `Kaldı` veya `Beklemede` kullan; yürütülmemiş test için sonuç uydurma.
7. Bir veya daha fazla senaryo `Kaldı` ise yeniden üretme adımlarını, beklenen ve gözlenen davranışı içeren `bug` etiketli Issue aç. Veri/üretim hatasını BE sahibine ata; test/grafik hatasını ilgili sahibine yönlendir. Başarısız testleri düzeltme veya başkasının dosyasını doğrudan değiştirme; önce Issue açıp sahibine ata.
8. İlgili Hafta 4 test Issue'suna test günlüğü ve commit hash'ini içeren kanıt yorumu bırak. Günlüğe Issue bağlantılarını ekle; sorun yoksa en az iki somut `enhancement` önerisi aç. `AGENTS.md` içindeki sahiplik ve kanıt kurallarına uy.
9. `tests/test-cases.md` dosyası yalnızca test tanımlarının kaynağıdır; gerçekleşen sonuçların tek yetkili kaynağı tarihli `tests/test-log.md` günlüğüdür. Mevcut sonuçları yeniden çalıştırmadan silme veya değiştirme.

## Kullanılan dosyalar

- `AGENTS.md` — depo kuralları ve skill envanteri
- `docs/veri-sozlugu-g1.md` — veri şeması ve doğrulama kuralları
- `data/kampanya-performans.csv` — test edilecek CSV
- `src/dq_test.py` — veri kalitesi senaryolarını çalıştıran betik
- `tests/test-cases.md` — test tanımları
- `tests/test-log.md` — tarihli test sonuçları

## Nasıl çalıştırılır?

Depo kökünde şu komutu çalıştır:

```console
python src/dq_test.py
```

Yeni senaryoları hazırlama/güncelleme isteği:

> `dq-test` skill'ini kullanarak veri sözlüğüyle tutarlı test tanımlarını `tests/test-cases.md` içine ekle.
