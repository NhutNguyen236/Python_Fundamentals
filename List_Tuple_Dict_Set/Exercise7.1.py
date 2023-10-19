danh_sach_thu = ['ant', 'bear', 'cat', 'dog', 'elephant', 'fish', 'goat', 'hippo']

index = input("Nhập thú cần tìm: ")

flag = True

for animal in danh_sach_thu:
    if(animal == index):
        flag = True
        break 
    else:
        flag = False
if(flag):
    print(f"Tìm thấy {index} trong danh sách tại index = {danh_sach_thu.index(index)}")
else:
    print("không tìm thấy")