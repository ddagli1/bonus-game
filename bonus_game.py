from speech import speech_en  # İngilizce konuşmayı tanıyacak fonksiyon içe aktarılıyor
from random import choice, randint  # Rastgele seçim ve sayı üretimi için modüller
import time  # Zaman işlemleri için

# Zorluk seviyelerine göre kelime listeleri
seviyeler = {
    "kolay": ["dairy", "mouse", "computer"],
    "orta": ["programming", "algorithm", "developer"],
    "zor": ["neural network", "machine learning", "artificial intelligence"]
}

# Oyun fonksiyonu: Seçilen zorluk seviyesine göre kelimeleri test eder
def play_game(level):
    words = seviyeler.get(level, [])  # Seçilen seviyeye ait kelimeleri al
    if not words:
        print("Hatalı zorluk seviyesi.")  # Geçersiz seviye kontrolü
        return

    score = 0  # Başlangıç puanı
    num_attempts = 3  # Her kelime için deneme sayısı (şimdilik kullanılmıyor)

    for _ in range(len(words)):
        random_word = choice(words)  # Rastgele bir kelime seç
        print(f"Lütfen kelimeyi telaffuz edin: {random_word}")
        recog_word = speech()  # Konuşmadan gelen kelimeyi tanı
        print(recog_word)  # Tanınan kelimeyi ekrana yazdır

        if random_word == recog_word:
            print("Doğru!")  # Doğru telaffuz
            score += 1
        else:
            print(f"Bir yanlışlık var. Kelime: {random_word}")  # Hatalı telaffuz

        time.sleep(2)  # Yeni kelimeye geçmeden 2 saniye bekle

    print(f"Oyun bitti! Skorunuz: {score}/{len(words)}")  # Oyun sonunda skoru göster

# Kullanıcıdan zorluk seviyesi girmesi istenir
selected_level = input("Zorluk seviyesini seçin (kolay/orta/zor): ").lower()
play_game(selected_level)  # Oyunu başlat
