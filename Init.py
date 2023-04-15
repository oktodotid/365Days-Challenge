class Kulkas:
    # Class Object attribute (attribute ini bersifat global untuk class kulkas)
    penjual = 'Toko Elektronik - Pak Eko'

    def __init__(self, merk, harga):
        self.merk = merk
        self.harga = harga
        self.garansi = 3
        self.tenaga = 'listrik'

    def tegangan(self):
        print('500 Watt')

    def laku(self):
        print(f'Barang {self.merk} sudah laku dengan harga Rp.{self.harga}')

    def karyawan(self, nama):
        print(f'Karyawan {nama} menjual barang {self.merk}')


barang1 = Kulkas('Samsung', 300)

"""
Untuk memanggil methode diluar fungsi __init__ 
harus menggunakan tanda () setelah nama methodnya.
"""
# Contoh:
barang1.tegangan()
print(barang1.harga)
barang1.laku()
barang1.karyawan('Budi')
# Methode 'karyawan' memiliki argumen nama dan harus memasukkan argumen tersebut.
# Jika tidak, maka akan terjadi error karena argumen nama belum diisi dan berada di luar fungsi __init__.


class Lingkaran:
    # koefisien phi
    phi = 3.14

    def __init__(self, jari):
        self.jari = jari

    def keliling(self):
        return 2 * self.phi * self.jari

    def luas(self):
        return self.phi * self.jari * self.jari


l1 = Lingkaran(10)

print(l1.keliling())
print(l1.luas())
