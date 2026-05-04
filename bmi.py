def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = int(weight) / (float(height) ** 2)
    print("BMI = " + str(bmi))
    
    if bmi < 18.5:
        print("Underweight")
        print(-1)
    
    elif bmi > 25:
        print("Overweight")
        print(1)
    
    else:
        print("Normal weight")
        print(0)

calculate_bmi(weight=85, height=1.73)