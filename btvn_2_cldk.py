print("Nhập điểm toạ độ điểm M")
x=float(input("Nhập điểm x: "))
y=float(input("Nhập điểm y: "))
print("Nhập toạ độ điểm I")
a=float(input("Nhập điểm a: "))
b=float(input("Nhập điểm b: "))
r=float(input("Nhập bán kính R "))
IM=((x-a)**2 +(y-b)**2)**1/2
if IM <= r:
    print(True)
else:
    print(False)
print("Kết thúc chương trình")


