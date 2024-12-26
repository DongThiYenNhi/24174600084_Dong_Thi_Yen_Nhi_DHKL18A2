from datetime import datetime

ds_sinh_vien = []

n = int(input("Nhập số sinh viên cần cập nhật: "))
for sv in range(n):
    sinh_vien = {
        "ma_sinh_vien": "",
        "ho_dem": "",
        "ten": "",
        "tuoi": "",
        "ngay_thang_nam_sinh": "",
        "so_dien_thoai": "",
        "ma_mon": "",
    }
    print(f"Nhập vào sinh viên thứ {sv + 1}")

    
    while True:
        sinh_vien['ma_sinh_vien'] = input("Nhập vào mã sinh viên (10 chữ số): ")
        if len(sinh_vien['ma_sinh_vien']) >= 10 and sinh_vien['ma_sinh_vien'].isdigit():
            break
        else:
            print("Lỗi: Mã sinh viên phải có đúng 10 chữ số. Vui lòng nhập lại.")

    
    while True:
        sinh_vien['ho_dem'] = input("Nhập vào họ và đệm: ")
        if len(sinh_vien['ho_dem']) <= 50 and sinh_vien['ho_dem'].isalpha():
            break
        else:
            print("Lỗi: Họ và đệm chỉ được chứa chữ cái và không quá 50 ký tự. Vui lòng nhập lại.")

    
    while True:
        sinh_vien['ten'] = input("Nhập vào tên sinh viên: ")
        if len(sinh_vien['ten']) <= 50 and sinh_vien['ten'].isalpha():
            break
        else:
            print("Lỗi: Tên chỉ được chứa chữ cái và không quá 50 ký tự. Vui lòng nhập lại.")

    
    while True:
        sinh_vien['tuoi'] = input("Nhập vào tuổi sinh viên: ")
        if sinh_vien['tuoi'].isdigit():
            break
        else:
            print("Lỗi: Vui lòng nhập lại.")
        print("Lỗi: Tuổi không hợp lệ. Vui lòng nhập lại.")

    
    while True:
        sinh_vien['ngay_thang_nam_sinh'] = input("Nhập vào ngày tháng năm sinh sinh viên (DD/MM/YYYY): ")
        
        if datetime.strptime(sinh_vien['ngay_thang_nam_sinh'], "%d/%m/%Y"):
            break 
        else:
            print("Lỗi: Ngày tháng năm sinh không hợp lệ. Vui lòng nhập lại (định dạng DD/MM/YYYY).")

    while True:
        sinh_vien['so_dien_thoai'] = input("Nhập vào số điện thoại sinh viên (10 chữ số): ")
        if len(sinh_vien['so_dien_thoai']) == 10 and sinh_vien['so_dien_thoai'].isdigit():
            break
        else:
            print("Lỗi: Số điện thoại phải có đúng 10 chữ số. Vui lòng nhập lại.")


    while True:
        sinh_vien['ma_mon'] = input("Nhập vào mã môn của sinh viên (chỉ chứa chữ cái và số): ")
        if len(sinh_vien['ma_mon']) >= 10 and sinh_vien['ma_mon'].isalnum():
            break
        else:
            print("Lỗi: Mã môn học phải có đúng 10 ký tự và chỉ chứa chữ cái và số. Vui lòng nhập lại.")
    ds_sinh_vien.append(sinh_vien)

# In danh sách sinh viên
print("Danh sách sinh viên:")
print("Mã sinh viên", "\t", "Họ và đệm", "\t", "Tên", "\t", "Tuổi", "\t", "Ngày tháng năm sinh", "\t", "Số điện thoại", "\t", "Mã môn học")
for sv in ds_sinh_vien:
    print(sv["ma_sinh_vien"], "\t", sv["ho_dem"], "\t", sv["ten"], "\t", sv["tuoi"], "\t", sv["ngay_thang_nam_sinh"], "\t", sv["so_dien_thoai"], "\t", sv["ma_mon"])

#
ds_diem=[]
n=int(input("Nhap so luong sinh vien can nhap diem: "))
for diem in range(n):
    diem_sv={"ma_sinh_vien":"",
          "diem_hs11":0.0,
          "diem_hs12":0.0,
          "diem_hs21":0.0,
          "diem_hs22":0.0,
          "diem_hs23":0.0,
          "diem_tb":0.0,
          "nam_hoc":"",
          "ma_hoc_ky":"",
    }
    print(f"Nhap vao diem sinh vien thu {diem+1}")
    
    
    while True:
        diem_sv['ma_sinh_vien']=input("Nhap ma sinh vien: ")
        if len(diem_sv['ma_sinh_vien']) >= 10 and diem_sv['ma_sinh_vien'].isdigit():
            break
        else:
            print("Vui long nhap lai")
    while True:
        diem_sv['diem_hs11']=input("Nhap diem he so 1 1: ")
        if diem_sv['diem_hs11'].count('.') == 1 and diem_sv['diem_hs11'].replace('.', '', 1).isdigit():

            break
        else:
            print("Vui long nhap lai")
    while True:
        diem_sv['diem_hs12']=input("Nhap diem so he so 1 2: ")
        if diem_sv['diem_hs12'].count('.') == 1 and diem_sv['diem_hs12'].replace('.', '', 1).isdigit():

            break
        else:
            print("Vui long nhap lai")
    while True:
        diem_sv['diem_hs21']=input("Nhap diem he so 2 1: ")
        if diem_sv['diem_hs21'].count('.') == 1 and diem_sv['diem_hs21'].replace('.', '', 1).isdigit():

            break
        else:
            print("Vui long nhap lai")
    while True:
        diem_sv['diem_hs22']=input("Nhap diem he so 2 2: ")
        if diem_sv['diem_hs22'].count('.') == 1 and diem_sv['diem_hs22'].replace('.', '', 1).isdigit():

            break
        else:
            print("Vui long nhap lai")
    while True:
        diem_sv['diem_hs23']=input("Nhap diem he so 2 3: ")
        if diem_sv['diem_hs23'].count('.') == 1 and diem_sv['diem_hs23'].replace('.', '', 1).isdigit():

            break
        else:
            print("Vui long nhap lai")
    while True:
        diem_sv['diem_hs3']=input("Nhap diem he so 3: ")
        if diem_sv['diem_hs3'].count('.') == 1 and diem_sv['diem_hs3'].replace('.', '', 1).isdigit():

            break
        else:
            print("Vui long nhap lai")
    while True:
        diem_sv['diem_tb']=input("Nhap diem trung binh: ")
        if diem_sv['diem_tb'].count('.') == 1 and diem_sv['diem_tb'].replace('.', '', 1).isdigit():

            break
        else:
            print("Vui long nhap lai")
    while True:
        diem_sv['ma_hoc_ky']=input("Nhap ma hoc ky : ")
        if len(diem_sv['ma_hoc_ky'])>=10 and diem_sv['ma_hoc_ky'].isalnum():
            break
        else:
            print("Vui long nhap lai")
    while True:   
        diem_sv['nam_hoc']=input("Nhap nam hoc: ")
        if diem_sv['nam_hoc'].isdigit() and len(diem_sv['nam_hoc']) == 4:
            break
        else:
            print("Vui long nhap lai")
    ds_diem.append(diem_sv)
# Xem danh sach diem
print("Xem danh sach diem sinh vien")
for diem in  ds_diem:
    print(diem["ma_sinh_vien"],"\t",diem["diem_hs11"],"\t",diem["diem_hs12"],"\t",diem["diem_hs21"],"\t",diem["diem_hs22"],"\t",diem["diem_hs23"],"\t",diem["diem_hs3"],"\t",diem["diem_tb"],"\t",diem["nam_hoc"],"\t",diem["ma_hoc_ky"])
