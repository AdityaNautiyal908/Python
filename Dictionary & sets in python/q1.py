# dict = {
#     "name" : "Aditya",
#     "cgpa" : 9.6,
#     "marks" : [98,90,98],
#     "anime" : ["Luffy","Ace","Sabo"],
# }

# dict["surname"] = "King"
# dict["name"] = 55


# null_dict = {}
# null_dict["name"] = "Monkey D. luffy"
# print(null_dict)

student = {
    "name" : "Aditya",
    "subject" : {
        "pyh" : 89,
        "chem" : 90,
        "bio" : 78
    },
    "percentage" : 90,
}

# print(student["subject"]["bio"])

# print(len(student))
# print(list(student.values()))
# print(student.items())
print(student.get("name2")) # None

student.update({"city" : "delhi"})
print(student.values())