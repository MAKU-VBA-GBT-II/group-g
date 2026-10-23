# Yan Görev: Açık Kaynak Repo İncelemesi

* **İncelediğim repo:** [matplotlib/matplotlib](https://github.com/matplotlib/matplotlib)
* **İnceleme tarihi:** 23 Ekim 2026

Python ile veri görselleştirme için kullanılan açık kaynak Matplotlib kütüphanesini inceledim. Projemizdeki `generate_visuals.py` betiği de Matplotlib kullanarak kampanya verilerinden PNG grafikler oluşturuyor.

## Çözdüğü problem

Sayısal veriler satır ve sütunlar hâlinde incelendiğinde zaman içindeki değişimler veya kategoriler arasındaki farklar kolayca fark edilmeyebilir. Matplotlib, Python verilerinden çizgi grafiği, çubuk grafik ve benzeri görseller üretmeyi sağlar. Böylece analiz sonuçları daha anlaşılır biçimde sunulabilir. Matplotlib'in GitHub açıklamasına göre kütüphane statik, animasyonlu ve etkileşimli görselleştirmeleri destekler.

## Güçlü yanları

- **Farklı grafik türleri:** Zaman serileri ve kategori karşılaştırmaları gibi farklı veri ihtiyaçlarına yönelik grafikler oluşturulabilir.
- **Grafik üzerinde ayrıntılı kontrol:** Başlık, eksen adları, açıklamalar, renkler, işaretçiler ve kılavuz çizgileri ayarlanabilir.
- **Python veri araçlarıyla kullanım:** Projemizde olduğu gibi pandas ile okunan ve gruplanan veriler Matplotlib kullanılarak görselleştirilebilir.
- **Dosyaya çıktı alma:** Grafikler PNG gibi görsel dosyalara kaydedilebilir; bu da analiz sonuçlarının raporlarda ve sunumlarda kullanılmasını kolaylaştırır.
- **Dokümantasyon ve katkı süreci:** Depoda kullanım dokümantasyonu, testler ve katkı bilgileri bulunur.

## Kendi projemde kullanabileceğim fikir

Projemizdeki `generate_visuals.py` betiği kampanya verisini pandas ile okuyup iki PNG grafik üretiyor: haftalık toplam gelir zaman serisi ve kanala göre birleşik ROAS karşılaştırması. Bu incelemeden şu fikirleri projemizde uygulayabilirim:

1. **Grafikleri anlaşılır hâle getirme:** Başlık, eksen adları ve ölçü birimlerini açıkça yazarak grafiği ek açıklama olmadan da okunabilir hâle getirmek.
2. **Analizle tutarlılığı koruma:** Grafiklerde kullanılan gruplama ve metrik hesaplarının `docs/analiz-g1.md` içindeki yöntemlerle aynı olduğunu kontrol etmek. Örneğin kanal ROAS'ını toplam gelir / toplam harcama olarak göstermek.
3. **Çıktıları düzenli üretme:** Grafikleri `visuals/` klasörüne anlamlı dosya adlarıyla kaydetmek ve sunumda kullanılacak çözünürlüğü belirlemek.
4. **Grafikleri çıktıdan önce gözden geçirme:** Eksen etiketlerinin, değerlerin ve ölçeklerin grafik üzerinde doğru ve okunaklı göründüğünü kontrol etmek.

Matplotlib'i incelemek, projemizdeki görselleştirmenin yalnızca grafik üretmekten ibaret olmadığını; doğru metriklerin seçilmesi ve sonuçların anlaşılır sunulmasının da önemli olduğunu gösterdi.
