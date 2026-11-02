---
name: be-simulasyon
description: "PrimeBee (Grup G) Görev 2 için docs/veri-sozlugu.md şemasına uyan, CLI parametreleri ve sabit tohumla tekrarlanabilir sentetik kampanya verisi üretir."
---

# Parametreli Kampanya Simülasyonu (be-simulasyon)

## Amaç
Bu skill, Görev 2 veri sözlüğünü uygulayan `src/simulasyon.py` simülatörünü ve `data/kampanya-simulasyon-g2.csv` çıktısını üretir veya günceller. Veri yalnızca sentetik kampanya performans ölçümlerinden oluşur; sabit tohumla yeniden üretilebilir ve yazılmadan önce şemaya göre doğrulanır.

## Girdi ve çıktı
- Kaynak şema: `docs/veri-sozlugu.md`
- Simülasyon kodu: `src/simulasyon.py`
- Varsayılan çıktı: `data/kampanya-simulasyon-g2.csv`
- Varsayılan parametreler: `tohum=42`, `hafta_sayisi=52`, `kampanya_sayisi=5`, `baslangic_tarihi=2025-10-06`
- Varsayılan boyut: 260 veri satırı ve bir başlık satırı
- Başlık: `kampanya_id,tarih,kanal,gosterim,tiklama,donusum,harcama_tl,gelir_tl`

`kampanya_sayisi`, sözlükteki kanal listesinden simüle edilecek kanal adedidir. Geçerli aralıklar `tohum >= 0`, `hafta_sayisi` 1–104, `kampanya_sayisi` 1–5 ve Pazartesi olan `baslangic_tarihi` değeridir.

## Adımlar
1. `AGENTS.md` ve `docs/veri-sozlugu.md` dosyalarını oku; alan adlarını, sıralamayı, kanal aralıklarını, formülleri ve parametre varsayılanlarını buradan al.
2. `src/simulasyon.py` içinde bu dosya yolunu ve CLI parametrelerini kullan. Rastgele değerleri yalnızca `random.Random(tohum)` nesnesinden üret.
3. Her hafta seçilen kanalları sözlük sırasıyla üret. `kampanya_id` değerlerini `K001` biçiminden başlayarak sıra ile ata.
4. `tiklama`, `donusum`, `harcama_tl` ve `gelir_tl` değerlerini sözlükteki aralıklardan ve formüllerden türet. Tutarları CSV'ye daima iki ondalık basamakla yaz.
5. CSV'yi UTF-8, virgül ayraçlı ve `\n` satır sonlu üret. Gerçek kişi, kurum veya kimlik bilgisi ekleme.
6. Yazmadan önce ve dosyayı geri okuyunca en az şu kontrolleri yap: tam satır sayısı (`hafta_sayisi × kampanya_sayisi`), tam ve sıralı 8 sütun, benzersiz `kampanya_id`, hafta-kanal çiftlerinin tekilliği, tarih ve kanal sırası, kanalın gösterim aralığı, sayısal ilişkiler, tutar aralıkları ve iki ondalık basamak.
7. Varsayılan çıktıyı iki kez üret; aynı parametrelerle CSV baytlarının aynı kaldığını doğrula. Parametre değişikliğinde satır sayısını tekrar kontrol et.
8. `tests/test-cases.md` içindeki DQ senaryolarına göre kendi çıktını doğrula. Sonuç uydurma; gerçek koşumun ölçümlerini Issue/PR açıklamasında ve test günlüğü sürecinde belirt.
9. `feature/veri` dalında değişiklikleri commit et ve push et. Commit mesajında satır sayısını ve sütun listesini belirt. `G2-veri` (#41) için PR aç; başlıkta `G2 parametreli simülasyon`, açıklamada `Closes #41` ve üretim/prompt özeti olsun. İnceleyen olarak `@tuanagurkan77` iste.
10. DQ yorumlarını PR üzerinden yanıtla ve gerekli düzeltmeleri aynı dalda yap. DQ `Approve` vermeden birleştirme.
11. Birleştirmeden sonra #43 G2-analiz ve #42 G2-gorsel Issue'larına şu devir yorumunu ekle: `Veri hazır — commit <hash>, dosya data/kampanya-simulasyon-g2.csv`.

## CLI kullanımı
Depo kökünden varsayılan veri:

```text
python src/simulasyon.py
```

Parametre örneği:

```text
python src/simulasyon.py --tohum 42 --hafta_sayisi 10 --kampanya_sayisi 3
```

Bu örnekte beklenen boyut 30 veri satırıdır; aynı parametreler her çalıştırmada aynı CSV'yi üretmelidir.

## Örnek giriş ve çıkış

**Giriş**

> be-simulasyon skill'ini kullanarak Görev 2 sözlüğüne göre varsayılan parametrelerle kampanya verisini üret ve doğrula.

**Çıkış özeti**

> `src/simulasyon.py` oluşturuldu; `data/kampanya-simulasyon-g2.csv` 260 veri satırı ve sözlükteki 8 sütunla üretildi. Tekrarlanabilirlik ve şema kontrolleri geçti.

## Reddetme durumları
- Gerçek kişisel veri (ad, telefon, e-posta, kimlik numarası, IP vb.) ekleme veya gerçek kişi/kurum verisiyle simülasyon üretme taleplerini reddet; yalnızca sentetik toplulaştırılmış metrikler üret.
- Sabit tohumla tekrarlanamayan veya sözlükte bulunmayan alanlar ekleyen talepleri reddet; şema/parametre değişikliği gerekiyorsa önce DQ ile sözlüğü güncelle.
- Şema sınırlarını bozan ya da veri doğrulamasını atlamayı isteyen talepleri reddet.

## Hata yönetimi notu
Şema aralığını korumak için bu sürüm temel parametre ve çıktı doğrulaması yapar. Hafta 6'da `fix/error-handling` dalında, ayrı Issue kapsamında ek hata yönetimi ve test kapsamı ele alınacaktır.
