---
name: dq-sozluk
description: "PrimeBee (Grup G) Görev 2 mini ürünü için parametreli dijital pazarlama simülasyonu veri şeması, simülasyon parametreleri, türetme kuralları ve analiz metriklerini içeren docs/veri-sozlugu.md dosyasını üretir veya günceller."
---

# Veri Sözlüğü ve Analiz Planı Hazırlama (dq-sozluk)

## Amaç Cümlesi
Bu skill, PrimeBee (Grup G) dijital pazarlama veri şirketi simülasyonu için sentetik, parametreli ve tutarlı bir veri şeması tanımlamak; BE simülasyonu, FE görselleştirmeleri ve DQ kalite/analiz süreçlerine temel teşkil edecek `docs/veri-sozlugu.md` dokümanını standartlara uygun olarak üretmektir.

## Ne İşe Yarar?
- Görev 2 mini ürünü için sentetik kampanya performans veri şemasını (`docs/veri-sozlugu.md`) oluşturur ve sürdürür.
- Simülasyonun alacağı parametreleri (tohum, hafta/gün sayısı, kampanya sayısı, kanal dağılımı vb.) ve varsayılan değerlerini belirler.
- Her alan için veri tipi, değer aralıkları, kısıtlar, biçimler ve örnek değerleri tanımlar.
- Dönem planı gereğince zorunlu olan **en az 5 analitik metriği** (toplam, ortalama, 2 kırılım [biri zaman serisi], top-N) formülleri ve açıklanan hedefleriyle kayıt altına alır.
- BE, FE ve Junior rollerinin teslimatlarını doğrulayabileceği tek doğruluk kaynağını (Single Source of Truth) oluşturur.

## Çıktı Formatı Kuralları
1. **Dosya Yolu ve Biçimi:** Çıktı mutlaka `docs/veri-sozlugu.md` yolunda ve geçerli GitHub Flavored Markdown formatında olmalıdır.
2. **Başlık ve Sürüm Bilgisi:** Dosya başında dokümanın sürümü (v1.0), tarihi, hazırlayan DQ rolü ve hedef veri yolu (`data/kampanya-simulasyon-g2.csv`) bulunmalıdır.
3. **Şema Tablosu:** Tabloda `Alan`, `Tip`, `Kural/Aralık`, `Birim`, `Örnek` sütunları eksiksiz yer almalıdır.
4. **Parametre Tablosu:** BE geliştiricisinin uygulayacağı en az 2 ayarlanabilir simülasyon parametresi (`tohum`, `hafta_sayisi`, `kampanya_sayisi` vb.), veri tipi ve varsayılan değerleri açıkça listelenmelidir.
5. **Türetme ve Matematiksel Kurallar:** Alanlar arası ilişkiler (`tiklama <= gosterim`, `donusum <= tiklama`, `donusum = 0` iken `gelir_tl = 0.00`, tam 2 ondalık basamak kuralı) matematiksel formüllerle yazılmalıdır.
6. **5 Metrik Zorunluluğu:** Analiz planı tablosunda en az 5 metrik (toplam, ortalama, zaman serisi kırılımı, kategorik kırılım, top-N) adı, formülü, birimi ve neyi ölçtüğü yer almalıdır.

## Reddetme Durumları
Bu skill aşağıdaki durumlarda üretimi durdurur ve talebi gerekçesiyle **REDDEDER**:
1. **Kişisel Veri (KVKK / PII) Talebi:** Gerçek müşteri adı, soyadı, T.C. kimlik numarası, telefon numarası, e-posta, kredi kartı veya gerçek kişi IP adresi içeren hiçbir alan şemaya eklenemez. Şema yalnızca sentetik dijital pazarlama metriklerini içerebilir.
2. **Tekrarlanamayan (Sabit Tohumsuz) Simülasyon:** `tohum` (seed) parametresi içermeyen veya sabit tohumla tekrarlanamayan simülasyon şeması talepleri reddedilir.
3. **Mantıksal Tutarsızlık:** Gösterimden büyük tıklama, tıklamadan büyük dönüşüm, sıfırdan küçük harcama gibi matematiksel tutarsızlık içeren alan ilişkileri tanımlanamaz.
4. **Eksik Metrik Seti:** Toplam, ortalama, zaman serisi kırılımı, kategorik kırılım ve top-N kategorilerinden herhangi birini içermeyen analiz planları reddedilir.

## Kullanılan Dosyalar ve Kaynaklar
- `AGENTS.md` — Depo bağlamı, rol rotasyonu ve ajan çalışma kuralları
- `docs/veri-sozlugu.md` — Üretilen ana şema ve analiz planı
- `docs/veri-sozlugu-g1.md` — Görev 1 geçmiş şema referansı

## Örnek Giriş ve Çıkış

### Örnek Giriş (Prompt):
> "dq-sozluk skill'ini kullanarak Görev 2 mini ürünü için parametreli dijital pazarlama kampanya veri sözlüğünü ve 5 analiz metriğini docs/veri-sozlugu.md içine yaz."

### Örnek Çıkış (docs/veri-sozlugu.md özeti):
```markdown
# Veri Sözlüğü — Parametreli Kampanya Simülasyonu (Görev 2)
**Sürüm:** v1.0 · **Rol:** DQ (Tuana Gürkan) · **Tarih:** 2026-11-01

## Simülasyon Parametreleri
| Parametre | Tip | Varsayılan | Açıklama |
|---|---|---|---|
| tohum | int | 42 | Tekrarlanabilir rastgele sayı üreteci tohumu |
| hafta_sayisi | int | 52 | Simüle edilecek hafta adedi (1-104) |
...
```

## Nasıl Çalıştırılır?
Ajan komut satırından veya doğrudan chat üzerinden şu talimatla çağrılır:
> `dq-sozluk skill'ini kullanarak docs/veri-sozlugu.md dosyasını Görev 2 kabul kriterlerine uygun şekilde üret.`
