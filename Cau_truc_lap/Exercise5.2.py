print("-" * 10, "CHƯƠNG TRÌNH TÍNH TỔNG N SỐ NGUYÊN", "-" * 10)

n = int(input("Nhập n: "))

numbers = []

for i in range(1, n + 1, 1):
    index = int(input("Nhập số nguyên thứ %d" % i))
    numbers.append(index)
    
print("Tổng = %d" % (sum(numbers)))