from time import *
import random as r

def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except :
            error += 1
    return error

def speed_time(time_st,time_ed,userinput):
    time_delay = time_ed - time_st
    time_R = round(time_delay,2)
    speed = len(userinput) / time_R
    return round(speed)

if __name__ == '__main__':
    while True:
        ck = input(" Ready to test : yes / no : ")
        if ck == "yes":
            test = ["My name is Aditya Nautiyal","Monkey D Luffy","Zoro","One Piece is Real","Luffy is the Joy Boy"]
            test1 = r.choice(test)
            print('***** Typing Speed Calculator *****')
            print(test1)
            print()
            print()
            time_1 = time()
            test_input = input(' Enter : ')
            time_2 = time()

            print('Speed : ',speed_time(time_1,time_2,test_input),"w/sec")
            print('Error : ',mistake(test1,test_input))

        elif ck == "no":
            print('Thank you')
            break
        else:
            print('Invalid error type')

