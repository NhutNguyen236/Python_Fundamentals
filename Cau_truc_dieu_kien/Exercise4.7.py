# input 
room_type = int(input("Nhập vào loại phòng (từ 1 đến 8): "))
night = int(input("Nhập số đêm: "))

final_price = 0

room_list = {1:1260000, 2: 1550000, 3: 1830000, 4: 1830000, 5: 2120000, 6: 2120000, 7: 2540000, 8: 4800000}

if 2 <= night <= 3:
    discount_price = room_list[room_type] * 0.25
    price_after_discount = room_list[room_type] - discount_price
    final_price = price_after_discount * night

elif night >= 4:
    discount_price = room_list[room_type] * 0.3
    price_after_discount = room_list[room_type] - discount_price
    final_price = price_after_discount * night

print("Thành tiền: {:,}".format(final_price))
