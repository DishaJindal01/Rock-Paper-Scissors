import random

def choose(ran):
    if ran == 1:
        return "rock"
        
    elif ran == 2:
        return "paper"

    elif ran == 3:
        return "scissors"
    elif ran == 4:
        return "Exiting"
    
    else:
        return ran
    

while True:
    a = random.randint(1,3)
    user = int(input("Enter 1 for rock\nEnter 2 for paper\nEnter 3 for sessiors\nEnter 4 to Quit:\n"))
    

    print("computer choose:-",choose(a))
    print("you choose:-",choose(user))
    print("\n")
    if a == user:
        print("its a tie\n")

    elif (a == 1 and user == 2) or (a == 2 and user == 3) or (a == 3 and user == 1)  :
        print("you win\n")

    elif user > 3 or user == 4:
        break

    else:
        print("you loose\n")










