# a = int(input("Enter the first number : "))
# b = int(input("Enter the second number : "))

# c = a + b;

# print("Sum of two number : ",c)


# num = int(input("Enter the number : "))

# if(num % 7 == 0):
#     print(num,"is divisible by 7")

# else:
#     print(num,"is not divisible by 7")


# percentage = int(input("Enter you percentage : "))

# if (percentage > 90 and percentage < 100):
#     print("A")

# elif (percentage > 80 and percentage <= 90):
#     print("B")

# elif (percentage >= 60 and percentage <= 80):
#     print("C")

# else :
#     print("D")

# bill = 0
# unit = int(input("Enter the unit : "))

# if ( unit <= 100):
#     print("No charge : ",bill)

# elif ( unit <= 200):
#     bill = (unit - 100) * 5
#     print("Total price : ",bill)

# else : 
#     bill = ( 100 * 5) + ( unit - 200) * 10
#     print("Total price : ",bill)



# for x in range (1,11):
#     print(x)

# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1

# i = 10
# while i >= 1:
#     print(i)
#     i = i - 1

# Write a program to print 1 to 5 using while loop
# i = 1
# while i <=5:
#     print(i)
#     i = i + 1

# Palindrome number
# reverse = 0
# num = int(input("Enter the number : "))
# original = num
# while num != 0:
#     digit = num % 10
#     reverse = (reverse * 10) + digit 
#     num = num // 10


# if (original == reverse):
#     print("Yes palindrome")
# else :
#     print("Not a palindrome")


# num = int(input("Enter the number : "))
# left = 0
# right = num.size()-1

# while ( left < right):
#     if(num[right] != num[left])
#     return 0
#     else :
#     right ++ 
#     left--


def Calculator(a,b):
    print("Add : ",a+b)
    print("Subtarct :",a-b)
    print("Divide :",a//b)
    print("Multiply :",a*b)



num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

Calculator(num1,num2)



