#Bai 3:
A=[]
B=[]
while True:
    n =(input("Nhap vao so nguyen duong n: "))
    if n.isdigit() == False:
        print("Yeu cau nhap lai so nguyen duong!!")
    else:
        n = int(n)
        break
    
for i in range(1, n):
    if i % 2 !=0:
        A.append(i)
        A.sort(reverse=True)
    else:
        B.append(i)
        B.sort(reverse=True)

print(f"Danh sách số lẻ nhỏ hơn n: {A}")
print(f"Danh sách số chẵn nhỏ hơn n: {B}")
#Bai 6:
m=int(input("Nhập vào số hàng của ma trận: "))
n=int(input("Nhập vào số cột của ma trận: "))
A=[]
for i in range(m):
    hang=[]
    for j in range(n):
        hang.append(int(input(f"Nhập phần tử A[{i+1}][{j+1}]: ")))
    A.append(hang)
print("Ma trận A là:")
for i in range(m):
    for j in range(n):
        print(A[i][j],end="\t")
    print()
#Bai 8:
m = int(input("Nhap vao hang i: "))
n = int(input("Nhap vao hang J: "))
A=[]
for i in range(m):
    hang=[]
    for j in range(n):
        hang.append(int(input(f"Nhập phần tử A[{i+1}][{j+1}] ")))
    A.append(hang)
    
c1 = int(input("Nhập chỉ số cột c1 với 1 <= c <= n: ")) - 1
c2 = int(input("Nhập chỉ số cột c2 với 1 <= c <= n: ")) - 1 
if c1 < 0 and c1 >= n or c2 < 0 and c2 >= n:
    print(" Chỉ số cột khong hợp lệ")
else:
    for hang in A:
        hang[c1],hang[c2]=hang[c2],hang[c1]
        
    print("Ma trận sau khi đảo cột:")
    for i in range(m):
        for j in range(n):
            print(A[i][j], end="\t")  
        print() 
#Bai 9 
m=int(input("Nhập vào số hàng ma trận A: "))
n=int(input("Nhập vào số cột ma trận A cũng như số hàng ma trận B: "))
h=int(input("Nhập vào số cột ma trận B: "))
A=[]
for i in range(m):
    hang_A=[]
    for j in range(n):
        hang_A.append(int(input(f"Nhập phần tử A[{i+1}][{j+1}]: ")))
    A.append(hang_A)
B=[]
for j in range(n):
    hang_B=[]
    for e in range(h):
        hang_B.append(int(input(f"Nhập phần tử B[{j+1}][{e+1}]: ")))
    B.append(hang_B)
C=[[0]*h]*m
for i in range(m):
    for j in range(h):
        for l in range (n):
            C[i][j]=A[i][l]+B[l][j]
print("Tổng hai ma trận A và B là")
for hang in C:
    print(hang)

for i in range(m):
    for j in range(h):
        for l in range (n):
            C[i][j]=A[i][l]-B[l][j]
print("Hiệu hai ma trận A và B là")
for hang in C:
    print(hang)

for i in range(m):
    for j in range(h):
        for l in range (n):
            C[i][j]=A[i][l]*B[l][j]
print("Tích hai ma trận A và B là")
for hang in C:
    print(hang)
k=int(input("Nhập vào 1 số k: "))
for i in range (m):
        for j in range(n):
            A[i][j] *=k
print("Ma trận A sau khi nhân với số k")
for hang in A:
    print(hang)
#Bai 11:
ten = ['Dung', 'Quang', 'Trang']
diem = [10.0, 5.3, 7.5]
print("Tên    Điểm")
for i in range(len(ten)):  
    print(ten[i], diem[i])  



    

