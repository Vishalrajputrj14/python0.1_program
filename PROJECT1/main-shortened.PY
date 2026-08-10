import random

"""
1 for snake 
-1 for water 
0 for gun



"""

computer = random.choice([-1,0,1])
yourstr = input("Entar your choice: ")
youdict = {"s":1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "gun"}

you = youdict[yourstr]

print(f"You chose {reverseDict[you]}\n computer chose {reverseDict[computer]}")
if(computer == you):
    print("Its a draw ")
else:
    #    if(computer ==-1 and you ==1): (computer - you) = -2
    #     print("you win!")
    # elif(computer ==-1 and you ==0): (computer - you) = -1
    #     print("you win!")
    # elif(computer ==-1 and you ==1): (computer - you) = 2
    #     print("you win!")
    # elif(computer ==-1 and you ==0): (computer - you) = 1
    #     print("you win!")
    # elif(computer ==-0 and you ==1): (computer - you) = 1
    #     print("you win!")
    # elif(computer ==-0 and you ==1): (computer - you) = -1
    #     print("you win!")
    # the below logic is witten on the value of computer - you
 
    if(computer ==-1 and you ==1):
        print("you win!")
    elif(computer ==-1 and you ==0):
        print("you win!")
    elif(computer ==-1 and you ==1):
        print("you win!")
    elif(computer ==-1 and you ==0):
        print("you win!")
    elif(computer ==-0 and you ==1):
        print("you win!")
    elif(computer ==-0 and you ==1):
        print("you win!")
 
    else:
       print("Something went wrong!")