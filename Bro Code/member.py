# Membership operator = used to test whether a value or variable is found in a sequence 
#                       (string,list,tuple,set or dictionary)
#                       1. in  
#                       2. not in


email = "nautiyaladitya7@gmail.com"

if "@" in email and "." in email:
    print(f"{email} ia valid email")

else:
    print("Invalid email")