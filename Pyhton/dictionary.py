# Tipe data Dictionary

customer = {"Name":"Hafid", "Age":15, "Addres":"Subang" } #customer = {"key":"value"}

nama = customer["Name"]
age = customer["Age"]
addres = customer["Addres"]

for key in customer:
    value = customer[key]
    print(f"{key}: {value}")

