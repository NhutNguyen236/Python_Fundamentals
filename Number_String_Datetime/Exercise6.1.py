import math

a = int(input("Nhập vào diện tích hình tròn: "))

# check if area is less than 0 or not
if(a < 0):
    print("Diện tích ko được bé hơn 0")

else:
    r = math.sqrt(a/math.pi)
    
    print("Bán kính hình tròn %.1f" %(r))