# get multiple user input split by ,
index1, index2 =input("Nhập 2 giá trị a, b: ").split(',')
print("Tổng = %i + %i = %i" % (int(index1), int(index2), int(index1) + int(index2)))
print("Trung bình cộng = (%i + %i) / 2 = %.1f" % (int(index1), int(index2), (int(index1) + int(index2)) / 2))