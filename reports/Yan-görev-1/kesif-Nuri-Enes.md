# Repo Keşfi — wger

**İncelediğim repo:** [wger-project/wger](https://github.com/wger-project/wger)

**İnceleme tarihi:** 21 Ekim 2026

Dersteki kısa sunum için spor ve fitness alanında açık kaynaklı bir repo inceledim.

## Çözdüğü problem

Antrenman programlarını, yapılan egzersizleri, beslenmeyi ve vücut ağırlığındaki değişimi farklı yerlerde takip etmek zor olabilir. wger; antrenman planları, egzersiz kaydı, beslenme ve kilo takibini tek bir fitness yönetim uygulamasında bir araya getiriyor. Kullanıcılar egzersiz ansiklopedisine erişebiliyor, ölçümlerini ve gelişim fotoğraflarını kaydedebiliyor.

## Güçlü yanları

- **Birden fazla ihtiyacı tek yerde topluyor:** Antrenman rutinleri, egzersizler, beslenme, kilo ve vücut ölçümleri aynı uygulamada yönetilebiliyor.
- **Açık kaynak ve kendi sunucunda çalıştırılabilir:** Uygulama AGPL-3.0-or-later lisanslı. Docker ile kendi sunucunda çalıştırılabiliyor; böylece kurulum ve verilerin barındırılması üzerinde daha fazla kontrol sağlıyor.
- **Farklı platformlarda kullanılabiliyor:** Web uygulamasının yanında Android, iOS, F-Droid ve Flathub üzerinden sunulan uygulamaları var.
- **Katkı yolları açık:** Proje; kod, çeviri, egzersiz içeriği ve hata/özellik bildirimleriyle katkı kabul ediyor. Örneğin [#2540 numaralı PR](https://github.com/wger-project/wger/pull/2540), API üzerinden egzersiz çevirilerini dile göre filtrelemeyi ekledi ve 21 Ekim 2026'da ana dala alındı. Bu, topluluk katkısının kullanıcıya dönük bir özelliğe nasıl dönüştüğünü gösteriyor.
- **Dokümantasyon ve entegrasyon desteği var:** Kurulum ve API belgeleri bulunuyor; REST API üçüncü taraf araçlarla entegrasyona imkân sağlıyor.

## Neden bu repoyu seçtim, keşiften ne öğrendim?

Spor ve fitness konularına ilgim olduğu için wger'i seçtim. İncelerken büyük bir açık kaynak projesinin yalnızca uygulama kodundan ibaret olmadığını; kurulum belgeleri, API, çeviriler, Issue ve PR süreçlerinin de projenin önemli parçaları olduğunu gördüm. Küçük bir katkının bile (örneğin API filtrelemesi) ayrı bir PR üzerinden tartışılıp ana projeye eklenebilmesi dikkatimi çekti.

## Kendi projemde kullanabileceğim fikir

Bizim kampanya performansı projemiz ile wger farklı alanlarda çalışıyor; wger'i doğrudan projeye eklemek yerine çalışma biçiminden fikir alabilirim. wger'in API ve dokümantasyon yaklaşımı, bizim veri sözlüğümüzün de net ve tek referans olmasının önemini gösteriyor. Kampanya verisinde yeni bir metrik veya kanal eklendiğinde veri sözlüğü, analiz ve grafiklerin birlikte güncellenmesi; sonuçların da test edilmesi gerekir. Böylece farklı ekip üyelerinin ürettiği veri ve görseller aynı tanımlara dayanır.

Mevcut `data/kampanya-performans.csv` dosyası toplu kampanya-hafta kayıtlarından oluşuyor; kişi veya müşteri segmenti içermiyor. Bu nedenle wger'den alınacak fikir, müşteri verisi varmış gibi varsaymak değil; kapsamı ve veri alanları açıkça belgelenmiş, doğrulanabilir bir sistem kurma yaklaşımıdır.
