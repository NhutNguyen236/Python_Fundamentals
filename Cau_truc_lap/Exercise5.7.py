a = int(input("Nhập số bắt đầu: "))
b = int(input("Nhập số kết thúc: "))

tong_so_le = 0
tong_so_chan = 0
tich = 1
tich2 = 1
tong_nguyen_to = 0

def check_prime(number):
    flag = True

    for i in range(2, number):
        if(number % i == 0):
            flag = False
            break
    return flag

for i in range(a, b+1):
    # tổng các số lẻ
    if(i % 2 == 1):
        tong_so_le += i
    # tổng các số chẵn
    if(i % 2 ==0):
        tong_so_chan += i
    # tích các số từ a đến b
    tich = tich * i
    # tích các số chia hết cho 3
    if(i % 3 == 0):
        tich2 = tich2 * i
    # tổng các số nguyên tố
    if(check_prime(i) == True):
        tong_nguyen_to += i
    
        
print("A = %d" % tong_so_le)
print("B = %d" % tong_so_chan)
print("C = %d" % tich)
print("D = %d" % tich2)
print("E = %d" % tong_nguyen_to)