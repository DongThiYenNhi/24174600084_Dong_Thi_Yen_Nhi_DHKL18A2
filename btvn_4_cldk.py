print("Nhập ba cạnh a,b,c của tam giác với cạnh c nhập là cạnh lớn nhất nếu có giá trị lớn nhất")
a=float(input("Nhập cạnh a: "))
b=float(input("Nhập cạnh b: "))
c=float(input("Nhập cạnh c: "))
if a==b and b==c and a==c:
    print("Đây là tam giác đều")
if a**2 + b**2 == c**2:
    print("Đây là tam giác vuông")
if a+b>c and a+c>b and b+c>a and a==b and a != c:
    print("Đây là tam giác cân")
if a**2 + b**2 == c**2 and a==b:
    print("Đây là tam giác vuông cân")
if a+b>c and a+c>b and b+c>a and a!=b and a**2 + b**2 != c**2:
    print("Đây là tam giác thường")
if a+b <= c or a+c <= b or b+c <= a:
    print("Đây không phải bộ ba cạnh của một tam giác")
    