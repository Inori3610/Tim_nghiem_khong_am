

def giaipt(xa,xb,da,db):
    n = da*db
    print(f"n = d1 * d2 = {da} * {db} = {n}")
    print (f"He PT co nhiem duy nhat trong khoang tu [0,{n-1}] co dang : ")
    print ("x = (n / d1 * x1 * y1 + n / d2 * x2 * y2) mod n ")
    y1 = 1
    y2 = 1 
    while y1<da:
        if db * y1 % da == 1:
            break
        y1 += 1
    while y2<db:
        if da * y2 % db == 1:
            break
        y2 += 1
    print (f"y1 = d2^-1 mod d1 = {d2}^-1 mod {d1} = {y1}")
    print (f"y2 = d1^-1 mod d2 = {d1}^-1 mod {d2} = {y2}")
    print (f"x = {n} / {da} * {xa} * {y1} + {n} / {db} * {xb} * {y2} = {(n/da*xa*y1+n/db*xb*y2)%n}")
    


print("Tim ngiem khong am cua phuong trinh sau")
print(" { x = x1 mod d1")
print(" { x = x2 mod d2")
print("----X-----------------------")
x1 = int(input("Enter x1 : "))
x2 = int(input("Enter x2 : "))
print("----D-----------------------")
d1 = int(input("Enter d1 : "))
d2 = int(input("Enter d2 : "))
giaipt(x1, x2, d1, d2)
