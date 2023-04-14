keranjang = [1,2.3,'Belajar Python',True]
print(len(keranjang)) # Menghitung jumlah elemen yang ada di dalam list

# Menggunakan for loop untuk mengakses elemen yang ada di dalam list
for i in range(len(keranjang)):
    print(keranjang[i])


# Mengubah isi list

keranjang = [1,2.3,'Belajar Python',True]

keranjang[2] = 'lapar'
print(keranjang)

# Mengubah isi list dengan append dan meletakkan elemen di akhir list
keranjang = [1,2.3,'Belajar Python',True]
keranjang.append('mangga')
print(keranjang)

# Menampilkan index terakhir pada list
keranjang = [1, 2.3, 'Belajar Python', True, 'mangga']
keranjang.pop()
print(keranjang)


## Nested List adalah list yang berisi list lainnya
#Contoh:

isi = [1,2,3,4,5,[6,7,8,[9,10,11,'target',12]]]
target = isi[5][3][3] # Mengakses elemen target dalam nested list
print(target)

# Membuat Nested list dari 2 list yang berbeda

ganjil = [1,3,5,7,9]
genap = [2,4,6,8,10]

nested = [ganjil,genap]
print(nested)

# Mengeluarkan elemen dari list atau Iterasi list 
for i in ganjil:
    print('Bilangan :', i)
