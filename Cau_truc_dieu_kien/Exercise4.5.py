loai_xe = int(input("Loại xe: "))
thoi_gian_cho = int(input("Thời gian chờ (phút): "))
so_km = int(input("Số km di chuyển: "))

tien_cho = 0
tien_di_chuyen = 0
tien_cuoc = 0

if loai_xe == 4: 
    if thoi_gian_cho >= 6:
        tien_cho = thoi_gian_cho * 750
    if so_km <= 0.5:
        tien_di_chuyen = 11000 * so_km
    elif so_km <= 30:
        tien_di_chuyen = 17600 * so_km
    elif so_km >= 31:
        tien_di_chuyen = 14500 * so_km 
elif loai_xe == 7:
    if thoi_gian_cho >= 6:
        tien_cho = thoi_gian_cho * 750
    if so_km <= 0.5:
        tien_di_chuyen = 12000 * so_km
    elif so_km <= 30:
        tien_di_chuyen = 19600 * so_km
    elif so_km >= 31:
        tien_di_chuyen = 17100 * so_km 
    
print("Tiền chờ: {:,}".format(tien_cho))
print("Tiền di chuyển: {:,.1f}".format(tien_di_chuyen))
print("Tiền cước = {:,.1f} + {:,} = {:,.1f}".format(tien_di_chuyen, tien_cho, tien_di_chuyen + tien_cho))