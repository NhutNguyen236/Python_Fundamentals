n = int(input(" Nhập vào n: "))
x = int(input("Nhập vào số x: "))

result = 1
# print("S = (x * x + 1) ^ n = %d" % ((x**2 + 1)**n))

for i in range(0, n):
    result = result * (x**2 + 1)

print(result)