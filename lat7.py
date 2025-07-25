def cek_genap(angka):
    if angka % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"

a = int(input("Masukkan angka: "))
print("Angka kamu adalah:", cek_genap(a))
