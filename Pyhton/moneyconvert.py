# Input
print(">>> Selamat datang di Moneyconvert <<<")
usd = int(input("Silahkan masukan nilai Dollar (USD) : "))

# Option
print("1. --IDR")
print("2. --JPY")
print("3. --MYR")
print("4. --EUR")
option = int(input("Silahkan masukan pilihan diatas 1-4 : "))

# Function
if option == 1:
    result = usd * 14410
    print(f"{usd} USD = {result} IDR")
elif option == 2:
    result = usd * 113.52
    print(f"{usd} USD = {result} JPY")
elif option == 3:
    result = usd * 4.23
    print(f"{usd} USD = {result} MYR")
elif option == 4:
    result = usd * 0.89
    print(f"{usd} USD = {result} EUR")

    


