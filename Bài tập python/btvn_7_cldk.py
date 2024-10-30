print("Nhập hệ phương trình")
a1 = float(input("Nhập a1: "))
b1 = float(input("Nhập b1: "))
c1 = float(input("Nhập c1: "))
a2 = float(input("Nhập a2: "))
b2 = float(input("Nhập b2: "))
c2 = float(input("Nhập c2: "))
D = a1 * b2 - a2 * b1
if D == 0:
    D1 = c1 * b2 - c2 * b1
    D2 = a1 * c2 - a2 * c1
    if D1 == 0 and D2 == 0:
        print("Hệ phương trình có vô số nghiệm.")
    else:
        print("Hệ phương trình vô nghiệm.")
else:
    Dx = c1 * b2 - c2 * b1
    Dy = a1 * c2 - a2 * c1
    x = Dx / D
    y = Dy / D
    print(f"Nghiệm của hệ phương trình là: x = {x}, y = {y}")