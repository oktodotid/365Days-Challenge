"""
# Function
- Dituliskan dengan cara sebagai berikut:

def nama_fungsi(argumen/variable):
    statement/perintah yang diinginkan
    return/print

Catatan:
    - Return digunakan untuk mendefenisikan hasil fungsi ke variable
    - Print digunakan jika hanya ingin mencetak hasil fungsi    
"""

# Contoh Sederhana :
""" Note: Untuk menjalankan fungsi,
cukup dengan menuliskan nama fungsi dan menambahkan tanda kurung () """


def cetak_kalimat():
    print('Halo Dunia')


cetak_kalimat()

""" Note: Hasil dari perkalian a*b akan dikembalikan dari hasil fungsi ke variable
    sehingga nilai dapat dipanggil/dijalankan dengan menuliskan nama fungsi tersebut
"""


def perkalian(a, b):
    return a*b


hasil = perkalian(2, 3)
print(hasil)


def deteksi_genap(var1):
    if var1 % 2 == 0:
        return ('Genap')
    else:
        return ('Ganjil')


hasil2 = deteksi_genap(5)
print(hasil2)


kata = input('Masukkan kata: ')


def cek_kata(kata):
    if 'python' in kata:
        return ('Ada')
    else:
        return ('Tidak Ada')


hasil3 = cek_kata(kata)
print(hasil3)
