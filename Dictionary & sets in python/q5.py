def is_armstrong_number(num):
    original_num = num
    sum_of_power = 0
    num_digit = 0

    while num > 0:
        num //= 10
        num_digit += 1

    num = original_num


    while num > 0:
        digit = num % 10
        sum_of_power += digit ** num_digit
        num //= 10


    return sum_of_power == original_num

number = int(input("Enter the number : "))
if is_armstrong_number(number):
    print(f"{number} is a Armstrong number")

else:
    print(f"{number} is not a Armstrong number")


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

num = int(input("Enter the number : "))
result = fibonacci(num)
for i in range(result):
    print(fibonacci(i), end=' ')

