import re

def valid_phone_number(number):
    pattern = r'^\d{3}-\d{3}-\d{4}$'

    if re.match(pattern,number):
        return True
    else:
        return False


number = input("Enter the number in this format (XXX-XXX-XXXX) : ")

if valid_phone_number(number):
    print("Valid phone number")

else:
    print("Valid phone number")