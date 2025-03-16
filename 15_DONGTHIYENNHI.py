#Bai1:
#a,
n = int(input("Nhap vao so nguyen duong n: "))
while n <= 0:
    print("Yeu cau nhap lai")
S4 = 0
i = 1
while i <= n:
    S4 += i**2
    i += 1
print(f"S4 = {S4}")
#n=4,S4=30
#b,
n = int(input("Nhap vao so nguyen duong n: "))
while n <= 0:
    print("Yeu cau nhap lai")
S5 = 0
i = 1
while i <= n:
    S5 += (2 * i - 1) ** 3  
    i += 1
print(f"S5 = {S5}")
#n=2,S5=28
#c;
n = int(input("Nhap vao so nguyen duong n: "))
while n <= 0:
    print("Yeu cau nhap lai")
S6 = 0
i = 1
while i <= n:
    S6 += (2*i)**4
    i += 1
print(f"S6 = {S6}")
#n=2,S6=272
#Bai2..........................................................
#a.
n = int(input("Nhập vào số nguyên dương n: "))
while n <= 0:
    print("Yêu cầu nhập lại.")
    n = int(input("Nhập vào số nguyên dương n: "))
S = 0
i = 1  
while i <= n:
    if i % 2 == 1: 
        S += 1/i
    else:  
        S -= 1/i
    i += 1 
print(f"Tổng S = {S}")
#n=3 , S = 0,8333333333
#b,
n = int(input("Nhập vào số nguyên dương n: "))
while n <= 0:
    print("Yêu cầu nhập lại.")
    n = int(input("Nhập vào số nguyên dương n: "))
S = 0
i = 2  
while i <= n:
    S += 1 / (i * (i + 1))  
    i += 1  

print(f"Tổng S = {S}")
#n=2,s= 0.16666666666666666
#c, 
n = int(input("Nhập vào số nguyên dương n: "))
while n <= 0:
    print("Yêu cầu nhập lại.")
    n = int(input("Nhập vào số nguyên dương n: "))
S = 0
i = 2  
while i <= n:
    S += 1 / (i**(1/2)) 
    i += 1  
print(f"Tổng S = {S}")
#n=3, S=1.2844570503761732
#Bai3:......................................................

#Bai4:.........................................................
tu_so = float(input("Nhập tử số: "))
while True:
    mau_so = float(input("Nhập mẫu số: "))
    if mau_so == 0:
        print("Mẫu số = 0, vui long nhap lai")
    else:
        break 
print(f"Phân số bạn nhập là: {tu_so}/{mau_so}")
# tu so=2 ,mau so=3 , in ra ket qua 2/3 
#Bai5:...................................................................
n= float(input("Nhập so bat ki : "))
while True:
    if n < 0:
        print(" Da nhap so am,dung viec nhap so")
        break
    else:
        n= float(input("Nhập so bat ki : "))
# nhap lan 1= 2 , nhap lan 2= 3 , nhap lan 3=  - 1 (hien thi dong lenh " Da nhap so am,dung viec nhap so" )
#Bai6:...........................................................
so  = input("Nhập một số: ")
chu = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
ket_qua = ""
i = 0
while i < len(so):
    chu_so= int(so[i])
    if i == len(so) - 1:
        ket_qua += chu[chu_so]
    else:
        ket_qua += chu[chu_so] + " "
    i += 1
print(ket_qua)
# so=123 , ket_qua= một hai ba
#Bai 7:.............................................................
a = int(input("Nhap so nguyen duong thu 1: "))
b = int(input("Nhập so nguyen duong thu 2: "))
if a > b:
    a, b = b, a
bcnn = b
while bcnn % a != 0:
    bcnn += b  
print(f"Bội chung nhỏ nhất của {a} và {b} là {bcnn}")
#a=4 , b=6 ,bcnn=12 
#Bai8:.............................................
ky_tu = input("Nhập một ký tự: ")
while len(ky_tu) != 1:
    print("Vui lòng nhập chỉ một ký tự.")
    ky_tu = input("Nhập một ký tự: ")
ASCII = ord(ky_tu)
print(f"Giá trị ASCII của '{ky_tu}' là: {ASCII}")
# ky_tu= a , ASCII = 97 
#Bai9...............................................
so = int(input("Nhap mot so nguyen bat ky : "))
tong=0
while so != 0:
    tong += so % 10 
    so//= 10 
print(f"Tổng các chữ số là: {tong}")
#so=12 , tong=3 
#Bai10:..................................................
so = input("Nhập một số thập phân: ")
chu = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
ket_qua = ""
if '.' in so:
    phan_nguyen, phan_thap_phan = so.split('.')
else:
    phan_nguyen = so
    phan_thap_phan = ""
i = 0
while i < len(phan_nguyen):
    chu_so = int(phan_nguyen[i])
    if i == len(phan_nguyen) - 1:
        ket_qua += chu[chu_so]
    else:
        ket_qua += chu[chu_so] + " "
    i += 1
if phan_thap_phan:
    ket_qua += " chấm "
    i = 0
    while i < len(phan_thap_phan):
        chu_so = int(phan_thap_phan[i])
        if i == len(phan_thap_phan) - 1:
            ket_qua += chu[chu_so]
        else:
            ket_qua += chu[chu_so] + " "
        i += 1
print(ket_qua)
#so=0.12 , ket_qua= không chấm một hai
#Bai11:.........................................................
print( "MENU :Chọn đồ uống")
print("1. Cafe")
print("2. Cam vắt")
print("3. Nước ép cà rốt") 
print("4. Nước lọc")
print("5. Nước dừa") 
print("6. Thoát")
while True:
    chon = int(input("Nhập số để chọn đồ uống: "))
    if chon == 1:
        print("Bạn đã chọn Cafe.")
    elif chon == 2:
        print("Bạn đã chọn Cam vắt.")
    elif chon ==3:
        print("Bạn đã chọn Nước ép cà rốt.")
    elif chon == 4:
        print("Bạn đã chọn Nước lọc.")
    elif chon== 5:
        print("Bạn đã chọn Nước dừa.")
    elif chon == 6:
        print("Ban da thoat ")
        break 
    else:
        print( "Vui lòng chọn lại.")
#chon =1 , Ban da chon cafe

