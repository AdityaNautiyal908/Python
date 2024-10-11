# class Student:
#     # default constructors
#     def __init__(self):
#         print("adding new values to my Database")

#     college_name = "ABC college" # class attri
#     # parameterized constructors
#     def __init__(self,name,marks):
#         self.name = name    # object attri
#         self.marks = marks

#     def welcome(self):
#         print("welcome student",self.name)

#     def get_marks(self):
#         return self.marks

# s1 = Student("Aditya",17)
# s1.welcome()
# print(s1.get_marks())


# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for value in self.marks:
            sum += value
        print("hi",self.name,"your avg score is : ",sum/3)

s1 = Student("Aditya",[99,98,97])
s1.get_avg()
