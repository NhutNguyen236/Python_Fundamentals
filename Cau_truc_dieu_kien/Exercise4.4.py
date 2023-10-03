year = int(input("Nhập vào năm cần xét: "))

def xet_nam_nhuan(year):
    flag = True
    if (year % 4 == 0) and (year % 100 != 0):
        flag = True
    elif (year % 400 == 0):
        flag = True
    else:
        flag = False 
    return flag
    
if(xet_nam_nhuan(year) == True):
    print("Năm %d là năm nhuần" % year)
elif(xet_nam_nhuan(year) == False):
    print("Năm %d không là năm nhuần" % year)
