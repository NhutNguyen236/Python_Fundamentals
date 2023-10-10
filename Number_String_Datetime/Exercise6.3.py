import math

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))

if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
    print("Chiều dài 3 cạnh tam giác ko hợp lệ")
else:
    p = (a + b + c) / 2
    dien_tich = math.sqrt(p*(p-a)*(p-b)*(p-c))

    print("Diện tích tam giác: ", dien_tich)
 