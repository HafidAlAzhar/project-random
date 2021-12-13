# Import File Secara Spesifik
from function import say_hello
from function import total

hello = say_hello("Hafid")
print(hello)

hasil = total(1,2,3,4)
print(hasil)

# Import File Sekaligus
import function

hello = function.say_hello("Hafid")
print(hello)

hasil = function.total(1,2,3,4)
print(hasil)


