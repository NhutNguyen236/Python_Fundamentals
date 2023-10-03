string = []

while True:
    chuoi = input("Nhập kí tự (Dừng lại nhấn phím 0): ")
    if chuoi == "0":
        break
    else:
        string.append(chuoi)
        
print("Các kí tự đã nhập: %s" % (''.join(string)))