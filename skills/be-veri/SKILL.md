---
name: be-veri
description: Dijital pazarlama (G şirketi) için sabit tohumlu, tekrarlanabilir bir kampanya performansı simülasyonu yazar, data/kampanya-performans.csv dosyasını üretir ve şemasını docs/veri-sozlugu-g1.md içine işler. BE rolünün G1 veri üretimi görevi için kullanılır.
---

# be-veri: Sektör verisini üretme (G1, BE)

## Ne yapar?
5 kanal (Google Ads, Meta Ads, TikTok Ads, E-posta, SEO) × 52 hafta = 260 satırlık sentetik kampanya verisi üretir. Aynı tohum aynı dosyayı verdiği için sonuç tekrarlanabilirdir.

## Ne zaman kullanılır?
- G1-veri görevinde BE olarak veri dosyasını ilk kez üretirken
- Şema (alan, aralık) ya da satır sayısı değiştiğinde dosyayı yeniden üretirken

## Kullanılan dosyalar
| Dosya | Rol |
|---|---|
| `src/kampanya_simulasyon.py` | Simülasyon betiği (SEED = 42) |
| `data/kampanya-performans.csv` | Üretilen veri (çıktı) |
| `docs/veri-sozlugu-g1.md` | Alan adları, tipler, aralıklar, birimler, satır sayısı |

## Adım adım talimat
1. DQ ile alanları ve geçerli aralıkları kesinleştir; sonucu `docs/veri-sozlugu-g1.md` dosyasına yaz (PM taslağı varsa onu güncelle).
2. `src/kampanya_simulasyon.py` içinde şu değerleri veri sözlüğüne uydur: `KANALLAR` (kategori değerleri ve aralıklar), `HAFTA_SAYISI`, `BASLANGIC` (bir Pazartesi olmalı). `SEED` değerini **42** olarak bırak.
3. Rastgele sayıları yalnızca `random.Random(SEED)` nesnesinden üret (global `random` kullanma).
4. Tutarları (harcama, gelir) **metin olarak** `f"{x:.2f}"` ile yaz. Yalnızca `round(x, 2)` yetmez: `4717.0` gibi tek ondalıklı yazılabilir.
5. Betik, dosyayı yazmadan önce veri sözlüğündeki **tüm** kuralları kontrol eder (`dogrula` fonksiyonu): satır sayısı, benzersiz ve `K001`–`K260` aralığında kampanya kimlikleri, tarih biçimi/aralığı/Pazartesi olması, tam olarak 5 geçerli kanal ve kanal başına 52 satır, gösterim aralığı, tıklama ≤ gösterim, dönüşüm ≤ tıklama, harcama > 0, gelir ≥ 0, tutarların tam 2 ondalık basamağı. Biri bozuksa betik hata verir ve dosya yazılmaz.
6. CSV'yi UTF-8, virgül ayraçlı, `\n` satır sonlu yaz.
7. Veri sözlüğündeki satır sayısını ve aralıkları gerçek dosyayla karşılaştır; sözlüğün sürümünü ve değişiklik günlüğünü güncelle.
8. Commit et ve push et. Sonra `G1-analiz` ve `G1-gorsel` Issue'larına devir teslim yorumunu yaz.

## Nasıl çalıştırılır?
Deponun kök klasöründe:
```bash
python src/kampanya_simulasyon.py
```
Beklenen çıktı: `260 satır yazıldı: .../data/kampanya-performans.csv`

## Kontrol listesi
- [ ] Betiği iki kez çalıştırınca dosya değişmiyor (git'te "değişiklik yok" görünüyor)
- [ ] CSV'nin ilk satırı başlık, toplam 261 satır
- [ ] Tüm harcama_tl ve gelir_tl değerleri tam 2 ondalık basamaklı
- [ ] Veri sözlüğü, dosyadaki alanlarla ve kurallarla birebir uyumlu
- [ ] Devir teslim yorumu iki Issue'ya da yazıldı

## Devir teslim yorumu şablonu
> Veri hazır — commit `<hash>`. Dosya: `data/kampanya-performans.csv` (260 satır). Şema: `docs/veri-sozlugu-g1.md`.
