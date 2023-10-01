# input 
lai_suat = float(input("Lãi suất 1 năm(%):"))
so_tien_gui = int(input("Số tiền gửi:"))
so_thang_gui = int(input("Số tháng gửi:"))

# print result
tien_lai = (so_tien_gui * so_thang_gui) * (lai_suat / 12 / 100)
tong_tien = tien_lai + so_tien_gui

print('-' * 10 + " Kết quả " + '-' * 10)
print("tiền lãi = {:,.1f}".format(tien_lai))
print("Tổng tiền = {:,} + {:,.1f} = {:,.1f}".format(so_tien_gui, tien_lai, tong_tien))