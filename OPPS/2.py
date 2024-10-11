num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

if num2 == 0:
    print("Error: Division by zero is not allowed.")
else:
    if num1 % num2 == 0:
        print("First number is divisible by second number")

    else:
        print("First number is not divisible by second number")