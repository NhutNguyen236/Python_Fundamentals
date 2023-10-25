from functools import reduce

list_diem_hkl = [8.5, 6.7, 9.0, 8.3, 5.0, 4.0, 6.0, 3.7, 9.5, 5.8] 
list_diem_hk2 = [7.0, 7.0, 9.2, 6.1, 4.8, 6.4, 8.5, 5.1, 5.6, 7.0]

def avg(item1, item2):
    return (item1 + item2)/2

# list_avg with lambda 
# list_avg = list(map((lambda item1, item2: (item1 + item2) / 2), list_diem_hkl, list_diem_hk2))
list_avg = list(map(avg, list_diem_hkl, list_diem_hk2))
print(f"Danh sách ĐTB: {list_avg}")

# map theo điểm trung bình đậu - rớt
def score_filter(score):
    if (score < 5):
        return "Rớt"
    else:
        return "Đậu"

list_score_filtered = list(map(score_filter, list_avg))
print("Danh sách KQ theo ĐTB: ", list_score_filtered)

# filter điểm trên tb
def tren_tb(score):
    if score >= 5:
        return True
    else:
        return False

list_tren_tb = list(filter(tren_tb, list_avg))
print("Danh sách điểm trên TB: ", list_tren_tb)

# filter điểm dưới tb
def duoi_tb(score):
    if score < 5:
        return True
    else:
        return False

list_duoi_tb = list(filter(duoi_tb, list_avg))
print("Danh sách điểm trên TB: ", list_duoi_tb)

# đổi list sang số nguyên 
def int_trans(number):
    return int(number)

list_int = list(map(int_trans, list_avg))
print(list_int)

# danh sách số nguyên tố
def check_prime(num):
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(num/2)+1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False      
        else:
            return True
    else:
        return False
    
prime_list = list(filter(check_prime, list_int))
print(prime_list)

# tính tổng các số nguyên tố
tong = reduce(lambda a, b: a + b, prime_list)
print(tong)