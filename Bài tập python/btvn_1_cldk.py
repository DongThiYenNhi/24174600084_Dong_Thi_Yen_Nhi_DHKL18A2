Nam=int(input("Nhập năm: "))
if Nam % 4 == 0 and Nam % 10 != 0 or Nam % 400 == 0:
    print("Năm này là năm nhuận")
else:
    print("Năm này là năm không nhuận")
print("Kết thúc chương trình")
    
