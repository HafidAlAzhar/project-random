# Game Penjumlahan

a = int(input("Silahkan masukan angka 1 : "))
b = int(input("Silahkan masukan angka 2 : "))

hasil = (a + b)

jwb = int(input(f"Jumlahkan Angka Angka Berikut {a} + {b} : "))

if jwb == hasil:
    print("Selamat jawaban anda benar")
else:
    print(f"Jawaban Anda Salah, Jawaban yang benar adalah: {hasil}")