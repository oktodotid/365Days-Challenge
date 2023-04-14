"""
LEGB adalah urutan eksekusi Python untuk mencari variabel.
Dimana Pyhton akan mengeksekusi/mencari variabel dari lingkup terdalam hingga keluar.
Sesuai urutannya Local -> Enclosing -> Global -> Built-in

# L --> adalah singkatan dari local yang dimana variable ini bersifat local,
        yang biasanya berada didalam fungsi(def/lambda tertentu).
         
# E --> adalah singkatan dari Enclosing function locals dimana variable ini
        berada didalam fungsi(def/lambda) mulai dari lingkup terdalam hingga keluar.
        
# G --> adalah singkatan dari Global (module) dimana variable ini berada diluar fungsi(def/lambda),
        biasanya di tahap awal.

# B --> adalah singkatan dari Built-in (Python) dimana variable ini berada diluar fungsi(def/lambda),
        biasanya di tahap awal seperti list,str,upper,dll
"""

# Contoh :

kalimat = "Ini adalah kalimat global"  # Variable Global


def cetak():
    kalimat = "Ini adalah kalimat lokal"  # Variable Local

    def eksekusi():
        print('Halo hasilnya adalah : ', kalimat)

    eksekusi()


cetak()  # Fungsi akan terlebih dahulu mengeksekusi variable Local


namaKucing = 'Meow'  # GLobal Variable


def rubahNamaKucing(namaBaru):
    global namaKucing  # Global Variable
    namaKucing = namaBaru  # Local Variable
    print(f'saya rubah nama kucing menjadi {namaKucing}')


rubahNamaKucing('Ketty')
