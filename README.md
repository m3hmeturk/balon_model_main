# 🎈 Teknofest Hava Savunma Sistemi: YOLO Balon Tespit Modeli

Bu depo, **Teknofest Çelikkubbe Hava Savunma Sistemleri** yarışması kapsamında otonom hedef tespiti ve takibi yapabilmek amacıyla geliştirilmiş özel bir nesne tanıma (Object Detection) projesini içermektedir. 

Proje, hava savunma sisteminin "hedef" olarak belirlediği balonları gerçek zamanlı ve yüksek doğrulukla tespit edebilmesi için en güncel YOLO (You Only Look Once) mimarileri kullanılarak eğitilmiştir.

## ✨ Öne Çıkan Özellikler

* **Özel Veri Seti Eğitimi:** Hava savunma senaryolarına uygun olarak toplanan ve etiketlenen verilerle baştan model eğitimi (`egitim.py`).
* **Farklı YOLO Mimarileri:** Sistem gereksinimlerine ve işlemci gücüne göre optimize edilmiş farklı ağırlık dosyaları (`yolo11n.pt`, `yolo11s.pt`).
* **Gerçek Zamanlı Test:** Canlı kamera akışı üzerinden modelin anlık hedef tespit performansını ölçen test modülü (`kamera_test.py`).
* **Dinamik Veri Yönetimi:** Veri seti etiketlerini proje standartlarına göre otomatik düzenleyen yardımcı araçlar (`etiket_degistir.py`).

## 📁 Proje Yapısı


📦 balon_model_main
 ┣ 📂 runs/detect        # Eğitim sonuçları, loglar ve grafik çıktıları
 ┣ 📂 train              # Eğitim için kullanılan veri seti (Görseller ve etiketler)
 ┣ 📂 valid              # Doğrulama (Validation) için ayrılan veri seti
 ┣ 📜 data.yaml          # Veri seti yollarını ve sınıf isimlerini içeren yapılandırma dosyası
 ┣ 📜 egitim.py          # YOLO modelini kendi veri setimizle eğiten ana script
 ┣ 📜 etiket_degistir.py # Bounding box etiketlerini formatlayan ön işleme betiği
 ┣ 📜 kamera_test.py     # Eğitilmiş modeli kamera ile canlı test etme scripti
 ┣ 📜 yolo11n.pt         # YOLO Nano ön eğitimli/eğitilmiş ağırlık dosyası (Hızlı)
 ┗ 📜 yolo11s.pt         # YOLO Small ön eğitimli/eğitilmiş ağırlık dosyası (Dengeli)


 🚀 Kullanım
Gereksinimleri Yükleyin:
Projeyi çalıştırmak için Python ortamınızda ultralytics ve opencv-python kütüphanelerinin kurulu olması gerekmektedir.

pip install ultralytics opencv-python
Modeli Eğitme:
Kendi veri setinizle eğitimi başlatmak için data.yaml dosyasını kontrol edip aşağıdaki betiği çalıştırın:

python egitim.py
Kamera ile Canlı Test:
Eğitilen modelin ağırlıklarını kullanarak bilgisayar kamerası veya harici bir kamera üzerinden hedef tespiti yapmak için:

python kamera_test.py
🎯 Proje Hedefi
Bu model, Miğfer takımının otonom hava savunma kulesi için kritik bir "göz" görevi görmektedir. Arduino ve motor sürücüleri ile haberleşecek olan bu sistem, görüntü işleme algoritmasından gelen koordinat (Bounding Box) verilerini kullanarak hedefi merkeze alacak ve atış kontrol/takip algoritmalarını tetikleyecektir.

👨‍💻 Geliştirici & Takım
Mehmet - Miğfer Takımı Erzincan Binali Yıldırım Üniversitesi
