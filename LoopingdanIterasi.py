""" # Penggunaan Looping FOR #"""


angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
for i in angka:
    total = total + i
    print(f'Hasil Penjumlahan Pada Iterator ke {i} adalah {total}')

for i in angka:
    total = total + i
print(f'Hasil Total Pengjumlahan 1 - {len(angka)} adalah {total}')

""" # Penggunaan Looping dan Conditional #"""

urutan = 0
for item in 'saya belajar pyhon':
    urutan += 1
    if item == 'a':
        print(f'Karakter {item} ditemukan pada urutan ke {urutan}')


""" # Tantangan #"""

angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in angka:
    if i % 2 == 0:
        print(f'Angka {i} adalah bilangan genap')
    else:
        print(f'Angka {i} adalah bilangan ganjil')


""" # For Loop Dengan Tuple dan List Multiple Items #"""

box1 = ((1, 2), (3, 4), (5, 6))

# Tupples Unpacking / Mengeluarkan Item Yang Ada Di Dalam Tupples
for a, b in box1:
    print(a, b, end=' ')

# List Unpacking / Mengeluarkan Item Yang Ada Di Dalam List

box2 = [[1, 2], [3, 4], [5, 6]]

for a, b in box2:
    print(a, b, end=' ')
