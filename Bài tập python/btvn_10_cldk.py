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
