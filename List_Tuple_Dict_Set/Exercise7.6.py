tu_dien = {
    'man': ['đàn ông', 'nam nhi'],
    'woman': ['đàn bà', 'phụ nữ'],
    'sun': ['mặt trời'],
    'moon': ['mặt trăng'],
    'earth': ['trái đất', 'địa cầu'],
    'mountain': ['núi', 'ngọn núi'],
    'table': ['cái bàn'],
    'ball': ['quả bóng'],
    'flower': ['hoa', 'bông hoa'],
    'fan': ['cái quạt']
}

list_nghia = []

while True: 
    print("-" * 10," Quản lý phim ", "-" * 10)
    print("""
        Bạn muốn làm gì? 
        1. Tra từ điển
        2. Thêm từ
        3. Thêm nghĩa
        4. Xoá từ
        """)
    select = input("Mời bạn chọn: ")

    # Tra từ
    if(int(select) == 1):
        word = input("Nhập từ cần tra: ")
        # check if word is in tu_dien or not
        if(word in tu_dien):    
            print(f"Từ {word} có nghĩa là", tu_dien[word])
        else:
            print(f"Không tìm thấy từ {word} trong từ điển")
        print("bạn có muón tiếp tục ko? (y/n)")
        cont = input("Mời bạn chọn: ")
        if(cont == "n"):
            break
        else:
            continue
        
    # Thêm từ mới vào từ điển
    elif(int(select) == 2):
        word = input("Nhập từ mới: ")
        while True:
            nghia = input(f"Nhập nghĩa của từ {word} (dừng lại bấm phím s): ")
            list_nghia.append(nghia)
            if(nghia == "s"):
                # xoá bỏ chữ s khỏi list nghĩa
                list_nghia.pop()
                break
            else: 
                tu_dien[word] = list_nghia
        print("bạn có muón tiếp tục ko? (y/n)")
        cont = input("Mời bạn chọn: ")
        if(cont == "n"):
            break
        else:
            continue
    
    # Thêm nghĩa 
    elif(int(select) == 3):
        word = input("Nhập từ tiếng anh cần cập nhật nghĩa: ")
        while True:
            nghia = input(f"Nhập nghĩa của từ {word} (dừng lại bấm phím s): ")
            if(nghia == "s"):
                # xoá bỏ chữ s khỏi list nghĩa
                break
            else: 
                # thêm nghĩa vào từ
                tu_dien[word].append(nghia)
        print("bạn có muón tiếp tục ko? (y/n)")
        cont = input("Mời bạn chọn: ")
        if(cont == "n"):
            break
        else:
            continue
        
    # xoá từ
    elif(int(select) == 4):  
        word = input("Nhập từ tiếng anh cần xoá: ")
        # xoá từ khỏi từ điển
        del(tu_dien[word])
        print(f"Đã xoá {word} khỏi từ điển")
        print("bạn có muón tiếp tục ko? (y/n)")
        cont = input("Mời bạn chọn: ")
        if(cont == "n"):
            break
        else:
            continue
        
    