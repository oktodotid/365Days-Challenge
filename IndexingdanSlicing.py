# Pada String python dapat membaca index pada string
# Misalnya 'Ini Python'
# Maka Indexnya adalah
# Kata       : 'I n i   P y t h o n'
# Index Maju :  0 1 2 3 4 5 6 7 8 9
# Index Mundur: 0 -9 -8 -7 -6 -5 -4 -3 -2 -1

#Contoh:

bil1 = 'IniPython'

print(bil1[0])
print(bil1[0:4]) # Memanggil dari index 0 sampai 3
print(bil1[4:]) # Memanggil dari index 4 sampai akhir
print(bil1[:4]) # Memanggil dari index awal sampai 3
print(bil1[-1]) # Memanggil dari index terakhir
print(bil1[0:6:2]) # Memanggil dari index 0 sampai 5 dengan step/Jarak 2 (Penulisan [awal,akhir,jarak])

#Contoh Memanipulasi String

messsage = 'Hello World'
print("Message Baru : ", messsage[:6] + 'Sayang')

#Indexing pada List

item = [1,2,3,4,5,6,7,8,9,10]

print(item[3:6]) # Memanggil dari index 3 sampai 5
