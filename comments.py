#I'm still relearning Python

#It is getting high level

try:
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by zero. Please input whole number.")
except ValueError:
    print("Invalid input. Please input whole number.")