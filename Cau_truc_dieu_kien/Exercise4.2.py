input_list = input("Enter a list of elements: ").split()
my_list = list(map(int, input_list))
print("Giá trị lớn nhất: %i" % max(my_list))
print("Giá trị nhỏ nhất: %i" % min(my_list))