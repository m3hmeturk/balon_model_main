from ultralytics import YOLO

if __name__ == '__main__':
    # YOLOv11'in en hızlı modeli olan Nano'yu indirip kuruyoruz
    model = YOLO("yolo11n.pt")

    print("--- EĞİTİM BAŞLIYOR (RTX 4050 DEVREDE) ---")
    
    # Parametreleri tam senin sistemine (README'deki 512x512'ye ve 6GB VRAM'e) göre ayarladık
    results = model.train(
        data="data.yaml", 
        epochs=50,       # Şimdilik 50 tur atalım, test için fazlasıyla yetecek
        imgsz=512,       # README'den yakaladığımız o 512 optimizasyonu!
        batch=16,        # RTX 4050'nin 6GB hafızasını hiç kasmayacak miktar
        device=0,        # 0 = Nvidia GPU kullan demek
        workers=2,       # Windows sistemlerde arka plan çökmesini engeller
        plots=True       # İş bitince bize başarı grafiklerini çizecek
    )