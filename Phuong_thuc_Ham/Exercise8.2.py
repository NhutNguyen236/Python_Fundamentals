# Calculate BMI and sorting BMI by height and weight
def bmi_calculator(height, weight):
    bmi = weight / (height * height)
    result = ""
    
    # sort bmi
    if (bmi < 18.5):
        result = "Thiếu cân(Gầy)"
    elif (bmi >= 18.5 and bmi <= 24.9):
        result = "Bình thường"
    elif (bmi >= 25 and bmi <= 29.9):
        result = "Thừa cân"
    elif (bmi > 30):
        result = "Béo phì"

    return bmi, result

weight = int(input("Nhập cân nặng: "))
height = float(input("Nhập chiều cao: "))
bmi, result = bmi_calculator(weight, height)

print(bmi, result)

