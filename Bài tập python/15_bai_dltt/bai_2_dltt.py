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