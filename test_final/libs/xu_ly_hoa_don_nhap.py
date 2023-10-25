import csv

def them_hoa_don(list_hoa_don):
    hoa_don = []
    # thêm ma_hd 
    mahd = input("Nhập mã hoá đơn: ")
    # thêm ngay_hd
    ngayhd = input("Nhập ngày tạo hoá đơn: ")
    # họ tên khách hàng 
    ho_ten_kh = input("Nhập họ tên khách hàng: ")
    # số lượng nhập
    so_luong_nhap = input("Nhập vào số lượng: ")
    # tổng tiền
    tong_tien = input("Nhập vào tổng tiền")

    # # check ma hoa don có phải duy nhất hay ko
    # for i in list_hoa_don:
    #     # lấy ra mã hoá đơn trong từng hoa_don, đứng index là 0
    #     if (i[0] == mahd):
    #         print("Mã hoá đơn đã tồn tại")
    #     else: 
    #         # thêm tất cả thông tin vào hoa_don
    #         hoa_don.append(mahd)
    # hoa_don.append(ngayhd)
    # hoa_don.append(ho_ten_kh)
    # if(int(so_luong_nhap) > 0 and int(tong_tien) > 0):
    #     hoa_don.append(so_luong_nhap)
    #     hoa_don.append(tong_tien)
    # else:
    #     print("Số lượng hay tổng tiền = 0")
    hoa_don.append(mahd)
    hoa_don.append(ngayhd)
    hoa_don.append(ho_ten_kh)
    hoa_don.append(so_luong_nhap)
    hoa_don.append(tong_tien)
    list_hoa_don.append(hoa_don)
    # test
    print(list_hoa_don)
    
def in_danh_sach_hoa_don(list_hoa_don):
    print(" {:4} {:20} {:20} {:20} {:8}".format("Mã HD", "Ngày hoá đơn", "Họ tên KH", "Số lượng nhập", "Tổng tiền"))
    for i in list_hoa_don:
        print(" {:4} {:20} {:20} {:20} {:8}".format(*i))

# tra cuu hoa don      
def tra_cuu_hoa_don(ma_hd, list_hoa_don):
    for i in list_hoa_don:
        if i[0] == ma_hd: 
            print(i)
            
# xoá hoá đơn
def xoa_hoa_don(ma_hd, list_hoa_don):
    for i in list_hoa_don:
        if i[0] == ma_hd:
            list_hoa_don.remove(i)
            print(f"Đã xoá {i[0]}")       
            
def thong_ke(x, list_hoa_don):
    n_so_luong = 0 
    tyle = 0
    for i in list_hoa_don: 
        if(int(i[3]) > x):
            n_so_luong += 1
    # tính tỷ lệ 
    tyle = n_so_luong/len(list_hoa_don)
    
    print(f"Có {n_so_luong} hoá đơn lớn hơn {x}")
    print(f"Tỷ lệ là: {tyle}")
    
def luu_file_csv(path, list_hoa_don):
    file = open(path, 'w', encoding='utf-8', newline='')
    csv.writer(file).writerows(list_hoa_don)
    print("Đã lưu thành công")
    file.close()
    
def doc_file_csv(path, list_hoa_don):
    file = open(path, 'r', encoding='utf-8', newline='')
    for row in csv.reader(file):
        print(row)
        list_hoa_don.append(row)
    file.close()
        
    
            