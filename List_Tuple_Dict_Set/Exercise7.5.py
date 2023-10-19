tuple_colors  =  ('red',  'green',  'yellow',  'blue',  'black',  'white', 'pink', 'orange', 'red', 'blue')

index = int(input("Nhập index (Từ 0 đến 9): "))
neg_index = int(input("Nhập negative index (Từ -10 đến -1): "))
color = input("Nhập màu cần tìm: ")
color_pos = []
count_color = 0

print("-" * 40)

print(f"- tuple_colors[{index}] = ", tuple_colors[index])
print(f"- tuple_colors[{neg_index}] = ", tuple_colors[neg_index])

# loop through the tuple_colors
for i in range (0, len(tuple_colors)):
    if(tuple_colors[i] == color):
        color_pos.append(i)
        count_color += 1

print(f"\"{color}\" xuất  hiện {count_color} lần trong danh sách tại vị trí {color_pos}")

# sort ascending tuple
sorted_color = sorted(tuple_colors)

print(sorted_color)