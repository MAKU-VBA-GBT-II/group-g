---
name: dq-analiz
description: "Doğrulanmış G1 kampanya CSV dosyasından toplam, ortalama ve kanal metriklerini hesaplayıp analiz raporunu ve haftalık gelir trendini hazırlarken kullan."
---

# DQ Analiz Skill'i

## Ne yapar?

Doğrulanmış `data/kampanya-performans.csv` ve `docs/veri-sozlugu-g1.md` temelinde kampanya performans metriklerini hesaplar, yorumları ve eylem önerisini `docs/analiz-g1.md` dosyasına yazar. Sonucu ilgili Issue'lara commit kanıtı ve devir teslim notuyla bildirir.

## Ne zaman kullanılır?

- BE, `G1-Analiz` Issue'suna güncel veri commit'i ve satır sayısını içeren `Veri hazır — commit ...` yorumunu ekledikten sonra.
- Kampanya verisi veya veri sözlüğü güncellendiğinde analizi yeniden üretirken.

## Adımlar

1. `AGENTS.md`, `docs/veri-sozlugu-g1.md` ve bu skill'deki iş akışını oku.
2. `G1-Analiz` Issue'sunda BE'nin en son teslim yorumunu doğrula. Yorumdaki commit'in depoda bulunduğunu ve güncel `data/kampanya-performans.csv` ile şema sürümünün aynı teslimata ait olduğunu kontrol et. Teslim yoksa analize başlama.
3. CSV'yi UTF-8 ve virgül ayraçlı olarak oku. Satır sayısı, sütun adları, kategori kümesi ve tutarların iki ondalık biçimini sözlükle karşılaştır. Uyumsuzluk varsa metrikleri teslim edilmiş gibi raporlama; önce DQ/BE üzerinden netleştir.
4. Para toplamlarını ondalık aritmetik (`Decimal`) ile hesapla; ara adımlarda `float` kullanma. Gerekli metrikleri üret:
   - toplam gelir (TL);
   - kayıt/kampanya-hafta ROAS değerlerinin aritmetik ortalaması;
   - kanala göre toplam gelir ve toplam gelir içindeki payı;
   - kanala göre ROAS = kanal toplam geliri / kanal toplam harcaması;
   - kanal ROAS'ına göre ilk üç kanal.
5. Ortalama kampanya ROAS'ı ile birleşik ROAS'ı karıştırma. Gerekirse birleşik ROAS'ı toplam gelir / toplam harcama olarak ayrıca ver ve iki ölçünün neden farklı olabileceğini açıkla.
6. Sonuçları `docs/analiz-g1.md` içine yaz. Her metriğe 1–2 cümlelik yorum, sayılara dayalı 3 somut gözlem ve tek, uygulanabilir bir eylem önerisi ekle. Verinin sentetik olduğunu ve gözlemsel sonuçların tek başına nedensellik göstermediğini belirt.
7. Sayıları veri üzerinde tekrar hesaplayarak doğrula; metrik kategorilerinin toplamlarıyla genel toplamların tutarlılığını ve top-3 sırasını kontrol et.
8. Skill'i, envanter satırını ve analiz raporunu commit edip depoya gönder. Commit hash'ini `G1-Analiz` Issue'suna kanıt olarak yaz. `G1-Görsel` Issue'suna şu biçimde devir teslim yorumu ekle: `Analiz hazır — commit <hash>. Dosya: docs/analiz-g1.md. Metrikler: <kısa liste>.`
9. Başka bir rolün sahibi olduğu dosyada hata görürsen o dosyayı değiştirme. Kanıt ve yeniden üretme adımlarıyla `bug` etiketli bir Issue açıp dosyanın sahibine ata.
10. Analizi aynı veriyle yeniden üretmek veya veri güncellendiğinde yenilemek için depo kökünde `python src/analiz_g1.py` komutunu çalıştır. Betik CSV şema kontrollerinden geçmezse hata verip raporu güncellemez.

## Kullanılan dosyalar

| Dosya | Rol |
|---|---|
| `AGENTS.md` | Depo yönergeleri ve skill envanteri |
| `docs/veri-sozlugu-g1.md` | Güncel veri şeması, kapsam ve kurallar |
| `data/kampanya-performans.csv` | Analiz girdisi |
| `docs/analiz-g1.md` | Metrik, yorum, gözlem ve eylem raporu |
| `src/analiz_g1.py` | CSV'yi doğrulayan ve analiz raporunu yeniden üreten betik |
| `skills/dq-analiz/SKILL.md` | Bu iş akışı |

## Nasıl çalıştırılır?

VS Code ajanına şu isteği ver:

> `dq-analiz` skill'ini kullan. Önce G1-Analiz Issue'sunda BE'nin güncel teslim yorumunu doğrula; ardından CSV'den metrikleri hesapla ve `docs/analiz-g1.md` dosyasını hazırla.

Analizi yeniden üretmek için depo kökünden `python src/analiz_g1.py` çalıştır. Betik yalnızca Python standart kütüphanesini kullanır; veri teslimini doğrular, metrikleri `Decimal` ile hesaplar ve haftalık toplam gelir tablosunu da içeren `docs/analiz-g1.md` dosyasını yazar.
