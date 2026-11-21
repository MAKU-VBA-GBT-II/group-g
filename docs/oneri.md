# PrimeBee (Grup G) — Çok Ajanlı Şirket Programı Önerisi ve Rol Bildirimi

**Tarih:** 2026-11-21  
**Sürüm:** v1.0  
**Şirket:** PrimeBee (Grup G)  
**Sektör:** Dijital Pazarlama  
**İlgili Duyuru:** [Duyuru 10 (2026-11-20)](https://github.com/MAKU-VBA-GBT-II/ders/blob/main/Duyuru-10_2026-11-20.md)  
**Teslim Tarihi:** 26 Kasım 2026 Perşembe 13:00  

---

## 1. Senaryo

**Senaryo Adı:** Rakip Reklamlarını İnceleyip Yeni Kampanya Kurma ve Maliyet/Performans Denetimi

PrimeBee, dijital pazarlama alanında faaliyet gösteren bir veri şirketidir. Bu görev kapsamında şirketimiz, ACP (Agent Client Protocol) üzerinden çalışan, kullanıcı aboneliğiyle yerel araçları (tarayıcı, Python) yöneten ve bir pazarlama işini uçtan uca çözen üç ajanlı bir sistem geliştirecektir:

1. Kullanıcı programa hedef sektörü/ürün kategorisini ve bütçe/CPA kısıtlarını verir (Örn: "Moda ve E-ticaret sektörü için rakip reklamlarını tara, maksimum 80 TL CPA hedefiyle yeni kampanya oluştur").
2. **Ajan 1**, açık reklam kütüphanelerini tarayıcı (Playwright/Chrome) aracılığıyla tarayarak rakiplerin güncel reklam metinlerini, formatlarını ve Google Trends arama hacimlerini toplar.
3. **Ajan 2**, toplanan piyasa verilerini PrimeBee'nin sentetik geçmiş kampanya verileriyle birleştirir; Python/NLP kullanarak yeni reklam başlık ve metinleri türetir, rakip metinlerle anlamsal benzerlik skorunu hesaplar.
4. **Ajan 3**, üretilen kampanyanın tahmini CPA (Cost Per Acquisition) değerini ve metin kalitesini denetler. Simüle edilen CPA değeri bütçe eşiğini aşarsa veya veriler eksik/tutarsızsa işi gerekçesiyle Ajan 2'ye geri gönderir. Uygun bulunan çıktıyı son onaylı kampanya planı olarak teslim eder.
5. **Çekirdek ve Arayüz**, ajanların ACP üzerinden başlatılmasını, aralarındaki mesaj taşınmasını, izin onaylarını, ilerleme ekranını ve tüm oturum/araç çalıştırma loglarını yönetir.

---

## 2. Üç Ajanın Görev Tanımları

Duyuru 10 şartlarına uygun olarak her ajanın birer cümlelik net görevi ve skill yapısı:

* **Ajan 1 (Web Verisi Toplama):** Açık reklam kütüphanelerinden (Meta Ad Library) ve Google Trends üzerinden rakiplerin aktif reklam metinlerini, kategorilerini ve arama trend puanlarını tarayıcı kullanarak toplar; veri alanlarının tamlığını ve güncelliğini denetleyerek Ajan 2'nin beklediği standart şemaya dönüştürür.
* **Ajan 2 (İşleme ve Sentetik Veri ile Birleştirme):** Ajan 1'den gelen dış piyasa verilerini şirketin sentetik geçmiş kampanya performans verisiyle birleştirir; Python kullanarak yeni reklam metni varyasyonları üretir ve rakip reklam metinlerine benzerlik skorunu (TF-IDF / Cosine Similarity) hesaplar.
* **Ajan 3 (Denetim, Kalite Kontrol ve Çıktı):** Üretilen kampanyaların simüle edilen CPA (Edinme Başına Maliyet) değerini şirketin hedef eşiğine göre süzer; maliyet eşiğini aşan veya kalite kriterlerine uymayan kampanyaları gerekçesiyle Ajan 2'ye geri gönderir, onaylanan kampanyaların doğrulanmış nihai teslim raporunu hazırlar.

---

## 3. Web Kaynakları Listesi

Duyuru 10 kuralları gereği yalnızca herkese açık, giriş istemeyen, captcha içermeyen ve kişisel veri barındırmayan kaynaklar seçilmiştir. Kaynaklardan biri tarayıcı (headless browser) gerektirmektedir.

| Kaynak Adı | Web Adresi | Sağladığı Veri | Tarayıcı Gerekli mi? | robots.txt & Kullanım Şartları Kontrolü |
|---|---|---|---|---|
| **Meta Ad Library (Reklam Kütüphanesi)** | `https://www.facebook.com/ads/library/` | Rakiplerin aktif reklam metinleri, başlıkları, kampanya sektörü, yayınlanma platformu ve reklam formatı (Görsel/Video/Metin) | **EVET** (JavaScript dinamik render, asenkron sayfalama; Playwright / Headless Chrome ile toplanacak) | Kamuya açık reklam şeffaflık arşividir. Giriş/hesap gerektirmez. İstekler arasına bekleme (rate limit) konulacak, kişisel veri (yorum, kullanıcı profili) asla toplanmayacaktır. |
| **Google Trends (Arama Trendleri)** | `https://trends.google.com/trends/` | Sektör ve kategorilere ait aranma ilgisi trend puanları ($0 - 100$), yükselen arama terimleri ve anahtar kelimeler | **EVET** (Etkileşimli grafikler ve dinamik bileşenler; tarayıcı veya açık RSS/veri uçlarıyla toplanabilir) | Kamuya açık genel arama hacmi indeksidir. Kişisel veri içermez, toplu anonim istatistiktir. robots.txt kurallarına uygun sorgulama yapılır. |

> **Kişisel Veri Taahhüdü:** Hiçbir kullanıcı yorumu, isim, telefon, e-posta, sosyal medya kullanıcı profili veya gizli ticari veri çekilmeyecektir. Yalnızca reklam veren kurumların kamuya açık ilan metinleri ve genel trend kelimeleri analiz edilecektir.

---

## 4. Rol Dağılımı ve Yapay Zekâ Abonelikleri

Grubumuzdaki 5 üyenin görev dağılımı ve kullanacakları yerel yapay zekâ abonelikleri:

| Ad Soyad | GitHub Kullanıcı Adı | Yeni Görev Rolü | Yapay Zekâ Aboneliği | Rol Sorumluluğu |
|---|---|---|---|---|
| **Dilara BAŞER** | `@baserdilara94-ui` | **Çekirdek ve Arayüz (PM / Lider)** | Gemini Pro (Advanced) | ACP bağlantısı, ajanları çalıştırma/mesaj taşıma, ayar ve ilerleme ekranı, oturum logları |
| **Ceren DOĞRUL** | `@cerendogrul120-byte` | **Çekirdek ve Arayüz Desteği (Junior)** | Gemini Plus & Claude (Ücretsiz) | Çekirdek log mekanizması, oturum kayıtlarının doğrulanması ve arayüz testleri |
| **Tuana GÜRKAN** | `@tuanagurkan77` | **Ajan 1** | Gemini Plus | Web verisi alma skill'i, Playwright/tarayıcı otomasyonu, veri doğrulama ve teslim skill'i |
| **Özge Nur DOĞU** | `@Ozge-nur` | **Ajan 2** | Claude (Ücretsiz) | Şirket sentetik verisi birleştirme, metin üretme ve benzerlik hesaplama skill'i |
| **Nuri Enes SEYHAN** | `@seyhannurienes-afk` | **Ajan 3** | Gemini (Ücretsiz) | Denetim ve filtreleme skill'i, CPA eşik kontrolü, geri gönderme mekanizması ve son teslim skill'i |

---

## 5. Çekirdek ve Arayüz Mimarisi (ACP İlkeleri)

* **Protokol:** Program ajanlarla ACP (Agent Client Protocol) üzerinden iletişim kuracaktır.
* **Sıfır API Anahtarı Prensibi:** Program kodunda hiçbir API anahtarı (OpenAI, Anthropic, Google vb.) saklanmaz. Sistem, öğretim elemanının veya kullanıcının bilgisayarında kurulu olan yerel istemciyi (Vibe, Claude Code veya Codex/Gemini) kullanır.
* **Oturum ve Araç İzleri:** Ajanların çalıştırdığı her komut, açtığı her sayfa ve yürüttüğü her Python betiği Çekirdek tarafından oturum logunda (`logs/session.jsonl`) şeffaf olarak tutulacaktır.
