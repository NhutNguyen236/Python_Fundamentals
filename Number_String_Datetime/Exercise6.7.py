import datetime

def next_birthday(year, month, day):
    today = datetime.date.today()
    current_year_birthday = datetime.date(today.year, month, day)
    next_birthday = current_year_birthday

    if today > current_year_birthday:
        next_birthday = datetime.date(today.year + 1, month, day)

    days_until_next_birthday = (next_birthday - today).days

    return next_birthday, days_until_next_birthday

year = int(input("Nhập năm sinh: "))
month = int(input("Nhập tháng sinh: "))
day = int(input("Nhập ngày sinh: "))

next_birthday_date, days_until_next_birthday = next_birthday(year, month, day)
print(f"Ngày sinh nhật kế tiếp của bạn là ngày {next_birthday_date.strftime('%d/%m/%Y')}")
print(f"Còn {days_until_next_birthday} ngày nữa đến sinh nhật kế tiếp.")