# Haberleşme Sistemlerinde Anomali Tespiti

Haberleşme sistemlerinde anomali tespiti, bir ağda veya iletişim sisteminde normal davranıştan sapmaların veya beklenmedik durumların tespit edilmesi sürecidir. Bu tür tespitler, siber saldırılar, ağ hataları, performans düşüşleri veya güvenlik ihlalleri gibi istenmeyen durumları belirlemek amacıyla yapılır.

## Anomali Tespiti Neden Önemlidir?

- **Kötü niyetli kullanıcıların sisteme zarar vermesini ve erişmesini önler.**
- **Hata tespiti ve önlem almamızı sağlar.**
- **Trafik akışındaki bozulmaları ve gecikmeleri belirler, önlem alınmasını sağlar.**
- **Trafik akışını ve ağ kaynaklarının verimli kullanılmasını sağlar.**

## Anomali Tespiti Yöntemleri

### İstatistiksel Yöntemler
- **Aritmetik Ortalama**: Verilerin merkezi eğilimi gösterir.
- **Varyans**: Verilerin ortalamadan uzaklıklarının karelerinin ortalamasıdır.
- **Z-Score**: Bir veri noktasının ortalamadan kaç standart sapma uzakta olduğunu gösterir.
- **Histogram Tabanlı Yöntemler**: Verilerin dağılımını görselleştirmek ve analiz etmek için kullanılan grafiksel yöntemdir.

### Parametrik Yöntemler
Verilerin belirli bir dağılıma (genellikle normal dağılım) uyduğu varsayımına dayanır. Örneğin t-testleri, ANOVA, Z-testi.

### Parametrik Olmayan Yöntemler
Verilerin belirli bir dağılıma uyduğu varsayımını yapmaz. Örneğin Mann-Whitney U testi, Kruskal-Wallis testi, Sperman Korelasyonu.

### Makine Öğrenmesi Tabanlı Yöntemler
- **Denetimli Öğrenme (Supervised Learning)**: Eğitim verisi hem normal hem de anormal durumları içerir. (Örnek: SVM, Karar Ağaçları, Yapay Sinir Ağları)
- **Denetimsiz Öğrenme (Unsupervised Learning)**: Eğitim verisi yalnızca normal durumları içerir, anomaliler tespit edilirken bu modelden sapmalar aranır. (Örnek: K-Means, Autoencoders, One-Class SVM, Isolation Forests)
- **Yarı-Denetimli Öğrenme (Semi-Supervised Learning)**: Normal durumların verisi ağırlıklıdır. Az sayıda anomali etiketi bulunabilir.

### Hibrit Yöntemler
İstatistiksel ve Makine Öğrenmesi yöntemlerinin bir arada kullanılmasını sağlar.

## Haberleşme Sistemlerinde Kullanım Alanları

- **Ağ Trafik Analizi**: Şüpheli trafiğin tespiti (DDoS saldırıları, port tarama vb.).
- **IoT (Nesnelerin İnterneti)**: Cihazların davranış analizleri ve saldırı tespiti.
- **SCADA Sistemleri**: Endüstriyel kontrol sistemlerinde güvenliğin sağlanması.
- **Kablosuz Ağlar (WLAN)**: Yetkisiz erişim veya paket manipülasyonu tespiti.
- **Bulut Tabanlı Sistemler**: Servis erişimlerinin anomali bazlı denetlenmesi.

## Uygulama Süreci

1. **Veri Toplama**: Ağ trafiği, sistem logları, protokol analizleri vb.
2. **Öznitelik Çıkarma (Feature Extraction)**: Bağlantı türü, paket büyüklüğü, bağlantı süresi gibi özniteliklerin çıkarılması.
3. **Öznitelik Seçimi (Feature Selection)**: En iyi sonuçları veren özniteliklerin belirlenmesi.
4. **Model Eğitimi**: Seçilen algoritmalarla normal davranış profilinin oluşturulması.
5. **Anomali Tespiti**: Gerçek zamanlı veya çevrimdışı analizlerle anomali durumlarının tespit edilmesi.
6. **Sonuçların Değerlendirilmesi**: Yanlış alarm oranı, algılama oranı gibi metriklerle performans değerlendirmesi.
7. **Model Güncellemesi**: Sistemin dinamiklerine uyum sağlamak için modelin sürekli güncellenmesi.

## Performans Değerlendirme Metrikleri

- **Doğruluk (Accuracy)**
- **Hassasiyet (Precision)**
- **Duyarlılık (Recall)**
- **F1-Skoru (F1-Score)**
- **ROC-Eğrisi ve AUC (Area Under Curve)**

# AWID3 Veri Seti (ALEXA Wireless Intrusion Detection Dataset 3)

AWID3, kablosuz ağlarda güvenlik tehditlerini analiz etmek ve tespit etmek amacıyla kullanılan geniş çaplı bir veri setidir. Bu veri seti, özellikle kablosuz ağlarda anomali tespiti ve saldırı tanıma için geliştirilmiştir. AWID3, çeşitli saldırı türlerinin simülasyonu ile ağ güvenliğini test etmek ve tehditleri tanımak için kullanılır.

## Veri Seti Özellikleri

- **Ağ Trafiği**: AWID3 veri seti, farklı ağ protokollerini içeren kablosuz ağ trafiği verilerini içerir.
- **Saldırı Türleri**: Birçok farklı saldırı türünü içerir, örneğin **Deauthentication (Deauth)**, **Disassociation (Disas)**, **Reassociation (Re-assoc)**, **Rogue Access Point (Rogue_AP)**, **KRACK**, **KR00K**, **Botnet**, **Malware**, **SQL Injection**, **SSDP**, **Evil Twin**, **Website Spoofing** ve daha fazlası.
- **Veri Formatı**: AWID3 veri seti, genellikle **PCAP (Packet Capture)** formatında sunulur, bu da ağ trafiğinin ayrıntılı bir şekilde yakalanmasını sağlar.
- **Ağ Konfigürasyonu**: Veri seti, farklı kablosuz ağ ortamlarını ve cihazları simüle eden veriler sunar.

## Veri Seti Yapısı

AWID3 veri seti, farklı türdeki saldırıların ve normal ağ trafiğinin simüle edilmesiyle oluşturulmuştur. Veri seti, aşağıdaki gibi farklı kategorilerdeki verileri içerir:

1. **Normal Trafik Verisi**: Kablosuz ağlardaki normal kullanıcı trafiği. Bu veriler, ağda saldırı bulunmayan, güvenli ağ trafiğini temsil eder.
2. **Saldırı Trafiği**: Farklı türdeki saldırıların simüle edilerek oluşturulmuş trafik verisi. Her saldırı türü, belirli bir kötü niyetli etkinliği içerir.

### Saldırı Türleri
- **Deauthentication (Deauth)**: Ağdan cihazların zorla çıkarılması amacıyla yapılan saldırılar. Cihazlar, ağ bağlantılarını kaybeder.
- **Disassociation (Disas)**: Bağlantıların sonlandırılması ve yeniden başlatılması amacıyla yapılan saldırılar.
- **Reassociation (Re-assoc)**: Cihazların yeni bir ağ erişim noktasına bağlanması için yapılan saldırılar.
- **Rogue Access Point (Rogue_AP)**: Yasadışı erişim noktalarının ağa dahil edilmesi ve ağ trafiğinin yönlendirilmesi.
- **KRACK (Key Reinstallation Attack)**: WPA2 protokolündeki güvenlik açığını kullanarak, şifrelerin yeniden yüklenmesini sağlayarak saldırı gerçekleştirilmesi.
- **KR00K**: WPA2 protokolündeki başka bir güvenlik açığını kullanarak şifreli ağ trafiğini ele geçirme.
- **Botnet**: Çeşitli cihazlardan oluşan bir ağ üzerinden gerçekleştirilmiş saldırılar.
- **Malware**: Kötü amaçlı yazılımlar kullanılarak ağda zararlı işlemler gerçekleştirilmesi.
- **SQL Injection**: Web uygulamalarındaki güvenlik açıklarını kullanarak veritabanlarına yetkisiz erişim sağlama.
- **SSDP (Simple Service Discovery Protocol)**: SSDP protokolü üzerinden saldırılar ve cihazların hedeflenmesi.
- **Evil Twin**: Sahte bir erişim noktası (AP) kurarak, kullanıcılardan veri toplama veya kötü amaçlı yazılım yayma saldırıları.
- **Website Spoofing**: Gerçek bir web sitesinin taklit edilmesi amacıyla yapılan saldırılar, kullanıcıları kandırarak kimlik bilgileri çalmak için kullanılır.

## Veri Seti Yapısı

AWID3 veri seti, her biri farklı bir saldırıyı temsil eden çok sayıda PCAP dosyası içerir. Her dosya, ağ trafiğini temsil eder ve her bir paket, normal trafik veya belirli bir saldırı türüne işaret eder.

Veri seti aşağıdaki bileşenlere sahiptir:

- **PCAP Dosyaları**: Ağa ait trafik verilerini içerir.
- **Etiketli Veriler**: Her veri örneği (paket) etiketlenmiş olup, normal trafik ve saldırı türleri arasındaki farkları belirtir.
