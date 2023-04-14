""" ## While LOOP ##"""

"""
Ada 3 Argument yang biasa digunakan pada While Loop:
1. Break --> Untuk menghentikan Loop
2. Continue --> Untuk melanjutkan Loop ke Iterator selanjutnya
                dan melewati iterator saat ini.
3. Pass --> Tidak Melakukan apa-apa
"""

"""
Penulisan While Loop:

while (sebuak kondisi=True):
    eksekusi/statement
"""

# Contoh:

index = 0
while True:
    print('Saya sedang belajar Python')
    index += 1
    if index == 10:
        break

x = 0

while x < 50:
    print('Angka Kelipatan 2 : ', x)
    x += 2


""" CONTINUE """

angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in angka:
    if item % 2 == 0:
        continue
    else:
        print('Angka Ganjil : ', item)
