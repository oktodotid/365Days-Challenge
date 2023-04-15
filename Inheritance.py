"""
Inheritance adalah sebuah konsep dimana sebuah class dapat mewarisi
semua method dan property dari class lain
"""


class Mahasiswa:
    status = "Mahasiswa"

    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

    def keterangan(self):
        print(f'{self.nama} dikelas {self.kelas} adalah {self.status}')


joko = Mahasiswa("Joko", "12")
joko.keterangan()

# Jika ingin melakukan pewarisan class (inheritance) Mahasiswa ke class Nilai
# Maka def __init__ nya harus sama dan menggunakan fungsi super()


class Nilai(Mahasiswa):
    def __init__(self, nama, kelas):
        super().__init__(nama, kelas)
        self.nilai_update = []

    def input_nilai(self, tambah):
        return self.nilai_update.append(tambah)


budi = Nilai("Budi", "12")
budi.input_nilai(100)
"""
Untuk mengeksekusi methode dari class Inheritance, tidak perlu menambahkan tanda ()
"""
print(budi.nilai_update)
