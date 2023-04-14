# Dictionary adalah object berpasangan yang tidak memiliki urutan
# Pengambilan item pada dictionary dilakukan dengan cara menggunakan 'key'
# Contoh:

dict1 = {
         'k1':'ayam',
         'k2':'kambing',
         'k3':'sapi'
         }

# Mengakses item (value) pada dictionary
print(dict1['k1']) # Mengakses item dengan key 'k1'

daftar_harga = {
                'kijang innova':250,
                'avanza':200,
                'vios':150
                }

daftar_harga['avanza'] = 300 # Mengubah item dengan key 'avanza'
print(daftar_harga['avanza'])

# Dictionary dalam Dictionary
dict2 = {
    'k1':100,
    'k2':200,
    'k3':300,
    'k4':{'buah1':'apel','buah2':'jeruk'}
         }

print(dict2['k4']['buah2']) # Mengakses item dengan key 'k4' dan 'buah2'

print(dict2['k4']['buah1'].upper()) # Mengakses item dengan key 'k4' dan 'buah1' dan mengubah menjadi huruf kapital
