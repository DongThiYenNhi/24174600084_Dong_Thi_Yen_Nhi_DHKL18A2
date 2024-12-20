#Bai 1:
def is_integer_string(a):
    if a.isdigit() or a[0]=='-' and a[1:].isdigit():
        return True
    else:
        return False
    
a=input("Nhập vào chuôĩ số bất kì: ")
if is_integer_string(a):
    print("Đây là chuỗi số nguyên")
else:
    print("Đây ko la chuoi so nguyen")
    
#Bai 2:
def kiem_tra_so_nguyen_duong(a):
    if a.isdigit() and int(a) > 0:
        return True
    else:
        return False
    
a=input("Nhập vào một chuỗi bất kì: ")
if kiem_tra_so_nguyen_duong(a):
    print("Đây là chuỗi số dương")
else:
    print("Đây là ko là chuỗi số dương")
#Bai 3:
def kiem_tra_so_thuc(a):
    if a.count('.') == 1 and a.replace('.','').isdigit() or a[0]=='-' and a[1:].replace('.','').isdigit():
         return True
    else:
        return False
    
a=input("Nhập vào một chuỗi bất kì: ")
if kiem_tra_so_thuc(a):
    print("Đây là chuỗi số thuc")
else:
    print("Đây là ko là chuỗi số thuc")

#Bai 4:
def kiem_tra_so_nguyen_to(x):
    if x < 2:
         return False
    
    for i in range(2, x):
         if x % i == 0:
            return False
    else:
       return True

x = int(input("Nhap vao so nguyen bat ki: "))
if kiem_tra_so_nguyen_to(x):
     print("Day la so nguyen to")
else:
     print("Day khong la so nguyen to")
#Bai 5:
def kiem_tra_so_chinh_phuong(a):
    for i in range(a + 1):
        if i**2 == a:
            return True
    else:
        return False
    
a=int(input("Nhập vào số a: "))
if kiem_tra_so_chinh_phuong(a):
    print("Đây là số chính phương")
else:
    print("Đây ko là số chính phương")
#Bai 6:
def kiem_tra_so_hoan_hao(a):
    if a <= 1:
        return False

    tong = 0 
    for i in range(1, a+1):
        if a % i == 0: 
            tong += i
    return tong == a

a=int(input("Nhập vào số a: "))
if kiem_tra_so_hoan_hao(a):
    print("Đây la so hoan hao ")
else:
    print("Đây ko la so hoan hao")
    
#Bai 7:
def tim_ucln(a,b):
    so_be = min(a,b)
    for k in range(so_be, 0, -1):
        if a % k == 0 and b % k == 0:
            return k 
a=int(input("Nhập vào số a: "))
b=int(input("Nhập vào số b: "))
ucln = tim_ucln(a,b)
if ucln:
    print(f"{ucln} là ước chung lớn nhất của {a} và {b} ")
else:
    print("Hai số ko có ước chung lớn nhất")   
#Bai 8:
uoc = []
def tim_uoc(a):
    for i in range(1, a + 1):
        if a % i == 0: 
            uoc.append(i)
            
    return uoc
a=int(input("Nhập vào số a: "))
uoc = tim_uoc(a)
print(f"Các ước của {a} là: {uoc}")

#Bai 9:
def toi_gian_phan_so(tu_so, mau_so):
    for i in range(min(tu_so,mau_so)):
        if tu_so % i == 0 and mau_so % i == 0:
            ucln = i
            break
    tu_so_toi_gian = tu_so // ucln
    mau_so_toi_gian = mau_so // ucln
    if mau_so_toi_gian < 0:
        tu_so_toi_gian = -tu_so_toi_gian
        mau_so_toi_gian = -mau_so_toi_gian
    return tu_so_toi_gian, mau_so_toi_gian 
tu_so = int(input("Nhập tử số: "))
mau_so = int(input("Nhập mẫu số: "))
tu_so_toi_gian, mau_so_toi_gian = toi_gian_phan_so(tu_so, mau_so)
print(f"Phân số tối giản là: {tu_so_toi_gian}/{mau_so_toi_gian}")
#Bài 10:

#Bai 11:
def tinh_tong_day_so():
    tong = 0
    while True:
            so = input("Nhập số nguyên (hoặc gõ 'kt' để kết thúc): ")
            if so.lower() == 'kt':
                break
            so = int(so)
            tong += so
            print("Vui lòng nhập một số nguyên hợp lệ hoặc 'dừng' để kết thúc.")
    return tong
tong = tinh_tong_day_so()
print(f"Tổng của dãy số bạn nhập là: {tong}")
#Bài 12:
def tinh_tich_day_so():
    tich = 1
    while True:
            so = input("Nhập số nguyên (hoặc gõ 'kt' để kết thúc): ")
            if so.lower() == 'kt':
                break
            so = int(so)
            tich *= so
            print("Vui lòng nhập một số nguyên hợp lệ hoặc 'dừng' để kết thúc.")
    return tich
tich = tinh_tich_day_so()
print(f"Tích của dãy số bạn nhập là: {tich}")
#Bai 13:
def phan_tich_thua_so_nguyen_to(n):
    thua_so = []  
    while n % 2 == 0:
        thua_so.append(2)
        n = n // 2  
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            thua_so.append(i)
            n = n // i 
    if n > 2:
        thua_so.append(n)
    
    return thua_so
n = int(input("Nhập vào một số nguyên để phân tích thành thừa số nguyên tố: "))
thua_so = phan_tich_thua_so_nguyen_to(n)
print(f"Phân tích thừa số nguyên tố của {n} là: {thua_so}")
#Bai 14:
import math
def kiem_tra_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def trung_binh_day_so_nguyen_to(danh_sach_so):
    so_nguyen_to = [so for so in danh_sach_so if kiem_tra_so_nguyen_to(so)]
    
    if len(so_nguyen_to) == 0:
        return "Không có số nguyên tố trong dãy."
    trung_binh = sum(so_nguyen_to) / len(so_nguyen_to)
    return trung_binh
danh_sach_so = list(map(int, input("Nhập dãy số nguyên (cách nhau bởi dấu cách): ").split()))

trung_binh = trung_binh_day_so_nguyen_to(danh_sach_so)
print(f"Giá trị trung bình của các số nguyên tố trong dãy là: {trung_binh}")
#Bai 15:
def kiem_tra_so_hoan_hao(n):
    if n <= 1:
        return False
    tong = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            tong += i
    return tong == n

def so_hoan_hao_nho_nhat(danh_sach_so):
    so_hoan_hao = [so for so in danh_sach_so if kiem_tra_so_hoan_hao(so)]
    
    if not so_hoan_hao:
        return "Không có số hoàn hảo trong dãy."
    
    return min(so_hoan_hao)
danh_sach_so = list(map(int, input("Nhập dãy số (cách nhau bởi dấu cách): ").split()))

ket_qua = so_hoan_hao_nho_nhat(danh_sach_so)
print(f"Số hoàn hảo nhỏ nhất trong dãy là: {ket_qua}")

    
            
        
        


       
            
        
        


    

