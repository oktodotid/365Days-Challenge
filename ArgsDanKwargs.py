""" # Args (arguments) dan Kwargs (Keyword Arguments) # """

'''
# Args adalah sebuah argument dimana kita dapat memasukkan sekian banyak variable
  tanpa dengan mendefinisikan variable tersebut terlebih dahulu pada fungsi
'''


def jumlah(*angka):
    return sum((angka))
    # Methode SUM hanya bisa digunakan pada object yang bisa
    # diiterasi, seperti list, tuple, dan set


hasil = jumlah(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(hasil)


"""
Kwargs adalah sebuah argument dimana kita dapat memasukkan sekian banyak variable
yang dimana hasil dari variable tersebut akan berupa dictionary

"""


def cek_kwargs(**kwargs):
    print(kwargs)


cek_kwargs(kwargs1='kucing', kwargs2='anjing', kwargs3='kuda')


def hasil_dict(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


hasil_dict(Nama='okto', Umur=20, Hobi='membaca')


''' # Menggabungkan Args dan Kwargs # '''


def fungsiku(*args, **kwargs):
    print(f'Saya ingin membeli {args[2]} buah {kwargs["buah"]}')


fungsiku(2, 3, 4, 1, buah='apel', sayur='bayam')
