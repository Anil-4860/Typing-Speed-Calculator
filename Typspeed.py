from time import *
import random as r

def mistake(paratest,usertest):
    error=0
    for i in range(len(paratest)):
        try:
            if paratest[i]!=usertest[i]:
                error=error+1
        except:
            error=error+1
    return error
def speed_time(time_s,time_e,userinput):
    time_delay=time_e-time_s
    time_r=round(time_delay,2)
    speed=len(userinput)/time_r
    return round(speed)

while True:
 ck=input("ready to test:yes/no:")
 if ck=="yes":
    test=["A paragraph is a self_contained unit of discore in writing dealing a particular point or idea.",
    "my name is anil kumar sahoo","welcome to wscube tech jodhpur"]
    test1=r.choice(test)
    print("*****typing speed*****")
    print(test1)
    print()
    print()
    time_1=time()
    testinput=input("Enter:")
    time_2=time()
    print("speed:",speed_time(time_1,time_2,testinput),"w/s")
    print("Error:",mistake(test1,testinput))
 elif ck=="no":
     print("thank you")
     break
 else:
     print("wrong input")
