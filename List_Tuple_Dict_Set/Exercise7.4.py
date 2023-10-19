danh_sach_phim = [
    'Dòng chảy của nước',
    'Đảo độc đắc',
    'Tiểu đội gấu bay',
    'Âm lượng hủy diệt',
    'Búp bê gọi hồn',
    'Tro tàn rực rỡ',
    'Nữ chiến binh Amazon',
    'Khỉ con lon ton thế giới'
]

def show_phim():
    print(f"Có {len(danh_sach_phim)} phim trong danh sách")
    print(" STT       TÊN PHIM")
    for i in range(0, len(danh_sach_phim)):
        print(i + 1, "     " , danh_sach_phim[i])
    
while True: 
    print("-" * 10," Quản lý phim ", "-" * 10)
    print("""
        Bạn muốn làm gì? 
        1. Đọc danh sách
        2. Thêm phim mới
        3. Cập nhật phim
        4. Xoá phim
        """)
    select = input("Mời bạn chọn: ")

    # Đọc danh sách phim
    if(int(select) == 1):
        show_phim()
        print("bạn có muón tiếp tục ko? (y/n)")
        cont = input("Mời bạn chọn: ")
        if(cont == "n"):
            break
        else:
            continue
    # Thêm phim mới vào danh sách phim
    elif(int(select) == 2):
        while True:
            value = input("Nhập tên phim(dừng lại bấm phím s): ")
            if(value == "s"):
                break
            else: 
                danh_sach_phim.append(value) 
        print("bạn có muón tiếp tục ko? (y/n)")
        cont = input("Mời bạn chọn: ")
        if(cont == "n"):
            break
        else:
            continue
    
    #Cập nhật phim 
    elif(int(select) == 3):
        show_phim()
        while True:
            print("Chọn phim cần cập nhật")
            index = input("Nhập STT")
            
            # check nếu index vượt ra khỏi len(danhsachphim)
            if((int(index) > len(danh_sach_phim)) or (int(index) < 1)):
                print(f"Vui lòng nhập STT trong khoảng từ 1 đến {len(danh_sach_phim) + 1}")
                continue
            movie_name = input("Nhập tên phim(dừng lại bấm phím s): ")
            if(movie_name == "s"):
                break
            else: 
                danh_sach_phim[int(index) - 1] = movie_name
        print("bạn có muón tiếp tục ko? (y/n)")
        cont = input("Mời bạn chọn: ")
        if(cont == "n"):
            break
        else:
            continue
    
    # xoá phim
    elif(int(select) == 4):
        show_phim()
        while True:
            print("Chọn phim cần xoá")
            index = input("Nhập STT")
            
            # check nếu index vượt ra khỏi len(danhsachphim)
            if((int(index) > len(danh_sach_phim)) or (int(index) < 1)):
                print(f"Vui lòng nhập STT trong khoảng từ 1 đến {len(danh_sach_phim)}")
                continue
            else: 
                name = danh_sach_phim[int(index) - 1]
                del(danh_sach_phim[int(index) - 1])
                print(f"Đã xoá phim {danh_sach_phim[int(index) - 1]} ra khỏi danh sách")
                break
        print("bạn có muón tiếp tục ko? (y/n)")
        cont = input("Mời bạn chọn: ")
        if(cont == "n"):
            break
        else:
            continue
    
        