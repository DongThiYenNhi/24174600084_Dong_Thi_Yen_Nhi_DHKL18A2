#Bai 1:
n=int(input("Nhap vao nam: "))
if n %4==0 and n % 100 !=0 or n%400==0:
    print("Day la nam nhuan")
else:
    print("Day la nam khong nhuan")
#.................................
#Bai 2:
x=int(input("Nhap vao x cua diem M: "))
y=int(input("Nhap vao y cua diem M: "))
a=int(input("Nhap vao a cua diem I: "))
b=int(input("Nhap vao b cua diem I: "))
r=int(input("Nhap vao ban kinh r: "))
MI= ((a-x)**2+(b-y)**2)**(1/2)
if MI==r:
    print(f"MI={MI},Diem M nam tren duong tron tam I")
elif MI>r:
    print(f"MI={MI},Diem M nam ngoai duong tron tam I")
else: 
    print(f"MI={MI},Diem M nam trong duong tron tam I")
#...................................
#Bai 3:
a=float(input("Nhap vao canh thu nhat cua tam giac: "))
b=float(input("Nhap vao canh thu hai cua tam giac: "))
c=float(input("Nhap vao canh thu ba cua tam giac: "))
if a+b>c and a+c>b and b+c>a:
    print("Day la bo ba canh cua tam giac")
else:
    print("Day khong phai bo ba canh cua tam giac")
if a==b and b==c and c==a:
    print("Day la tam giac deu")
elif a==b and a!=c or a==c and a!=b or b==c and b!=a:
    print("Day la tam giac can")
elif a**2 + b**2 == c**2 or a**2 + c**2 ==b**2 or b**2 +c**2==a**2:
    print("Day la tam giac vuong")
elif a==b and a**2 + b**2 == c**2 or a==c and a**2 + c**2 ==b**2 or b==c and b**2 +c**2==a**2:
    print("Day la tam giac vuong can")
#.....................................
#Bai 4:
a=int(input("Nhap vao so thu nhat: "))
b=int(input("Nhap vao so thu hai: "))
c=int(input("Nhap vao so thu ba: "))
if a>=b and a>=c:
    print(f"{a} la so lon nhat")
elif b>=a and b>=c:
    print(f"{b} la so lon nhat")
elif c>=a and c>=b:
    print(f"{c} la so lon nhat")
elif a==b and a==c and b==c:
    print(f"{a} la so lon nhat")
#.......................................
#Bai 5:
n=input("Nhap vao ki tu bat ky tren ban phim: ").lower()
if n=='u' or n=='e' or n== 'o' or n=='a' or n=='i':
    print("Day la nguyen am")
elif n.isalpha():
    print("Day la phu am")
else:
    print("Day khong phai nguyen am hay phu am, hay nhap lai!")
#...........................................
#Bai 6:
print("MENU:")
print("1.Phim hoat hinh")
print("2.Phim hanh dong")
print("3.Phim hai")
lua_chon=input("Nhap vao lua chon cua ban: ")
if lua_chon=='1':
    print("Ban da chon xem phim hoat hinh")
elif lua_chon =='2':
    print("Ban da chon xem phim hanh dong")
elif lua_chon=='3':
    print("Ban da lua chon phim hai")
else:
    print("Vui long lua chon lai theo dung so thu tu tren menu")
#............................................
#Bai 8:
n=input("Nhap vao diem cua ban: ")
if n=='A':
        print("Ban dat hoc luc xuat xac")
    
elif n=='B':
     
        print("Ban dat hoc luc gioi")
elif n=='C':
        print("Ban dat hoc luc kha")
    
elif n=='D':
        print("Ban dat hoc luc trung binh")
    
elif n=='E':
        print("Ban dat hoc luc yeu")
    
elif n=='F':
        print("Ban dat hoc luc kem")

else:
        print("Vui long nhap lai")
#...................................
#Bai 9:
luong=float(input("Nhap luong: "))
if luong == 15000000:
    thue_thu_nhap=(0.3*luong)
    luong_rong=luong - thue_thu_nhap
    print(f"Thue thu nhap cua ban la: {thue_thu_nhap}")
    print(f"Luong rong cua ban la {luong_rong}")
if luong >= 7000000 and luong <= 15000000:
    thue_thu_nhap=(0.2*luong)
    luong_rong=luong-thue_thu_nhap
    print(f"Thue thu nhap cua ban la: {thue_thu_nhap}")
    print(f"Luong rong cua ban la {luong_rong}")
if luong < 7000000:
    thue_thu_nhap=(0.1*luong)
    luong_rong=luong-thue_thu_nhap
    print(f"Thue thu nhap cua ban la: {thue_thu_nhap}")
    print(f"Luong rong cua ban la {luong_rong}")
#.............................................
#Bai 10:
thang= int(input("Nhap thang: "))
if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
    print("Thang nay co 31 ngay")
elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
    print("Thang nay co 30 ngay")
elif thang == 2:
    nam = int(input("Nhap nam: "))
    if (nam% 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        print("Thang nay vo 29 ngay")
    else:
        print("Thang nay co 28 ngay")
else:
    print("Vui long nhap lai")
#.............................................
#Bai 11:
s = int(input("Nhập vào một số nguyên có ba chữ số: "))
if 100 <= s <= 999:
    ones = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    tens = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    
    t = s // 100  
    c = (s // 10) % 10  
    dv = s % 10  

    doc = f"{ones[t]} trăm"
    
    if c != 0:
        if c == 1:
            doc += " mười"
        else:
            doc += f" {tens[c]}"
    
    if dv != 0:
        if c == 1:
            doc += f" {ones[dv]}"
        elif c > 1 or c == 0:
            doc += f" {ones[dv]}"

    print("Số bạn nhập là:", doc)
else:
    print("Vui lòng nhập lại")

#.............................................
#Bai 12:
TNCT=int(input("Nhap tham nien cong tac cua ban: "))
luong_co_ban=1350000
if TNCT <12:
    luong=2.34*luong_co_ban
elif TNCT >= 12 and TNCT <36:
    luong=3.33*luong_co_ban
elif TNCT>= 36 and TNCT <60:
    luong=3.66*luong_co_ban
elif TNCT >=60:
    luong=3.99*luong_co_ban
print(f"Luong cua ban nhan duoc la: {luong}")
