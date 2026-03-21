import cv2
from ultralytics import YOLO

def ana_fonksiyon():
    # 1. Eğittiğimiz o harika beyni yüklüyoruz!
    # Uyarı: Eğer terminalde 'train2' veya 'train3' içine kaydettim derse, buradaki yolu ona göre güncelle.
    model_yolu = "runs/detect/train/weights/best.pt"
    model = YOLO(model_yolu)

    # 2. Bilgisayarın kamerasını başlatıyoruz (0 genelde laptop'ın kendi kamerasıdır)
    kamera = cv2.VideoCapture(0)

    print("--- KAMERA AÇILIYOR... ---")
    print("Çıkmak ve kamerayı kapatmak için klavyeden 'q' tuşuna basın.")

    while True:
        # Kameradan anlık kareyi (frame) al
        basarili_mi, kare = kamera.read()
        if not basarili_mi:
            print("Kameradan görüntü okunamadı!")
            break

        # 3. Alınan kareyi yapay zekaya ver ve balon var mı diye sor!
        # conf=0.5 demek: "Sadece %50 ve üzeri eminsen hedefi işaretle" (Hatalı atışları önler)
        sonuclar = model.predict(kare, conf=0.5, verbose=False)

        # 4. Yapay zekanın bulduğu hedeflerin üzerine kutu çizilmiş halini al
        cizilmis_kare = sonuclar[0].plot()

        # 5. Ekranda göster (TEKNOFEST havası katalım pencere adına!)
        cv2.imshow("MIGFER-AI Hedef Tespiti (Balon)", cizilmis_kare)

        # 'q' tuşuna basılırsa döngüden çık
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # İş bitince kamerayı serbest bırak ve pencereleri kapat
    kamera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    ana_fonksiyon()