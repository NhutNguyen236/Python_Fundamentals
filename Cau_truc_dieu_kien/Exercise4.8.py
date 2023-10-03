thu_nhap_nam = int(input("Số tiền thu nhập trong năm: "))
nguoi_phu_thuoc = int(input("Số người phụ thuộc: "))

tien_thue = 0

if thu_nhap_nam <= 60000000:
    tien_thue = (thu_nhap_nam * 5) / 100
if 60000000 <= thu_nhap_nam <= 120000000:
    tien_thue = (thu_nhap_nam * 10) / 100
if 120000000 <= thu_nhap_nam <= 216000000:
    tien_thue = (thu_nhap_nam * 15) / 100
if 216000000 <= thu_nhap_nam <= 384000000:
    tien_thue = (thu_nhap_nam * 20) / 100
if 384000000 <= thu_nhap_nam <= 624000000:
    tien_thue = (thu_nhap_nam * 25) / 100
if 624000000 <= thu_nhap_nam <= 960000000:
    tien_thue = (thu_nhap_nam * 30) / 100
if thu_nhap_nam >= 960000000:
    tien_thue = (thu_nhap_nam * 35) / 100
    
print("Tiền thuế: {:,}".format(tien_thue))