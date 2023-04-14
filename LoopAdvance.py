""" RANGE """

# Pembuatan list dengan range

for i in range(1, 21):  # (awal, akhir, step)
    print(i)

for i in range(1, 21, 2):  # (awal, akhir, step)
    print(i)


""" ENUMERATE """
# Adalah menunjukan index di for loop

# Contoh Penunjukan index pada for loop tanpa enumerate

index = 0
for item in 'abcdefghij':
    print(f'Karakter "{item}" berada di index Ke - {index}')
    index += 1

# Contoh Penunjukan index pada for loop dengan enumerate

kata = 'abcdefghij'

for item in enumerate(kata):
    print(item)

""" ZIP """
# Menggabungkan 1 atau lebih list

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']

print('=== Menggabungkan 2 list dengan zip ===')
for item in zip(list1, list2):
    print(item)

""" 
Catatan: Enumerate dan Zip Outputnya Berupa Tuple
Jika Ingin Mengubahnya Menjadi List, Gunakan List()

"""

""" # Item Checking # """

# Mengecek Keys dan Values pada Dictionary

kotak = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}

a = 'c' in kotak.keys()
print(a)

b = 100 in kotak.values()
print(b)


""" Pembuatan List Dengan For Loop """

isi = [item for item in range(1, 11)]
print(isi)

isi2 = [item*2 for item in range(1, 11)]
print(isi2)

isi3 = [item**2 for item in range(1, 11)]
print(isi3)

isi4 = [item for item in range(1, 31) if item % 2 == 0]
print(isi4)
