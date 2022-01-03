height = input("Enter your height in meters: ")
weight = input("Enter your weight in kilograms: ")

BMI = int(weight) / float(height) ** 2
bmi_as_int = int(BMI)
print("Your BMI is: " + str(bmi_as_int))