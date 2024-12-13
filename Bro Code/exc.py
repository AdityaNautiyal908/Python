# exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError,Exception)
#             1. try, 2.except, 3.finally

try:
    number = int(input("Enter a number : "))
    print(1/number)
    
except ZeroDivisionError:
    print("number cannot divide by Zero")

except ValueError:
    print("Type a number")

except Exception as e:
    print(f"{e}")

finally:
    print("You got the answer")