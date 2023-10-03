so_kwh = float(input("Số kw tiêu thụ: "))
tong_so_tien = 0

if 0 <= so_kwh <= 50:
    tong_so_tien = 1.678 * so_kwh
if 51 <= so_kwh <= 100:
    tong_so_tien = 1.734 * so_kwh
if 101 <= so_kwh <= 200:
    tong_so_tien = 2.014 * so_kwh
if 201 <= so_kwh <= 300:
    tong_so_tien = 2.536 * so_kwh
if 301 <= so_kwh <= 400:
    tong_so_tien = 2.834 * so_kwh
if so_kwh >= 401:
    tong_so_tien = 2.927 * so_kwh

print("Tiền điện phải trả: {:,}".format(tong_so_tien))