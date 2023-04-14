# Comparasion Operator Berantai

# Ada 3 Argument yang digunakan Untuk Comparasion Operator Berantai yaitu :

"""
1. and --> Jika kedua argument bernilai True maka hasilnya True
2. or --> Jika salah satu argument bernilai True maka hasilnya True
3. not --> Jika argument bernilai True maka hasilnya False dan Sebaliknya
"""

# Contoh :
a = 3 > 2 and 2 < 1
b = 3 > 2 or 2 < 1
print(a)
print(b)

# Ada 3 Argument yang digunakan untuk conditional yaitu :

"""
1. if --> Jika argument bernilai True maka akan menjalankan statement dibawahnya
2. elif --> Jika argument bernilai True maka akan menjalankan statement dibawahnya
3. else --> Jika argument bernilai False maka akan menjalankan statement dibawahnya
"""

# Contoh :

angka = int(input('Masukkan Angka : '))
angka2 = int(input('Masukkan Angka : '))

if angka < angka2:
    print('Angka Pertama Lebih Kecil Dari Angka Kedua')
elif angka == angka2:
    print('Angka Pertama Sama Dengan Angka Kedua')
else:
    print('Angka Pertama Lebih Besar Dari Angka Kedua')
