#4. ÖDEV
# Enes GÜNGÖR
# enesgungor.gs@gmail.com
# Quiz Notları: 90-100-100-100-100

class Adamasmaca():
    def __init__(self, secret, guess, lives):
        self.secret = str(input("Gizli Kelimeyi Giriniz: "))
        self.guess = ""
        self.lives = 10

    def start(self):
        while self.lives > 0:
            char_left = 0
            for char in self.secret:
                if char in self.guess:
                    print(char)
                else:
                    print("-")
                    char_left += 1
            if char_left == 0:
                print("\n Kazandınız !!!")
                break
            guess = input("\n Kelime veya harf tahmin  et: ")
            self.guess += guess
            if guess not in self.secret:
                self.lives -= 1
                print("\n Yanlış!")
                print(f"\n {self.lives} hakkın kaldı !")
                if self.lives == 0:
                    print("\n Kaybettiniz!")


Adamasmaca = Adamasmaca('', '', '')
Adamasmaca.start()
