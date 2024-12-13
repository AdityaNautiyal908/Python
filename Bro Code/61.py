# # Python reading files(.txt,.json,.csv)

# import string
# import random


# digits = string.digits
# uppers = string.ascii_uppercase
# all_chars = string.digits + string.ascii_letters + string.punctuation

# def generate_password():
#     password = [
#         random.choice(digits),
#         random.choice(uppers)
#     ]
#     remaining_length = 6 - len(password)

#     password += random.choices(all_chars,k=remaining_length)

#     random.shuffle(password)

#     return ''.join(password)

# print(f"Generate password : {generate_password()}")


dict = {'a' : 1, 'b' : 2, 'c' : 3}

for key,value in dict.items():
    print(f"key : {key}, value : {value}")