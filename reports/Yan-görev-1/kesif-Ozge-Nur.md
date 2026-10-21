**İncelenen repo:** https://github.com/github/gitignore

# Git Keşfi: github/gitignore

## Çözdüğü problem

Git, klasördeki her dosyayı takip etmeye çalışır. Oysa her projede repoya yüklenmesi gerekmeyen dosyalar olur: Python'un çalışırken oluşturduğu geçici dosyalar, işletim sisteminin ya da editörün bıraktığı dosyalar, şifre içeren ayar dosyaları gibi. Bunları yüklememek için projelerde `.gitignore` dosyası kullanılır.

Bu dosyayı her seferinde sıfırdan yazmak hem zaman alır hem de eksik satır bırakma riski taşır. `github/gitignore` bu problemi hazır şablonlarla çözer: GitHub'ın hazırladığı ve GitHub'da yeni repo açarken şablon seçicisini besleyen bir şablon koleksiyonudur.

## Güçlü yanları

- **Düzenli klasör yapısı:** Dil ve araca özel şablonlar ana klasörde, işletim sistemi ve editör şablonları `Global` klasöründe, daha özel projelerin şablonları `community` klasöründe durur. İhtiyacı olan şablonu bulmak kolaydır.
- **Anlaşılır içerik:** Python şablonunu açtığımda `__pycache__` gibi satırları gördüm. Her satır "şu dosya ya da klasör repoya yüklenmesin" anlamına geliyor, açıklama satırları (`#`) bölümleri ayırıyor.
- **Kaliteyi koruyan katkı kuralları:** Herkes Pull Request açabiliyor ama koleksiyonun amacı her projeyi kapsamak değil, en yaygın ve yararlı şablonları derlemek. Bu yüzden her istek kabul edilmiyor, katkılar belirli kurallara uymak zorunda.
- **Büyük bir topluluk:** Çok yüksek yıldız ve fork sayısı, şablonların yaygın biçimde kullanıldığını gösteriyor.

## Kendi projemde kullanabileceğim fikir

- Grup deposumuzdaki (`group-g`) `.gitignore` dosyasını bu repodaki Python şablonuyla karşılaştırıp eksik satır var mı (örneğin `__pycache__/`) kontrol etmek. Veri üreten Python betikleri çalıştırdığımız için bu geçici dosyaların repoya girmemesi önemli.
- Şablonlardaki gibi bölümlere ayrılmış ve açıklama satırlı bir `.gitignore` kullanmak, ekip üyelerinin dosyayı daha kolay anlamasını sağlar.
- Katkı kuralları fikrini ekibimizde de uygulamak: `AGENTS.md` ve Issue yorumlarıyla zaten "kim ne yapacak, nasıl teslim edilecek" kurallarımız var. Bu repo, kuralların yazılı ve herkes tarafından görülebilir olmasının işe yaradığını gösteriyor.
