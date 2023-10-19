so = int(input(" Nhập số cần kiểm tra: "))

flag = True

if(so > 1): 
    for i in range(2, so):
        if(so % i == 0):
            flag = False
            break
else: 
    flag = False
    
if(flag == True):
    print("Số %d là số nguyên tố" % so)
else:
    print("Số %d là không là số nguyên tố" % so)