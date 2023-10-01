# input string 
chuoi = input("Nhập chuỗi:")
# print("Chuỗi " + str(do_c) + " " + str(len(do_c)))
print("Chuỗi \"%s\" có chiều dài: %i" % (chuoi, len(chuoi)))

# get character at the input index
index = int(input("Nhập vào index: "))
# print("Ký tự tại vị trí index " + str(index) + " : " + str(do_c[int(index)]))
print("Ký tự tại vị trí index %i là: %s" % (index, chuoi[index]))

# get multiple user input split by ,
index1, index2 =input("Enter index range: ").split(',')
# print(chuoi[int(index1): int(index2)])
print("%i ký tự từ vị trí index %i đến %i là: %s" % (int(index2) - int(index1), int(index1), int(index2), chuoi[int(index1):int(index2)]))
 