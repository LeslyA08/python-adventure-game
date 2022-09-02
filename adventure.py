import time 

def scene1():
    print("Hello there! Would you like to enter? Enter Yes or No")
    a1 = input()
    time.sleep(2)
    if (a1.upper() == 'YES'):
        print("You move on")
        scene2()
    elif (a1.upper() == 'NO'):
        print("You do nothing you lazy bum")
    else:
        print("Choose correctly! Yes or No!: ")
        a1 = input()

def scene2():
    print("This is a super creepy dark hall way. Go left or right?: ")
    a1 = input()
    time.sleep(2)
    if(a1.upper()== 'LEFT'):
        print("You go Left")
        scene3()
    elif(a1.upper()== 'RIGHT'):
        print("You ded")
        scene1()
    else:
        print("Choose correctly! Yes or No!: ")
        a1 = input()

scene1()
            