email = input('Enter your Email : ') #g@g.in,wscube@gmail.com
k = j = d = 0
if len(email) >= 6: #1
    if email[0].isalpha() and email[0].lower: #2
        if ("@" in email) and (email.count("@")==1): #3
            if (email[-4] == ".") ^ (email[-3] == "."): #4
                for i in email:
                    if i == i.isspace(): #5
                        k = 1
                    elif i.isalpha():
                        if i == i.upper(): # 5
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        d = 1
                if k == 1 or j == 1 or d == 1:
                    print('Invalid email type 5')
                else:
                    print(f'{email} is a valid email address')
            else:
                print('Double point 4')
        else:
            print('wrong email to many @ 3')
    else:
        print('Wrong way to write the email 2')
else:
    print('Invalid email type 1')

