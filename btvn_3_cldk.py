a=float(input("Nhập số a: "))
b=float(input("Nhập số b: "))
c=float(input("Nhập số c: "))
if a > b and a > c:
    print(" a là số lớn nhất")
if b > c and b > a:
    print(" b là số lớn nhất")
if c > a and c > b:
    print(" c là số lớn nhất")
if a==c and a >b:
    print("a và c là số lớn nhất")
if a==b and a > c:
    print("a và b là số lớn nhất")
if b==c and b > a:
    print("b và c là số lớn nhất")