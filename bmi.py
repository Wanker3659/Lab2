def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = int(weight) / (float(height) ** 2)
    print("BMI = " + str(bmi))
    
    if bmi < 18.5:
        print("Underweight")
    
    elif bmi > 25:
        print("Overweight")
    
    else:
        print("Normal weight")

calculate_bmi(weight=57, height=1.73)