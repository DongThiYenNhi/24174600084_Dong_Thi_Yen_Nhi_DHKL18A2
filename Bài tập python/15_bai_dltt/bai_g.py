ds_sinh_vien = []
n = int(input("Nhap so sinh vien n = "))
for sinh_vien in range(n):
    print(f"Nhap thong tin sinh vien thu {sinh_vien + 1}:")
    ten = input("Nhap ten sinh vien: ")
    diem = float(input("Nhap diem sinh vien: "))
    thong_tin_sinh_vien = {ten: diem}
    ds_sinh_vien.append(thong_tin_sinh_vien)
print(ds_sinh_vien)

print("Xóa thông tin sinh viên ứng với tên sinh viên")
t= input("Nhap vao ten sinh vien muon xoa: ")
index = -1
if len(ds_sinh_vien)==0:
    print("Danh sach rong")
else:
    for i in range(len(ds_sinh_vien)):
        if ds_sinh_vien[i][{'ten'}] == t:
            print("Sinh vien ton tai")
            index=i
    else:
        print("Sinh vien khong tai")
    if index != -1:
        ds_da_xoa=ds_sinh_vien.remove(ds_sinh_vien[index])   
        print("Tien hanh xoa sinh vien thanh cong")
print(ds_da_xoa)
    
            
        