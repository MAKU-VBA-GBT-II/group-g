# Yan Görev #16: Açık Kaynak Repo İncelemesi

* **İncelediğim repo:** `streamlit/streamlit`
* **İnceleme tarihi:** 21 Ekim 2026

Dersteki kısa sunum için veri bilimi ve görselleştirme alanında popüler bir açık kaynak proje olan **Streamlit** reposunu inceledim.

### Çözdüğü Problem
Veri analistlerinin ve veri bilimcilerinin hazırladığı Python analizlerini, makine öğrenmesi modellerini veya grafikleri kullanıcıların etkileşime girebileceği bir web uygulamasına dönüştürmek karmaşık web geliştirme (HTML/CSS/JS) süreçleri gerektirir. **Streamlit**; sadece Python kodları yazarak veri odaklı interaktif web panelleri ve dashboard'lar oluşturmayı son derece kolaylaştırır.

### Güçlü Yanları
* **Saf Python İle UI Geliştirme:** Front-end bilgisine ihtiyaç duymadan, doğrudan Python script'leri üzerinden grafikler ve kullanıcı arayüzleri tasarlamaya imkan tanır.
* **Açık Kaynak ve Zengin Ekosistem:** Apache-2.0 lisansı ile sunulan proje; çok geniş bir geliştirici topluluğuna, eklenti desteğine ve aktif bir katkı mekanizmasına sahiptir.
* **Modüler Klasör Yapısı ve Aktif PR Kültürü:** Repoda çekirdek kodlar (`lib/`), testler ve dokümantasyon çok net bir mimariyle ayrılmıştır. Pull Request (PR) ve Issue süreçleri son derece düzenli yürütülmektedir.
* **Zengin Veri Görselleştirme Entegrasyonu:** `matplotlib`, `pandas`, `plotly` ve `altair` gibi sık kullanılan veri kütüphaneleriyle eksiksiz ve doğrudan uyumlu çalışır.

### Neden Bu Repoyu Seçtim, Buradan Ne Öğrendim?
Veri analitiği ve görselleştirme konularına ilgim olduğu için ve kendi projemizde de görselleştirme tarafını üstlendiğim için **Streamlit** reposunu seçtim. Projeyi incelerken büyük bir açık kaynak projesinin yalnızca kod satırlarından ibaret olmadığını; modüler dosya düzeninin, net Issue/PR başlıklarının ve görselleştirme standartlarının projeyi nasıl sürdürülebilir kıldığını gördüm.

### Kendi Projemde (`fe-gorsel` Rolümde) Kullanabileceğim Fikir
Bizim projemizde benim sorumluluğum **FE (Front-End / Görselleştirme)** rolü kapsamında `generate_visuals.py` betiği ile kampanya verilerinin grafiklerini (`visuals/` altında) üretmektir. **Streamlit**'in arayüz ve veri sunumu yaklaşımından şu fikirleri projemize uygulayabilirim:

1. **İnteraktif Dashboard Mantığı:** İlerleyen süreçte Matplotlib ile ürettiğimiz statik PNG grafiklerini (`gelir-zaman-serisi.png` ve `kanal-kirilim.png`) Streamlit mimarisinden esinlenerek interaktif bir web arayüzüne taşımak harika bir geliştirme adımı olur.
2. **Veri Uyum ve Modülerlik:** Streamlit'in veri kütüphaneleriyle olan sıkı entegrasyonu, bizim tarafımızda da analistimizin (`docs/analiz-g1.md`) hesapladığı metrikler (örneğin E-posta Birleşik ROAS: 45.50x) ile benim `generate_visuals.py` kodumdaki görsel çıktıların her zaman birebir senkronize çalışması gerektiğini gösteriyor.

Mevcut `data/kampanya-performans.csv` dosyamız toplu kampanya-hafta kayıtlarından oluşuyor. **Streamlit** reposundan aldığım temel çıkarım; karmaşık veri setlerini ve analiz sonuçlarını, kullanıcıya en açık, anlaşılır ve görsel olarak doğrulanabilir bir yapıda sunma disiplinidir.
