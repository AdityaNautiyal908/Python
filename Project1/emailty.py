# a-z (small case character) nautiyaladitya7@gmail.com
# 0-9 (digit)
# . _ time 1
# @ count only 1
# . 2, 3 position

import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_input = input('Enter your email : ')

if re.search(email_condition,user_input):
    print(f'{user_input} is a valid email address')
else:
    print(f'{user_input} is a invalid email address')