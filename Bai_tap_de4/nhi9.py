sinh_vien_hoc_lai = []
sinh_vien_qua_mon = []

for sv in ds_diem:
    if sv['diem_tb'] <= 3.5 or sv['diem_hs3'] < 4.0:
        sinh_vien_hoc_lai.append(sv)
    else:
        sinh_vien_qua_mon.append(sv)

sinh_vien_hoc_lai.sort(key=lambda x: x['ma_sinh_vien'])
sinh_vien_qua_mon.sort(key=lambda x: x['ma_sinh_vien'])

# In kết quả
print("Danh sách sinh viên học lại:")
print("Mã sinh viên", "\t", "Điểm TB", "\t", "Điểm HS3", "\t", "Mã môn", "\t", "Năm học")
for sv in sinh_vien_hoc_lai:
    print(sv["ma_sinh_vien"], "\t", sv["diem_tb"], "\t", sv["diem_hs3"], "\t", sv["ma_mon"], "\t", sv["nam_hoc"])

print("Danh sách sinh viên qua môn:")
print("Mã sinh viên", "\t", "Điểm TB", "\t", "Điểm HS3", "\t", "Mã môn", "\t", "Năm học")
for sv in sinh_vien_qua_mon:
    print(sv["ma_sinh_vien"], "\t", sv["diem_tb"], "\t", sv["diem_hs3"], "\t", sv["ma_mon"], "\t", sv["nam_hoc"])
