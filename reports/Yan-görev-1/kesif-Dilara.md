**Repo:** [mautic/mautic — Open Source Marketing Automation](https://github.com/mautic/mautic)

## Çözdüğü problem

Dijital pazarlamada "hangi müşteriye, hangi kanaldan, hangi zamanda, hangi mesajı gönderelim?" sorusunun elle yönetilmesi zordur; kişi sayısı arttıkça e-posta listeleri, form kayıtları ve web sitesi hareketleri farklı araçlara dağılır, kampanyalar tek tek elle hazırlanır ve kişiye özel iletişim kurmak imkansızlaşır. Bu repo, pazarlama otomasyonunu pahalı ve kapalı SaaS araçlarına bırakmak yerine, kendi sunucuda çalıştırılabilen açık kaynaklı bir platformla çözer: kişi takibi, segmentasyon, e-posta kampanyaları, form ve açılış sayfaları, lead skorlama ve otomatik kampanya akışlarını tek yerden yönetmeyi sağlar.

## Güçlü yanları

- **Pazarlamaya doğrudan uygun:** Kişi takibi, segmentasyon, kampanya akışları, e-posta, form, açılış sayfası ve web sitesi aktivite takibi gibi dijital pazarlamanın temel ihtiyaçları hazır destekleniyor; sistemi sıfırdan yazmak gerekmiyor.
- **Ücretsiz ve veri sende:** GPL v3 lisanslı ve kullanımı ücretsiz; PHP ile yazılmış, kendi sunucuda ve kendi veritabanında çalışıyor. Müşteri verisi kuruma ait kalıyor, kişi sayısına göre artan abonelik ücreti yok.
- **Genişletilebilir ve topluluk desteği güçlü:** Açık REST API ve eklenti yapısı ile CRM ve diğer araçlara bağlanabiliyor. Yaklaşık 10.8k yıldız ve 3.5k fork ile aktif bir topluluğu var; kullanıcı ve geliştirici dokümantasyonu mevcut.
- **Kolay denenebilir:** Repoda DDEV yapılandırması var; `ddev start` komutuyla yerel ortamda hızlıca kurulup denenebiliyor. Üretim için ise Composer veya hazır paket öneriliyor.

## Kendi projemde kullanabileceğim fikir

- **Proje lideri olarak karar:** Ekibin ürettiği kampanya verisini (`data/kampanya-performans.csv`) yalnızca üretilip bırakılan bir dosya olmaktan çıkarıp, hangi segmente hangi mesajın daha iyi çalıştığını gösteren segmentli otomatik kampanyaya dönüştürmek için "pazarlama otomasyonu" adımını projeye ek bir görev olarak eklemeyi öneriyorum. Mautic hazır olduğu için bu adım için yeni bir sistem geliştirmeye gerek yok; ekibin işi veriyi doğru hazırlamak ve sonucu ölçmek.
- **Görev dağılımı:** Veri adımından sorumlu kişi, `kampanya-performans.csv` içindeki kişi, segment, gönderim, açılma ve tıklama bilgilerinin Mautic'in içe aktarabileceği biçimde (temiz ve tekrarsız) çıktı vermesini sağlar. Kampanya adımından sorumlu kişi, segmentleri oluşturur ve hoş geldin serisi gibi hazır bir otomatik akışı projenin verisine uyarlar. Rapor adımından sorumlu kişi sonuçları tabloya döker.
- **Başarı ölçütü (liderin belirlediği):** "Elle yapılan toplu gönderim ile Mautic segmentli kampanyası arasındaki açılma ve tıklama oranı farkı" tek bir net metrik olarak raporlanır. Böylece ekip, çalışmanın işe yarayıp yaramadığını sayıyla gösterebilir.
- **Risk yönetimi:** Mautic'in GitHub'daki kaynak kodunun etiketli sürümler dışında "alpha" sayılması, e-posta gönderiminde alan adı doğrulaması (SPF/DKIM) yapılmazsa e-postaların spam'e düşebilmesi ve müşteri verisinin kişisel veri olduğu için KVKK uyumunun gerekmesi baştan ekibe bildirilir; ilk sürümde küçük bir test listesi ve tek bir kampanyayla başlanır, gerçek müşteri listesiyle genişletme sonraki aşamaya bırakılır.
