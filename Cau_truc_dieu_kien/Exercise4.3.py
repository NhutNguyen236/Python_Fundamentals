a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

if a != 0:
    print("Phương trình có 1 nghiệm x = %.2f" % (-b/a))
elif a == 0 and b == 0: 
    print("Phương trình có vô số nghiệm")
elif a == 0 and b != 0:
    print("Phương trình vô nghiệm")
