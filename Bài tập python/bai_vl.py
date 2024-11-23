#Bài 1:
r=float(input("Nhập bán kính khối trụ :"))
h=float(input("Nhập chiều cao khối trụ :"))
if h > 0 and r > 0:
    pi = 3.14
    dtxq= (2*pi*r*h)
    dttp= (2*pi*r**2) + dtxq
    tt= (pi*r**2)*h
    print(f" Diện tích xung quanh của khối trụ là: {dtxq:.2f}")
    print(f" Diện tích toàn phần của khối trụ là: {dttp:.2f}")
    print(f" Thể tích của khối trụ là: {tt:.2f}")
else:
    print(" Giá trị nhập không thoả mãn")
print(" Ket thuc chuong trinh")
#Bài 2:
x=float(input("Nhập số x: "))
if  x**4 + 1 > 0:
     t= -x + (x**2+4)**(1/2)
     m= (x**4+1)**(1/7)
     f= t/m
     print(f"Giá trị của biểu thức là {f:.2f}")
else:
    print("Giá trị không thoả mãn")
print(" Kết thúc chương trình")
#Bài 4:
tgsd=float(input("Nhập thời gian sử dụng của bóng đèn: "))
if tgsd > 0:
    U=220
    I=2.7
    P=U*I
    gd=7000
    tien_dien=(P/3600000)*tgsd*gd
    print(f"Số tiền điện phải trả là: {tien_dien}")
else:
    print(" Giá trị nhập không thoả mãn")
print(" Ket thuc chuong trinh")
#Bài 8:
import math
x=float(input("Nhập giá trị x: "))
if x > 0 and x != 1:
    fx= math.log(x,4) + math.log(2,x)
    print(f" Giá trị của biểu thức là: {fx:.2f}")
else:
    print(" Giá trị nhập không thoả mãn")
print(" Ket thuc chuong trinh")


