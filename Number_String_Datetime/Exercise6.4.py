# define danh sach thuc uong list
danh_sach_thuc_uong =  ['Bac xỉu đá', 'Freeze trà xanh', 
                        'Trà Thạch vải', 'Trà thanh đào', 
                        'Cappuccino', 'Cà phê sữa đá']

index = input("Nhập từ khoá cần tìm: ")

# define 1 list rỗng để chứa tên thức uống
result = []

for food in danh_sach_thuc_uong: 
    if food.lower().find(index.lower()) != -1:
        result.append(food)
        
if(len(result) != 0):
    print("Tìm thấy 3 thức uống với từ khoá \"%s\"" % (index))
    print(', '.join(result))
else:
    print("Không tìm thấy thức uống với từ khoá \"%s\"" % (index) )
