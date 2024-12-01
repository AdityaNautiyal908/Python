# *args = parameter that will pack all arguments into a tuple useful so that a function
#        can accept a varying amount of arguments

def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(add(1,2,3,5,5,7))
