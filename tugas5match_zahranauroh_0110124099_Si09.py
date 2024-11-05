import math

def hitung_luas(bangun, *param):
    match bangun:
        case "persegi":
            sisi = param[0]
            luas = sisi ** 2
            return luas
        case "lingkaran":
            jari_jari = param[0]
            luas = math.pi * jari_jari ** 2
            return luas
        case "segitiga":
            alas, tinggi = param
            luas = (alas * tinggi) / 2
            return luas
        case _:
            return "Bangun datar tidak dikenali."

# Contoh penggunaan
bangun = input("Masukkan jenis bangun datar (persegi, lingkaran, segitiga): ").lower()

if bangun == "persegi":
    sisi = float(input("Masukkan panjang sisi persegi: "))
    print(f"Luas persegi: {hitung_luas(bangun, sisi)}")
elif bangun == "lingkaran":
    jari_jari = float(input("Masukkan jari-jari lingkaran: "))
    print(f"Luas lingkaran: {hitung_luas(bangun, jari_jari)}")
elif bangun == "segitiga":
    alas = float(input("Masukkan panjang alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))
    print(f"Luas segitiga: {hitung_luas(bangun, alas, tinggi)}")
else:
    print("Jenis bangun datar tidak valid.")
