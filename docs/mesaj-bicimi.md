# Ortak Mesaj Biçimi ve Sözleşmesi (Data Contract)

**Şirket:** PrimeBee (Grup G)  
**Tarih:** 2026-11-27  
**Sürüm:** v1.0  
**İlgili Duyuru:** [Duyuru 11 — Çok Ajanlı Şirket Programı (İnşa Haftası 1)](https://github.com/MAKU-VBA-GBT-II/ders/blob/main/Duyuru-11_2026-11-26.md)  
**Hedef:** Ajanlar arası bağımsız çalışmayı sağlamak, girdi/çıktı formatlarını standartlaştırmak ve red döngüsünü belirlemek.

---

## 1. Genel İlkeler ve Sözleşme Kuralları

1. **Format Standardı:** Ajanlar arası veri aktarımı **JSON (UTF-8)** formatında gerçekleştirilir.
2. **Sıfır API / Bağımsızlık İlkesi:** Ajan 2, Ajan 1'in canlı çalışmasını beklemeden `data/ornek-ajan1.json` ile; Ajan 3 de Ajan 2'yi beklemeden `data/ornek-ajan2.json` ile geliştirilir ve test edilir.
3. **Zaman Damgası ve Kaynak Zorunluluğu:** Duyuru 11 gereğince aktarılan her sayısal/metrik veri bloğu için `kaynak` (hangi web sitesi veya dahili tablo) ve `uretim_zamani` (ISO 8601 formatında UTC zaman damgası) alanları **zorunludur**.
4. **Zarf Mimarisi:** Tüm mesajlar standart bir üst zarf (`envelope`) içinde iletilir:
   - `durum`: `"onay"` veya `"red"`
   - `gonderen_ajan`: `"ajan1"`, `"ajan2"` veya `"ajan3"`
   - `hedef_ajan`: `"ajan2"` veya `"ajan3"` (red durumunda tersi)
   - `zaman_damgasi`: ISO 8601 formatı (`YYYY-MM-DDTHH:MM:SSZ`)

---

## 2. Ajan 1 ➔ Ajan 2 Mesaj Formatı (Web Verisi)

Ajan 1 (Web Veri Toplayıcı), açık reklam kütüphanesinden (Meta Ad Library) ve Google Trends'ten çektiği piyasa verilerini aşağıdaki şemayla Ajan 2'ye teslim eder:

### 2.1. Şema Alanları

| Alan Adı | Tip | Zorunlu? | Açıklama |
|---|---|:---:|---|
| `reklam_id` | String | Evet | Reklamın benzersiz kayıt kimliği (Örn: `RAD-202611-001`) |
| `kaynak` | String | Evet | Verinin çekildiği platform: `Meta Ad Library` veya `Google Trends` |
| `uretim_zamani` | String | Evet | Çekilme zamanı (ISO 8601: `2026-11-27T10:15:00Z`) |
| `kategori` | String | Evet | Sektör/ürün kategorisi (`Moda`, `Elektronik`, `Kozmetik` vb.) |
| `hedef_bolge` | String | Evet | Coğrafi pazar (`TR-Marmara`, `TR-Genel` vb.) |
| `reklam_baslik` | String | Evet | Rakipten çekilen reklam başlığı |
| `reklam_metni` | String | Evet | Rakipten çekilen reklam gövde metni |
| `reklam_formati` | String | Evet | Reklam türü: `Metin`, `Gorsel`, `Video` |
| `trend_kelime` | String | Evet | Google Trends'te yükselen anahtar kelime |
| `trend_puani` | Integer | Evet | Arama trend ilgi puanı ($0 - 100$) |
| `tahmini_rakip_cpa_tl`| Float | Evet | Sektör referans müşteri edinme maliyeti (2 ondalık basamak) |

### 2.2. Örnek JSON Zarfı (`Ajan 1 ➔ Ajan 2`)

```json
{
  "durum": "onay",
  "gonderen_ajan": "ajan1",
  "hedef_ajan": "ajan2",
  "zaman_damgasi": "2026-11-27T10:15:30Z",
  "kategori": "Moda",
  "toplam_kayit": 2,
  "veriler": [
    {
      "reklam_id": "RAD-202611-001",
      "kaynak": "Meta Ad Library",
      "uretim_zamani": "2026-11-27T10:14:22Z",
      "kategori": "Moda",
      "hedef_bolge": "TR-Marmara",
      "reklam_baslik": "Kış Sezonu Mont ve Kabanlarda %40 İndirim",
      "reklam_metni": "Yeni sezon su geçirmez mont modellerinde kaçırılmayacak fırsatları hemen keşfedin. Ücretsiz kargo!",
      "reklam_formati": "Gorsel",
      "trend_kelime": "kis-sezonu",
      "trend_puani": 85,
      "tahmini_rakip_cpa_tl": 62.50
    },
    {
      "reklam_id": "RAD-202611-002",
      "kaynak": "Meta Ad Library",
      "uretim_zamani": "2026-11-27T10:14:45Z",
      "kategori": "Moda",
      "hedef_bolge": "TR-Marmara",
      "reklam_baslik": "Termal İçlik ve Polar Modelleri",
      "reklam_metni": "Soğuk havalara hazır mısınız? Termal giyimde 3 al 2 öde fırsatı sepetinizde sizi bekliyor.",
      "reklam_formati": "Metin",
      "trend_kelime": "termal-iclik",
      "trend_puani": 74,
      "tahmini_rakip_cpa_tl": 58.00
    }
  ]
}
```

---

## 3. Ajan 2 ➔ Ajan 3 Mesaj Formatı (Zenginleştirilmiş Analiz ve Kampanya Önerisi)

Ajan 2 (İşleme ve Birleştirme), Ajan 1'den gelen piyasa verilerini şirketin sentetik geçmiş performans verisi (`data/kampanya-simulasyon-g3.csv`) ile birleştirir; Python/NLP ile yeni metin türetir ve TF-IDF Cosine Similarity ile benzerlik skorunu hesaplayarak Ajan 3'e teslim eder:

### 3.1. Şema Alanları

| Alan Adı | Tip | Zorunlu? | Açıklama |
|---|---|:---:|---|
| `oneri_id` | String | Evet | Öneri paket kimliği (Örn: `PROP-202611-01`) |
| `kaynak` | String | Evet | `PrimeBee Sentetik + Meta Ad Library NLP` |
| `uretim_zamani` | String | Evet | Analiz ve türetim zamanı (ISO 8601) |
| `kanal` | String | Evet | Önerilen kanal (`Meta Ads`, `Google Ads` vb.) |
| `kategori` | String | Evet | Kampanya sektörü |
| `hedef_bolge` | String | Evet | Hedef pazar |
| `uretilmis_baslik`| String | Evet | Yeni türetilen reklam başlığı |
| `uretilmis_metin` | String | Evet | Yeni türetilen reklam metni |
| `benzerlik_skoru` | Float | Evet | Rakip metinlere anlamsal benzerlik ($0.00 - 1.00$, tam 2 basamak) |
| `planlanan_harcama_tl`| Float | Evet | Simüle edilen bütçe harcaması (TL, 2 basamak) |
| `beklenen_donusum`| Integer | Evet | Tahmini satın alma / dönüşüm adedi ($> 0$) |
| `simule_cpa_tl` | Float | Evet | Kampanyanın simüle edilen birim edinme maliyeti ($\text{harcama} / \text{donusum}$) |
| `hedef_cpa_max` | Float | Evet | Şirketin kabul ettiği tavan CPA eşiği |

### 3.2. Örnek JSON Zarfı (`Ajan 2 ➔ Ajan 3`)

```json
{
  "durum": "onay",
  "gonderen_ajan": "ajan2",
  "hedef_ajan": "ajan3",
  "zaman_damgasi": "2026-11-27T10:20:00Z",
  "oneri_id": "PROP-202611-01",
  "kaynak": "PrimeBee Sentetik + Meta Ad Library NLP",
  "uretim_zamani": "2026-11-27T10:19:45Z",
  "onerilen_kampanyalar": [
    {
      "kampanya_kodu": "CMP-OPT-01",
      "kanal": "Meta Ads",
      "kategori": "Moda",
      "hedef_bolge": "TR-Marmara",
      "uretilmis_baslik": "Kışa Özel Prime Koleksiyonu — %40 Avantajla",
      "uretilmis_metin": "Soğuk günlerde tarzınızdan ödün vermeyin. Yeni sezon su geçirmez montlarda lansmana özel avantajlar.",
      "benzerlik_skoru": 0.42,
      "planlanan_harcama_tl": 4500.00,
      "beklenen_donusum": 68,
      "simule_cpa_tl": 66.18,
      "hedef_cpa_max": 80.00
    },
    {
      "kampanya_kodu": "CMP-OPT-02",
      "kanal": "Google Ads",
      "kategori": "Moda",
      "hedef_bolge": "TR-Marmara",
      "uretilmis_baslik": "Termal Konfor Şimdi Kapınızda — 3 Al 2 Öde",
      "uretilmis_metin": "Kış soğuklarına karşı üstün koruma sağlayan termal giyim serisi sepette sürpriz hediyelerle sizi bekliyor.",
      "benzerlik_skoru": 0.38,
      "planlanan_harcama_tl": 3200.00,
      "beklenen_donusum": 45,
      "simule_cpa_tl": 71.11,
      "hedef_cpa_max": 80.00
    }
  ]
}
```

---

## 4. Standart Geri Gönderme (Red) Zarfı

Duyuru 11 uyarınca, Ajan 2 veya Ajan 3 gelen girdide eksik alan, geçersiz sayısal değer, bayat tarih veya kural ihlali tespit ettiğinde işi işleme almaz; aşağıdaki standart red zarfını döner.

### 4.1. Red Zarfı Şeması

| Alan Adı | Tip | Zorunlu? | Açıklama |
|---|---|:---:|---|
| `durum` | String | Evet | Sabit: `"red"` |
| `gonderen_ajan` | String | Evet | Reddeden ajan (`ajan2` veya `ajan3`) |
| `hedef_ajan` | String | Evet | Düzeltmesi gereken önceki ajan (`ajan1` veya `ajan2`) |
| `zaman_damgasi` | String | Evet | Reddin üretildiği ISO 8601 UTC zamanı |
| `gerekce` | String | Evet | Reddin insan ve ajan tarafından anlaşılır özeti |
| `sorunlu_alanlar`| List | Evet | Hataya sebep olan alanların detaylı listesi |

### 4.2. Örnek Red Zarfı (Ajan 2'nin Ajan 1'i Reddetmesi)

```json
{
  "durum": "red",
  "gonderen_ajan": "ajan2",
  "hedef_ajan": "ajan1",
  "zaman_damgasi": "2026-11-27T10:16:10Z",
  "gerekce": "Girdide zorunlu alanlar eksik veya veri güncelliğini yitirmiş.",
  "sorunlu_alanlar": [
    {
      "kayit_id": "RAD-202611-002",
      "alan": "trend_puani",
      "hata_turu": "eksik_alan",
      "mesaj": "trend_puani alanı boş veya null bırakılamaz."
    },
    {
      "kayit_id": "RAD-202611-002",
      "alan": "uretim_zamani",
      "hata_turu": "bayat_veri",
      "mesaj": "Veri uretim_zamani 48 saatten daha eski olamaz."
    }
  ]
}
```

### 4.3. Örnek Red Zarfı (Ajan 3'ün Ajan 2'yi Reddetmesi)

```json
{
  "durum": "red",
  "gonderen_ajan": "ajan3",
  "hedef_ajan": "ajan2",
  "zaman_damgasi": "2026-11-27T10:22:40Z",
  "gerekce": "Kampanya simülasyonu kabul edilebilir maliyet eşiğini (CPA Tavanı) aşıyor.",
  "sorunlu_alanlar": [
    {
      "kampanya_kodu": "CMP-OPT-03",
      "alan": "simule_cpa_tl",
      "hata_turu": "esik_asimi",
      "mevcut_deger": 94.50,
      "beklenen_ust_sinir": 80.00,
      "mesaj": "Hesaplanan simule_cpa_tl (94.50 TL) hedef tavan eşik olan 80.00 TL değerini aşıyor."
    }
  ]
}
```
