---
name: be-veri
description: Dijital pazarlama (G şirketi) için sabit tohumlu, tekrarlanabilir bir kampanya performansı simülasyonu yazar, data/kampanya-performans.csv dosyasını üretir ve şemasını docs/veri-sozlugu-g1.md içine işler. BE rolünün G1 veri üretimi görevi için kullanılır.
---

# be-veri: Sektör verisini üretme (G1, BE)

## Ne yapar?
5 kanal (Google Ads, Meta Ads, TikTok Ads, E-posta, SEO) × 26 hafta = 130 satırlık sentetik kampanya verisi üretir. Aynı tohum aynı dosyayı verdiği için sonuç tekrarlanabilir.

## Ne zaman kullanılır?
- G1-veri görevinde BE olarak veri dosyasını ilk kez üretirken
- Şema (alan, aralık) değiştiğinde dosyayı yeniden üretirken

## Kullanılan dosyalar
| Dosya | Rol |
|---|---|
| `src/kampanya_simulasyon.py` | Simülasyon betiği (SEED = 42) |
| `data/kampanya-performans.csv` | Üretilen veri (çıktı) |
| `docs/veri-sozlugu-g1.md` | Alan adları, tipler, aralıklar, birimler, satır sayısı |

## Adım adım talimat
1. DQ ile alanları ve geçerli aralıkları kesinleştir; sonucu `docs/veri-sozlugu-g1.md` dosyasına yaz (PM taslağı varsa onu güncelle).
2. `src/kampanya_simulasyon.py` içinde şu değerleri veri sözlüğüne uydur: `KANALLAR` (kategori değerleri ve aralıklar), `HAFTA_SAYISI`, `BASLANGIC`. `SEED` değerini **42** olarak bırak.
3. Rastgele sayıları yalnızca `random.Random(SEED)` nesnesinden üret (global `random` kullanma).
4. Betik, dosyayı yazmadan önce kuralları kontrol eder: en az 100 satır, en az 4 kanal, tıklama ≤ gösterim, dönüşüm ≤ tıklama, harcama > 0. Kontrol başarısızsa betik hata verir ve dosya yazılmaz.
5. CSV'yi UTF-8, virgül ayraçlı, `\n` satır sonlu yaz.
6. Veri sözlüğündeki satır sayısını ve aralıkları gerçek dosyayla karşılaştır.
7. Commit et ve push et. Sonra `G1-analiz` ve `G1-gorsel` Issue'larına devir teslim yorumunu yaz.

## Nasıl çalıştırılır?
Deponun kök klasöründe:
```bash
python src/kampanya_simulasyon.py
```
Beklenen çıktı: `130 satır yazıldı: .../data/kampanya-performans.csv`

## Kontrol listesi
- [ ] Betiği iki kez çalıştırınca dosya değişmiyor (git'te "değişiklik yok" görünüyor)
- [ ] CSV'nin ilk satırı başlık, toplam 131 satır
- [ ] Veri sözlüğü, dosyadaki alanlarla birebir uyumlu
- [ ] Devir teslim yorumu iki Issue'ya da yazıldı

## Devir teslim yorumu şablonu
> Veri hazır — commit `<hash>`. Dosya: `data/kampanya-performans.csv` (130 satır). Şema: `docs/veri-sozlugu-g1.md`.
