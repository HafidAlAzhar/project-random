banyak = int(input("Ingin berapa banyak data : "))

nama = []
umur = []

for i in range(0, banyak):
    print(f"Data ke {i}")
    input_nama = input("Masukan nama : ")
    input_umur = int(input("Masukan Umur : "))

    nama.append(input_nama)
    umur.append(input_umur)

print(nama)
print(umur)