from ultralytics import YOLO

if __name__ == '__main__':
    # Nano (n) yerine daha zeki olan Small (s) modelini indiriyoruz
    model = YOLO("yolo11s.pt")

    print("--- 🚀 MİĞFER-AI: MAKSİMUM DOĞRULUK İÇİN ULTRA EĞİTİM BAŞLIYOR 🚀 ---")
    
    results = model.train(
        data="data.yaml", 
        
        # --- 1. TEMEL VE SÜRE AYARLARI ---
        epochs=150,           # Eğitimi çok daha uzun tutuyoruz (150 tur)
        patience=30,          # KRİTİK: Eğer 30 tur boyunca zeka gelişmezse, ezberlememesi (overfitting) için eğitimi en zirvede otomatik keser.
        imgsz=640,            # Yüksek çözünürlük
        batch=16,             # Ekran kartı hafıza sınırı
        device=0,             # RTX 4050 Devrede
        workers=2,            
        plots=True,           
        
        # --- 2. GELİŞMİŞ ÖĞRENME ALGORİTMALARI ---
        cos_lr=True,          # Öğrenme hızını sona doğru yumuşatır, hedefe milimetrik oturmasını sağlar.
        warmup_epochs=5,      # Modele ilk 5 tur "ısınma" yaptırır, ani ağırlık sapmalarını önler.
        
        # --- 3. ZORLU EĞİTİM ŞARTLARI (ŞARTNAMEYE ÖZEL) ---
        hsv_h=0.1,            # Renk tonunu rastgele değiştirir (Renk ezberini bozar, sadece şekle odaklanır)
        hsv_s=0.7,            # Doygunluğu değiştirir (Farklı kameralardaki solukluklar için)
        hsv_v=0.4,            # Parlaklığı değiştirir (Güneş parlaması veya gölge simülasyonu)
        degrees=15.0,         # Fotoğrafları sağa sola yatırır (Rüzgarda savrulan balonlar için)
        translate=0.1,        # Hedefi kadrajda kaydırır
        scale=0.5,            # Hedefi büyütüp küçültür (Uzak/yakın menzil algısı)
        mosaic=1.0,           # 4 fotoğrafı birleştirip tek fotoğraf yapar (Zorlu arka planlarda bulmasını sağlar)
        erasing=0.4           # Bazen balonun bir kısmını siyah kareyle kapatır (Yarı gizli/kesilmiş balonları bulsun diye)
    )