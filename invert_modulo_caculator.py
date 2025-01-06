import math
print ("|---------Modulo calulator : a * i mod b  while i < b---------|")
print ("|                                                             |")
a = float(input("| Enter number a : "))
b = float(input("| Enter number b : "))
i = 1
while i<b:
    if a * i % b == 1:
        break
    i += 1
print (f"|\t\t\t\t\t\t Results : {i}  |")
print ("|-------------------------------------------------------------|")
