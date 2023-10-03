n = int(input(" Nhập vào n: "))
x = int(input("Nhập vào số x: "))

result1 = 1 
result2 = 1

for i in range(0, n):
    result1 = result1 * (x**2 + x + 1)
    
for i in range(0, n):
    result2 = result2 * (x**2 - x + 1)
    
print(result1 + result2)