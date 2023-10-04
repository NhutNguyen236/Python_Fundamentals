# Nhập số bắt đầu và số kết thúc
n = int(input("Nhập số bắt đầu: "))
m = int(input("Nhập số kết thúc: "))

# In bảng cửu chương từ n đến m
for i in range(n, m+1): #m+1 
    print(f"Bảng cửu chương của {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print()