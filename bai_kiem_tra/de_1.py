ds_cau_thu=[]
while True:
    print("Menu")
    print("1.Xem danh sach cau thu")
    print("2.Nhap thong tin cau thu tu ban phim")
    print("3.Tinh cot thuong")
    print("4.Tim va xoa cau thu")
    print("5.Tim kiem va chinh sua thong tin cau thu")
    print("6.Xem danh sach cau thu voi so huy chuong tu nho toi lon")
    lua_chon=input("Nhap vao lua chon cua ban: ")
    if lua_chon.isdigit ==False:
        print("Yeu cau nhap lai")
    else:
        lua_chon=int(lua_chon)
        if lua_chon==1:
            print("Xem danh sach cau thu")
            print("ma_cau_thu","\t","ten_cau_thu","\t","tuoi","\t","vi_tri","\t","so_huy_chuong","\t","thuong")
            for ct in ds_cau_thu:
                print(ct["ma_cau_thu"],"\t",ct["ten_cau_thu"],"\t",ct["tuoi"],"\t",ct["vi_tri"],"\t",ct["thuong"])
        elif lua_chon ==2:
            print("Nhap thong tin cau thu")
            while True:
                cau_thu={"ma_cau_thu":"",
                         "ten_cau_thu":"",
                         "tuoi":"",
                         "vi_tri":"",
                         "so_huy_chuong":"",
                         "thuong":0.0,
                        }
                cau_thu['ma_cau_thu']=input("Nhap ma cau thu")
                cau_thu['ten_cau_thu']=input("Nhap ten cau thu")
                cau_thu['tuoi']=input("Nhap tuoi cau thu")
                cau_thu['vi_tri']=input("Nhap vi tri cau thu")
                cau_thu['thuong']=input("Nhap thuong cau thu")
                ds_cau_thu.append(cau_thu)
                n=input("Ban muon nhap nua ko?Y/N")
                if n.capitalize != 'Y':
                    break
        elif lua_chon == 4:
            print("Xoa thong tin cau thu")
            n = input("Nhap vao ma cau thu: ")
            index = -1
            if len(ds_cau_thu) == 0:
                print("Dang sach rong")
            else:
                for i in range(len(ds_cau_thu)):
                    if ds_cau_thu[i]["ma_cau_thu"] == n:
                        print("Cau thu ton tai")
                        index = i
                        break
                else:
                    print("Cau thu khong ton tai")
                    
                if index != -1:
                    ds_cau_thu.remove(ds_cau_thu[index])   
                    print("Tien hanh xoa cau thu thanh cong")
