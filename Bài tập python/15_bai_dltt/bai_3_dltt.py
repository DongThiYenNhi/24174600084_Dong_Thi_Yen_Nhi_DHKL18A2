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