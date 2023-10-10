"""
Giải phương trình bậc 2
"""
import math

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))

def phuong_trinh_bac_nhat(b,c):
    if b != 0:
        print("Phương trình có 1 nghiệm x = %.2f" % (-c/b))
    elif b == 0 and c == 0: 
        print("Phương trình có vô số nghiệm")
    elif b == 0 and c != 0:
        print("Phương trình vô nghiệm")

if a == 0:
    phuong_trinh_bac_nhat(b,c)
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        print("Phương trình có nghiệm kép x1=x2= %.1f" % (-b/(2*a)))
    elif delta > 0:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print("Phương trình có 2 nghiệm phân biệt:\nx1 = %.1f \nx2 = %.1f" % (x1, x2))
    