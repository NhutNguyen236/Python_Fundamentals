from datetime import datetime

# input vào format dd/MM/yyyy
date = input("Nhập chuỗi (dd/MM/yyyy)")

def kiem_tra_ngay_thang_nam(date):
    date_obj = datetime.strptime(date, "%d/%m/%Y")

    day = date_obj.day
    month = date_obj.month
    year = date_obj.year
    
    check = []
    
    # check if year is valid or not 
    if(len(str(year)) == 2 or len(str(year)) == 4):
        check.append(True)
    else:
        check.append(False)
    # check if month is valid or not
    if(month >= 1 and month <=12):
        check.append(True)
    else:
        check.append(False)
    
    # final_check = list(map(lambda a, b: a and b, check))
    
    return check
    

print (kiem_tra_ngay_thang_nam(date))

