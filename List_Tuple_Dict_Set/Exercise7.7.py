# init set 1 and set 2
set1 = set()
set2 = set()

# Input set 1 
while True: 
    value = input("Nhập giá trị cho set 1: ")
    cont = input("Tiếp tục nhập set 1? 1. Có 0. không: ")
    if(int(cont) == 0):
        set1.add(int(value))
        break
    else:
        set1.add(int(value))

# Input set 2
while True: 
    value = input("Nhập giá trị cho set 2: ")
    cont = input("Tiếp tục nhập set 1? 1. Có 0. không: ")
    if(int(cont) == 0):
        set2.add(int(value))
        break
    else:
        set2.add(int(value))

print("-" * 30, " SET 1", "-" * 30)
print("Set 1: ", set1)
print("Chiiều dài: ", len(set1))
print("Tổng: ", sum(set1))
print("Max: ", max(set1))
print("Min: ", min(set1))
print("Sắp xếp theo giảm dần: ", sorted(set1, reverse=True))

print("-" * 30, " SET 2", "-" * 30)
print("Set 1: ", set2)
print("Chiiều dài: ", len(set2))
print("Tổng: ", sum(set2))
print("Max: ", max(set2))
print("Min: ", min(set2))
print("Sắp xếp theo giảm dần: ", sorted(set2, reverse=True))

print("-" * 60)
print("Union: ", set1 | set2)
print("Intersection ", set1 & set2)
print("Difference ", set1 - set2)
print("Symmetric Difference ", set1 ^ set2)
        