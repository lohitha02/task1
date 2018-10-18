import random
computer=["rock","paper","scissors"]
userscore=0
computerscore=0
for i in range(0,5):
    user=input()
    while(user!="rock" and user!="paper" and user!="scissors"):
        print("enter either rock or paper or scissors")
        user=input()
    choice=random.choice(computer)
    if(user==choice):
        print("tie,scores are equal")
    elif(user=="rock"):
        if(choice=="scissors"):
            print("rock blunts scissors,you won")
            userscore=userscore+5
        else:
            print("computer wins")
            computerscore=computerscore+5
    elif(user=="scissors"):
        if(choice=="paper"):
            print("scissors cut paper,you won")
            userscore=userscore+5
        else:
            print("computer wins")
            computerscore=computerscore+5
    elif(user=="paper"):
        if(choice=="rock"):
            print("paper covers rock,you won")
            userscore=userscore+5
        else:
            print("computer wins")
            computerscore=computerscore+5
    else:
        print("something is wrong,please check the input")
print("userscore="+str(userscore))
print("computerscore="+str(computerscore))
if(userscore>computerscore):
    print("yayyy you won")
elif(computerscore==userscore):
    print("match tied")
else:
    print("computer won")
