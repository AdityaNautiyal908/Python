import re

def validate_phone_number(phone_number):
    pattern = r'^\d{3}-\d{3}-\d{4}$'

    if re.match(pattern,phone_number):
        return True
    else:
        return False
    
phone_number = input("Enter the phone number in the format XXX-XXX-XXXX : ")

if validate_phone_number(phone_number):
    print("Phone number is valid")

else:
    print("Phone number is invalid")