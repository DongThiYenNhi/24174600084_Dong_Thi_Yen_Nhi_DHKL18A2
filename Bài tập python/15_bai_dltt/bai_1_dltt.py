#Bai 1:
ds_nguyen_to = []
while True:
    n = input("Nhap vao so nguyen duong n: ")
    if n.isdigit() == False:
        print("Yeu cau nhap lai so nguyen duong!!")
    else:
        n = int(n)
        break

for i in range(1, n):
    if i == 1:
        ds_nguyen_to.append(i)
        continue
    for j in range(1,i):
        if i%j == 0 and j != 1 and i != j:
            break
    else:
        ds_nguyen_to.append(i)
ds_nguyen_to.sort()
print(ds_nguyen_to)
#Bai 2:
ds_so=[]
while True:
    n = input("Nhap vao so phan tu n trong danh sach: ")
    if n.isdigit() == False:
        print("Yeu cau nhap lai so nguyen duong!!")
    else:
        n = int(n)
        break

for i in range(n):
    while True:
        so = input(f"Nhap gia tri so thu {i + 1}: ")
        if so.count('-')==1 and so.replace('-',' ').isdigit:
             so = float(so)
        else:
            print("Yêu cầu nhập lại số")
ds_so.append(so)
tong = sum(ds_so)
print(f"Tong cac so vua nhap: {tong}")
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
#Bai