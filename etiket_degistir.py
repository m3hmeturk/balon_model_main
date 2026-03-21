import os
import glob

# Etiketlerin (txt dosyalarının) bulunduğu klasörler
klasorler = ["train/labels", "valid/labels", "test/labels"]

degistirilen_dosya_sayisi = 0

for klasor in klasorler:
    if not os.path.exists(klasor):
        continue
        
    # Klasördeki tüm .txt dosyalarını bul
    txt_dosyalari = glob.glob(os.path.join(klasor, "*.txt"))
    
    for dosya in txt_dosyalari:
        with open(dosya, "r") as f:
            satirlar = f.readlines()
            
        with open(dosya, "w") as f:
            for satir in satirlar:
                parcalar = satir.strip().split()
                if len(parcalar) > 0:
                    # Ne olursa olsun ilk rakamı 0 yap (Yani tek sınıf: balloon)
                    parcalar[0] = "0"
                    f.write(" ".join(parcalar) + "\n")
        degistirilen_dosya_sayisi += 1

print(f"BİTTİ! Toplam {degistirilen_dosya_sayisi} dosyadaki tüm renkler tek bir sınıfa (0) dönüştürüldü.")