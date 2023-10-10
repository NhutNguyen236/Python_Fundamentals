import re

string = "Python 1.0 đã được ra mắt vào năm 1994 với các hàm mới để dễ dàng xử lý danh sách dữ liệu, chẳng hạn như ánh xạ, lọc và lược bỏ. Python 2.0 đã được ra mắt vào ngày 16 tháng 10 năm 2000, với các tính năng hữu ích mới cho lập trình viên, chẳng hạn như hỗ trợ ký tự Unicode và cách xử lý chi tiết một danh sách nhanh chóng hơn. Python 3.0 đã được ra mắt vào ngày 3 tháng 12 năm 2008. Phiên bản này bao gồm các tính năng như hàm in và hỗ trợ nhiều hơn cho việc phân chia số và xử lý lỗi."
count = 0

numbers = re.findall('\d+', string)
integers = [int(num) for num in numbers]

# tính các integer trong integers
for int in integers:
    count += int

# in ra kết quả theo format 
# chuyển list sang str cho từng phần tử
output = [str(i) for i in integers]
print(' + '.join(output) + " = " + str(count))