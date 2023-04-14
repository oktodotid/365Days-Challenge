# Tuples bersifat immutable(tidak dapat diubah isinya) tapi bisa di iterasi dan memiliki indeks

keranjangt = (1, 2, 'jeruk', 5)

# Mengubah isi tuples

list1 = list(keranjangt)
print(list1)

list1[2] = 'berubah'
keranjangt = tuple(list1)

print(keranjangt)


# Methode Pada Tuples

t1 = (1, 2, 3, 4, 5, 2, 2, 2, 2)
l1 = [1, 2, 3, 4, 5]

print(t1.count(2))  # Menghitung jumlah item 2 pada tuples

# Mengecek Type Data Tuples

t1 = 1, 2, 3, 4, 'jeruk'

print(type(t1))


# Multiple Assignment and Tuples

a, b, c, d = 1, 2, 3, 4

print(a, b, c, d)

tas = ['rambutan', 23, 15, 33, [1, 2, 3, 4]]

item1, item2, item3, item4, item5 = tas

print(item1)
print(item5)

# SET $$

set1 = set()
set1.add('jeruk')

print(set1)

list_angka = [12, 3213, 442]
set2 = set(list_angka)
print(set2)
