from libs.xu_ly_hoa_don_nhap import *

path = 'files/file_csv.csv'
list_hoa_don = []

if __name__ == "__main__":
    while True: 
        print("CHUONG TRInH QUAN LY HOA DON")
        print("""
            1. Đọc file hoá đơn
            2. Thêm hoá đơn
            3. Danh sách hoá đơn
            4. Tra cứu hoá đơn
            5. Xoá hoá đơn
            6. Thống kê
            7. Lưu danh sách hoá đơn ra file
            """)
        select = int(input("Hãy nhập vào số chức năng: "))
        # Đọc file hoá đơn
        
        if select == 1:
            doc_file_csv(path, list_hoa_don)
            
        elif select == 2:
            them_hoa_don(list_hoa_don)
            
        elif select == 3:
            in_danh_sach_hoa_don(list_hoa_don)
        
        elif select == 4: 
            ma_hd = input("Nhập vào mã hoá đơn cần tìm: ")
            tra_cuu_hoa_don(ma_hd, list_hoa_don)
        
        elif select == 5:
            ma_hd = input("Nhập vào mã hoá đơn cần xoá: ")
            xoa_hoa_don(ma_hd, list_hoa_don)
        
        elif select == 6:
            x = int(input("Nhập vào số lượng x muốn thống kê: "))
            thong_ke(x, list_hoa_don)
        
        elif select == 7:
            luu_file_csv(path, list_hoa_don)
        cont = int(input("Bạn có muốn tiếp tục hay ko? "))
        if cont == 1:
            continue
        else:
            break