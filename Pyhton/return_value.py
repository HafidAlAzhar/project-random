# Belajar Method Return Value

def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    print(f"Total {list_angka} = {total}")
    return total
total = jumlahkan(10, 10 ,10)

# Mengambil data total
print(total)
