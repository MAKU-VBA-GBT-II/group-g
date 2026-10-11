import random
import os

def generate_random_number():
  # 1 ile 100 arasında 10 rastgele sayı üret
  numbers = [random.randint(1, 100) for _ in range(10)]
  
  # 1. Ekrana tek sütun halinde yazdır (İlk satır: deger) 
  print("deger")
  for num in numbers:
    print(num)

  #2. data klasörünü oluştur ve CSV dosyasına da kaydet
  output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
  os.makedirs(output_dir, exist_ok=True)

  file_path = os.path.join(output_dir, 'prova-ceren.csv')

  with open(file_path, 'w', encoding='utf-8') as f:
      f.write("deger\n")
      for num in numbers:
          f.write(f"{num}\n")
        
   print(f"\nBaşarıyla kaydedildi: {file_path}")

if __name__ == "__main__":
    generate_random_numbers()




  
  
