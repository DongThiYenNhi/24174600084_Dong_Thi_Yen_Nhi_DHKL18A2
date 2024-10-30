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