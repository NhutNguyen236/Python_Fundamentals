try:
    a = int(input("a: "))
    b = int(input("b: "))
    if b == 0:
        raise ZeroDivisionError("Lỗi chia cho 0")
    thuong = a / b
except ZeroDivisionError as err:
    print('Error1: ', err)
except NameError as err:
    print('Error: ', err)
else: 
    print('Thương: ', thuong)