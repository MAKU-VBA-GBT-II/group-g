import random
import os

def generate_random_numbers():
    # 1'den 100'e (dahil) 10 rastgele sayı üret
    numbers = [random.randint(1, 100) for _ in range(10)]
    
    # data klasörünü kontrol et ve oluştur
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
    os.makedirs(output_dir, exist_ok=True)
    
    file_path = os.path.join(output_dir, 'prova-dilara.csv')
    
    # CSV dosyasına tek sütun halinde yaz (başlık: deger)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("deger\n")
        for num in numbers:
            f.write(f"{num}\n")
            
    print(f"Başarıyla 10 rastgele sayı {file_path} dosyasına yazıldı.")

if __name__ == "__main__":
    generate_random_numbers()
