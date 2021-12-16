# Sisa bagi

bil1 = int(input("Silahkan masukkan bilangan 1 : "))
bil2 = int(input("Silahkan masukkan bilangan 2 : "))

hasil = bil1 % bil2

if hasil == 0:
    print(f"Hasil sisa bagi adalah '{hasil}' dan termasuk bilangan Genap")
elif hasil == 1:
    print(f"Hasil sisa bagi adalah '{hasil}' dan termasuk bilangan Ganjil")