# init a list to store value 
list = []

while True: 
    value = int(input("Nhập giá trị: "))
    cont = int(input("Tiếp tục 1. Có 0. Không: "))
    if(cont == 0):
        # append the final value to list before break 
        list.append(value)        
        break
    else:
        list.append(value)
        
print("Danh sách đã nhập: ", list)
print("Tổng các phần tử trong list: ", len(list))

x = int(input("Nhập x: "))
print(f"{x} xuất hiện trong list {list.count(x)} lần")

# danh sách số âm
negatives = [i for i in list if(i < 0)]
print("Danh sách số âm: ", negatives)

# danh sách số dương
positives = [i for i in list if(i > 0)]
print("Danh sách số âm: ", positives)

# check prime 
def check_prime(number):
    flag = True
    # check if number > 1 then check prime 
    if(number > 1):
        for i in range(2, number):
            if(number % i == 0):
                flag = False
                break
    else:
        flag = False
    return flag

prime = [i for i in list if(check_prime(i) == True)]
print("Danh sách số nguyên tố", prime)

# tính trung bình cộng 
print(f"Trung bình cộng các số âm: {sum(negatives)/len(negatives)}")
print(f"Trung bình cộng các số dương: {sum(positives)/len(positives)}")
print(f"Trung bình cộng các số nguyên tố: {sum(prime)/len(prime)}")