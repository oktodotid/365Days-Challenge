# Methode Built in Python

var = 'Belajar Python'

var = var.upper() # Mengubah semua huruf menjadi huruf besar
print(var)

var = var.lower() # Mengubah semua huruf menjadi huruf kecil
print(var)

var = var.split() # Memisahkan kata pada string
print(var)

# Penggunaan Methode split sangat penting pada NLP
# NLP = Natural Language Processing yang digunakan pada Machine Learning
var = 'Belajar Python'
var = var.split('a') # Memisahkan kata pada string dengan pemisah hufur 'a' dan memasukkannya ke dalam list
print(var)

var = [3,2,8,4,10,6,7,1,4,9]
var.sort() # Mengurutkan huruf pada string
print(var)

## Formatting String ##

nilai1 = 10
nilai2 = 20

print(f'Nilai 1 adalah {nilai1} dan Nilai 2 adalah {nilai2}') # Menggunakan format-string

class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def showInfo(self):
        print(f'Nama Hero : {self.name}, Health: {self.health}')
Hero1 = Hero('Ucup', 100)
Hero1.showInfo() # Memanggil methode showInfo(showInfo adalah methode yang ada di dalam class Hero)
