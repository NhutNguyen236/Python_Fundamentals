import calendar
import datetime

# take the input 
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

# check if year is leap or not
if calendar.isleap(nam):
    print("Năm %d là năm nhuần" % (nam))
else:
    print("Năm %d không là năm nhuần" % (nam))

# count number of days in month 
_, day_count = calendar.monthrange(nam, thang)
print(f"Tháng {thang} năm {nam} có {day_count} ngày")

# calculate the last date of the month 
last_day = datetime.date(nam, thang, day_count).strftime("%A")
print(f"Ngày cuối cùng của tháng {thang} năm {nam} là {last_day}")

# Get the first Sunday of the week
cal = calendar.monthcalendar(nam, thang)
sunday = 0
for week in cal:
    print(week[6])
    if(week[6] != 0):
        sunday = week[6]
        break
print(f"Ngày chủ nhật đầu tiên của tháng {thang} năm {nam} là ngày {sunday}")

# print the calendar out 
print(calendar.month(nam, thang))
