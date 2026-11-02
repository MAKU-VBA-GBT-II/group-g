---
name: dq-test
description: "PrimeBee (Grup G) Görev 2 mini ürünü için veri sözlüğü şemasına (docs/veri-sozlugu.md) ve parametreli simülasyon dinamiklerine uygun veri kalitesi test senaryoları (tests/test-cases.md) hazırlar veya günceller; BE PR incelemesi ve test koşumu standartlarını tanımlar."
---

# Veri Kalitesi Test Senaryoları ve İnceleme Standardı (dq-test)

## Amaç Cümlesi
Bu skill, PrimeBee (Grup G) dijital pazarlama veri şirketi mini ürününün veri güvenilirliğini, şema uyumunu ve parametreli simülasyon davranışını doğrulamak üzere `docs/veri-sozlugu.md` şemasına dayalı bağımsız test senaryolarını (`tests/test-cases.md`) oluşturmak, BE PR'larını incelemek ve test koşum standartlarını belirlemektir.

## Ne İşe Yarar?
- Görev 2 mini ürünü için sentetik kampanya performans verisi kalite test senaryolarını (`tests/test-cases.md`) yazar ve günceller.
- Simülasyonun parametre değişim davranışlarını (satır sayısı = hafta_sayisi × kampanya_sayisi, tohum determinizmi vb.) doğrulayan senaryolar üretir.
- 8 temel sütunun varlığı, veri tipleri, mantıksal sınırlar (`tiklama <= gosterim`, `donusum <= tiklama`, `harcama_tl > 0.00`, `gelir_tl >= 0.00`) ve format hassasiyetlerini (tam 2 ondalık basamak) denetler.
- BE geliştiricisinin simülasyon PR'ını incelerken en az 2 somut teknik yorum ve onay sürecini yürütür.
- Hafta 6 kapsamındaki tam test turu ve hata (`bug`) raporlama adımlarına temel oluşturur.

## Çıktı Formatı Kuralları
1. **Dosya Yolu ve Biçimi:** Senaryolar `tests/test-cases.md` dosyasında, geçerli GitHub Flavored Markdown tablosu olarak yer almalıdır.
2. **Tablo Yapısı:** Tablo zorunlu 7 sütunu içermelidir: `No`, `Senaryo`, `Adımlar`, `Girdi`, `Beklenen sonuç`, `Gerçekleşen sonuç`, `Durum`.
3. **Senaryo Sayısı ve Kapsam:** En az 5 farklı kabul senaryosu bulunmalıdır:
   - 1) Dosya varlığı ve şema dosya yolu kontrolü
   - 2) Satır sayısı ve hedef boyut kontrolü (varsayılan: 260 satır)
   - 3) Sütun adları, sıralaması ve veri tipleri
   - 4) Mantıksal aralıklar, tutarlar ve biçimler (gösterim, tıklama, dönüşüm, tam 2 ondalık TL)
   - 5) Kategori değerleri ve dağılım (5 sabit pazarlama kanalı, kanal başına eşit kayıt)
   - 6) **Parametre davranışı:** `hafta_sayisi` ve `kampanya_sayisi` değiştirildiğinde satır sayısının dinamik uyumu ile `tohum` determinizmi.
4. **Test Koşum İlkesi:** Fiili test çalıştırılmadan `Gerçekleşen sonuç` hücresi doldurulamaz; test koşumu öncesi `Durum` mutlaka `Beklemede` olarak işaretlenir.

## Reddetme Durumları
Bu skill aşağıdaki durumlarda üretimi durdurur ve talebi gerekçesiyle **REDDEDER**:
1. **Kişisel Veri (KVKK / PII) Talebi:** Gerçek müşteri veya kişi verisi içeren veri setlerini test etme talepleri; isim, TC kimlik, telefon, e-posta içeren sahte/gerçek PII alanları reddedilir.
2. **Parametre Davranışı Olmayan Test Seti:** Görev 2 parametreli bir simülasyon ürünü olduğundan, parametre değişim testlerini içermeyen test senaryo talepleri reddedilir.
3. **Uydurma Test Sonucu:** Gerçekte çalıştırılmamış testler için sahte veya hayali "Geçti" sonucu yazılması talepleri reddedilir.
4. **Tekrarlanamayan (Sabit Tohumsuz) Test Koşumu:** `tohum` değeri belirtilmemiş ve rastgelelik kontrolü yapılamayan test istekleri reddedilir.

## Kullanılan Dosyalar ve Kaynaklar
- `AGENTS.md` — Depo kuralları, roller ve devir teslim zinciri
- `docs/veri-sozlugu.md` — Görev 2 veri şeması, parametreler ve analiz planı
- `data/kampanya-simulasyon-g2.csv` — Test edilecek hedef veri kümesi
- `tests/test-cases.md` — Oluşturulan test senaryoları dokümanı
- `tests/test-log.md` — Test yürütme günlüğü ve koşum kayıtları

## Örnek Giriş ve Çıkış

### Örnek Giriş (Prompt):
> "dq-test skill'ini kullanarak docs/veri-sozlugu.md şemasına göre Görev 2 test senaryolarını tests/test-cases.md içine hazırla."

### Örnek Çıkış (tests/test-cases.md özeti):
```markdown
# G2 — Parametreli Kampanya Simülasyonu Veri Kalitesi Test Senaryoları
Şema referansı: docs/veri-sozlugu.md
Hedef veri: data/kampanya-simulasyon-g2.csv

| No | Senaryo | Adımlar | Girdi | Beklenen sonuç | Gerçekleşen sonuç | Durum |
|---:|---|---|---|---|---|---|
| 1 | Dosya Varlığı | Depo kökünden veri dosyasını kontrol et | `data/kampanya-simulasyon-g2.csv` | Dosya mevcut ve okunabilir olmalı | | Beklemede |
| 6 | Parametre Davranışı | Farklı hafta ve kampanya sayıları ile üret | `hafta_sayisi=10, kampanya_sayisi=3` | Tam 30 satır üretilmeli | | Beklemede |
```

## Nasıl Çalıştırılır?
Ajan komut satırından veya doğrudan chat üzerinden şu talimatla çağrılır:
> `dq-test skill'ini kullanarak docs/veri-sozlugu.md şemasına göre Görev 2 test senaryolarını tests/test-cases.md dosyasına yaz.`
