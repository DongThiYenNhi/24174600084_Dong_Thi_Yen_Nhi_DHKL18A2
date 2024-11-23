#Bài 1:
tong_s = 0
n = int(input("Nhap vao gia tri nguyen duong n: "))
for i in range(n + 1):
    tong_s = tong_s + i 
print(f"Tong cac so tu 1 den n= {tong_s}")
#Bài 2:
for i in range(100):
    if i % 2 != 0:
        print(i)
#
n = int(input("Nhập giá trị n: "))
S2 = 1
for i in range(1, n):
    S2 *= i
print("Kết quả của S2 là:", S2)
#
n = int(input("Nhập giá trị n: "))
S3 = 0
for i in range(1, n+1):
    S3 += ((-1)**(i+1)) / i
print(f"Tổng S3 là: {S3}")
#
n = int(input("Nhập giá trị n: "))
tong = 0
for k in range(n + 1):  
    tong += k / (k + 2)
print("Tổng là:", tong)
#Bài 3:
a=0
b=1
for i in range(50):
    print(a)
    a,b = b, a+b
#Bài 4:
n = int(input("Nhap vao so nguyen duong: "))
if n <= 1:
    print("So nay khong phai la so nguyen to")
else:
    k = n
    for i in range(n):
        if n % k == 0 and k != n and k != 1:
            print("So nay khong phai la so nguyen to")
            break
        k = k - 1
    else:
        print("So nay la so nguyen to")
#Bài 5:
n=int(input("Nhập số n: "))
so_hoan_hao=0
for i in range(n):
    if i==0:
        continue
    if n % i == 0:
        so_hoan_hao += i
if so_hoan_hao == n:
    print("Đây là số hoàn hảo")
else:
    print("Đây không phải số hoàn hảo")

#Bài 6:
n=int(input("Nhập số n: "))
if n <= 0:
    print("Đây không phải số chính phương")
else:
    for i in range(n):
         if i**2 == n:
             print("Đây là số chính phương")
             break
    else:
        print("Đây không phải số chính phương")
#Bài 7:
n = int(input("Nhập vào số nguyên n: "))
for num in range(2,n):
    so_nguyen_to = True  
    can_bac_hai =int((num**0.5)+1)
    for i in range(2,can_bac_hai):
        if num % i == 0:
            so_nguyen_to = False
            break
    if so_nguyen_to:
        print(num)
#Bài 8:
n = int(input("Nhập vào n: "))
print(f"Các số hoàn hảo nhỏ hơn {n} là:")
for num in range(1, n):
    so_hoan_hao = 0
    for i in range(1, num):
        if num % i == 0:
            so_hoan_hao += i
    if so_hoan_hao == num:
        print(num, end=" ")

#Bài9:
n = int(input("Nhập số nguyên n: "))
for i in range(1, n):
    if i * i < n:
        print(i * i)
#Bài10:
a= int(input("Nhap vao so nguyen duong a: " ))
b = int(input("Nhap vao so nguyen duong b: " ))
min_num = a
if b <= a:
    min_num = b
k = min_num
for i in range(min_num):
    if a % k == 0 and b % k == 0:
        print(f"{k} la uoc chung lon nhat")
        break
    k = k - 1
#Bài 11:
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
for i in range(max(a, b), a * b + 1):
    if i % a == 0 and i % b == 0:
        bcnn = i
        break
print("Bội chung nhỏ nhất của", a, "và", b, "là:", bcnn)
#Bài 12:
tuso = int(input("Nhập tử số: "))
mauso = int(input("Nhập mẫu số: "))
if mauso == 0:
    print("Mẫu số không thể bằng 0!")
else:
    ucln = 1  
    for i in range(1, min(abs(tuso), abs(mauso)) + 1):
        if tuso % i == 0 and mauso % i == 0:
            ucln = i  
    tuso_toi_gian = tuso // ucln
    mauso_toi_gian = mauso // ucln
    print(f"Phân số tối giản là: {tuso_toi_gian}/{mauso_toi_gian}")
#Bài 13:
n = int(input("Nhập vào một số: "))
print(1, end="")
for i in range(2, n + 1):
    for _ in range(n // i):
        if n % i == 0:
            print("*", i, end="")
            n = n // i
print()
#Bài 14:
n = int(input("Nhập số hàng cho tam giác Pascal: "))
for i in range(n):
    print(" " * (n - i), end="")
    C = 1  
    for j in range(i + 1):
        print(C, end=" ")
        C = C * (i - j) // (j + 1)  
    print() 
#
n = int(input("Nhập số hàng cho tam giác Floyd: "))
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print() 
#Bài 15:
num = int(input("Nhập số ở hệ cơ số 10: "))
nhi_phan = ""
if num == 0:
    nhi_phan = "0"
else:
    for i in range(num, 0, -1):
        nhi_phan= str(num % 2) + nhi_phan
        num = num // 2
print("Số trong hệ cơ số 2 là:", nhi_phan)
    
    
