#Bài 1:
Nam=int(input("Nhập năm: "))
if Nam % 4 == 0 and Nam % 10 != 0 or Nam % 400 == 0:
    print("Năm này là năm nhuận")
else:
    print("Năm này là năm không nhuận")
print("Kết thúc chương trình")
#Bài 2:
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
#Bài 3:
a=float(input("Nhập số a: "))
b=float(input("Nhập số b: "))
c=float(input("Nhập số c: "))
if a > b and a > c:
    print(" a là số lớn nhất")
if b > c and b > a:
    print(" b là số lớn nhất")
if c > a and c > b:
    print(" c là số lớn nhất")
if a==c and a >b:
    print("a và c là số lớn nhất")
if a==b and a > c:
    print("a và b là số lớn nhất")
if b==c and b > a:
    print("b và c là số lớn nhất")
#Bài 4:
print("Nhập ba cạnh a,b,c của tam giác với cạnh c nhập là cạnh lớn nhất nếu có giá trị lớn nhất")
a=float(input("Nhập cạnh a: "))
b=float(input("Nhập cạnh b: "))
c=float(input("Nhập cạnh c: "))
if a==b and b==c and a==c:
    print("Đây là tam giác đều")
else:
    print("Đây k la tam giac deu")
#Bài 5:
ky_tu=input("Nhập một ký tự trên bàn phím: ")
if ky_tu == 'u' or ky_tu == 'o' or ky_tu == 'e' or ky_tu == 'i' or ky_tu == 'a':
    print(" Đây là nguyên âm")
else:
    print("Đây là phụ âm")
#Bài 6:
print(" Menu phim chiếu của rạp ABC")
print("1. Phim tình cảm, 2. Phim kinh dị, 3.Phim hoạt hình, 4.Phim khoa học viễn tưởng")
option = input("Nhập lựa chọn của bạn từ 1-4: ")
if option == '1':
    print("Bạn đã chọn Phim tình cảm.")
elif option == '2':
    print("Bạn đã chọn Phim kinh dị.")
elif option == '3':
    print("Bạn đã chọn Phim hoạt hình.")
elif option == '4':
    print("Bạn đã chọn Phim khoa học viễn tưởng.")
elif option == '0':
    print("Thoát chương trình.")
else:
    print("Lựa chọn không hợp lệ.")
#Bài 7:
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
#Bài 8:
Diem=input("Nhập điểm của bạn từ A-F: ")
if Diem== 'A':
    print(" Bạn đạt loại xuất sắc")
if Diem== 'B':
    print("Bạn đạt loại giỏi")
if Diem=='C':
    print("Bạn đạt loại khá")
if Diem== 'D':
    print("Bạn đạt loại trung bình")
if Diem== 'E':
    print("Bạn đạt loại yếu")
if Diem== 'F':
    print("Bạn đạt loại kém")
#Bài 9:
loai_xe = int(input("Nhập loại xe (4 hoặc 7): "))
khoang_cach = float(input("Nhập khoảng cách (km): "))
thoi_gian_cho = int(input("Nhập thời gian chờ (phút): "))

if loai_xe == 4:
    gia_mo_cua = 11000 / 0.8
    if khoang_cach <= 0.8:
        cuoc_phi = gia_mo_cua
    elif khoang_cach <= 20:
        cuoc_phi = gia_mo_cua + (khoang_cach - 0.8) * 12100
    else:
        cuoc_phi = gia_mo_cua + (19.2 * 12100) + ((khoang_cach - 20) * 10000)
elif loai_xe == 7:
    gia_mo_cua = 13000 / 0.8
    if khoang_cach <= 0.8:
        cuoc_phi = gia_mo_cua
    elif khoang_cach <= 30:
        cuoc_phi = gia_mo_cua + (khoang_cach - 0.8) * 14100
    else:
        cuoc_phi = gia_mo_cua + (29.2 * 14100) + ((khoang_cach - 30) * 12000)
else:
    cuoc_phi = None
    print("Loại xe không hợp lệ!")
if cuoc_phi is not None:
    if thoi_gian_cho > 5:
        tien_cho = (thoi_gian_cho - 5) * 800
    else:
        tien_cho = 0

    tong_cuoc = cuoc_phi + tien_cho
    print(f"Cước taxi phải trả là: {tong_cuoc:.0f} đồng")
#Bài 10:
luong = float(input("Nhập lương nhân viên (VNĐ): "))
if luong > 15000000:
    thue = luong * 0.30
elif 7000000 <= luong <= 15000000:
    thue = luong * 0.20
else:
    thue = luong * 0.10
luong_rong = luong - thue
print(f"Thuế thu nhập: {thue:.2f} VNĐ")
print(f"Lương ròng: {luong_rong:.2f} VNĐ")

