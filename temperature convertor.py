import math

user_weight = int(input("Enter your weight in KG:"))
user_height = float(input("Enter your height in M:"))
raw_BMI_calculator = user_weight/math.pow(user_height,2)
BMI_calculator = round(raw_BMI_calculator,2)
print(f"Your BMI is {BMI_calculator}")

weight_class = raw_BMI_calculator

if weight_class <=18.5 :
    print('[Weight_Class]:UNDERWEIGHT')
elif weight_class >= 18.5 and weight_class <= 24.9:
    print('[Weight_Class]:NORMAL')
elif weight_class >= 25:
    print('[Weight_Class]:OVERWEIGHT')
elif weight_class >= 30:
    print('[Weight_Class]:OBESE')