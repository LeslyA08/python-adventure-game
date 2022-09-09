import time 
import logging
import datetime


logging.basicConfig(filename="adventurelog.log", level= logging.DEBUG)

class Player:
    def __init__(self):
        self.name= input ("Enter your name: ")

player1 = Player().name

def loggingFunct():
    with open('adventurelog.log') as file:
        lines = file.read().splitlines()
        lines = [lines[x:x+3] for x in range(0,len(lines), 3)]

def scene1():
    global player1
    logging.info(f"The game begins {datetime.datetime.now()}")
    print(f"{player1}, you slowly open your eyes and look around you. The room is cold and dark, a place you have never been before. \n You ask yourself, how did I get here? You slowly make your way onto a door, your hear sounds coming from the other side. \n Should you go out and investigate or should you stay put? \n Choose: stay or go?")
    a1 = input()
    time.sleep(2)
    if (a1.upper() == 'GO'):
        print(f"{player1} decides to go out and investigate.")
        time.sleep(8)
        scene2()
    elif (a1.upper() == 'STAY'):
        print(f"{player1} decided to do nothing. Something sinister is already in the room, and it is too late to change your mind.")
        time.sleep(8)
        scene1()
    else:
        print("*******************Choose correctly!*******************")
        time.sleep(8)
        scene1()

def scene2():
    global player1
    logging.info(f"{player1} goes out and investigates. {datetime.datetime.now()}")
    print(f"The door creeks as {player1} slowly open it. You are cautious at what may lie ahead. \n You look around, but see no one. You go down the hallway, you can't seem to find any light at all. \n A wall stops you in your tracks. You can barely make out that there is two ways to go. To your left is a faint light, to your right is pitch black darkness. Where will you go? Choose: Left or right? ")
    a1 = input()
    time.sleep(2)
    if(a1.upper()== 'LEFT'):
        print("You decide to go left")
        time.sleep(8)
        scene3()
    elif(a1.upper()== 'RIGHT'):
        print("You decide to go right")
        time.sleep(8)
        scene4()
    else:
        print("*******************Choose correctly!*******************")
        time.sleep(8)
        scene2()

def scene3():
    global player1
    logging.info(f"{player1} decides to go left. {datetime.datetime.now()}")
    print(f"As {player1} walks towards the light, you notice a faint figure. You can barely make out a shape of a man... a rotting man. \n You freeze in place, contemplating what to do. You grab fireplace poker to defend yourself. Should you attack? \n or should you quietly run and hope he didn't hear you? Choose: Attack or Flee?")
    a1=input()
    time.sleep(2)
    if(a1.upper()=='ATTACK'):
        print(f"{player1} decided to attempt to attack him with the fireplace poker, but he's dead already! It does absolutely nothing. \n He grabs you and throws you across the room...")
        time.sleep(8)
        scene1()
    elif(a1.upper()=='FLEE'):
        print(f"{player1} slowly goes into the nearest room. You're not sure where you are, but you feel much safer in here. ")
        time.sleep(8)
        scene5()
    else:
        print("*******************Choose correctly!*******************")
        time.sleep(8)
        scene3()

def scene4():
    global player1
    logging.info(f"{player1} decides to go right. {datetime.datetime.now()}")
    print(f"{player1} walks down the halway in total darkness. You reach out to touch anything in front of you. You feel old furniture here and there, but nothing too concerning...yet. \n you stumble upon a dead end. You still can't see where to go. You feel around for anything at all. You come across a door. Do you think it's safe to go in? \n Choose: Go or Stay?")
    a1=input()
    time.sleep(2)
    if(a1.upper()=='GO'):
        print("You open the door and go inside")
        time.sleep(8)
        scene6()
    elif(a1.upper()=='STAY'):
        print("You decide to stay put.")
        time.sleep(8)
        scene7()
    else:
        print("*******************Choose correctly!*******************")
        time.sleep(8)
        scene4()

def scene5():
    global player1
    logging.info(f"{player1} slowly go into the nearest room to you. You're not sure where you are, but you feel much safer in here. {datetime.datetime.now()}")
    print(f"The room seems pretty lived in compared to everywhere else. There is everything a normal bedroom would have, \n a bed, night stand and dresser. In the middle of the dresser is a doll. \n As {player1} walks around the room you feel eyes diretly on you but you're not sure where it's coming from. \n You go look at the closet to see if there is anything you can use to protect yourself. You hear footsteps rattling around, and as your turn around, you notice the doll is gone. Inside the closet is a hidden doorway. \n Should you stay in the room or go through the doorway? Choose: Go or Stay?")
    a1=input()
    time.sleep(2)
    if(a1.upper()=='GO'):
        print("You decide to go through the hidden doorway. ")
        time.sleep(8)
        scene4()
    elif(a1.upper()=='STAY'):
        print("You decide to stay in the room.")
        time.sleep(8)
        scene7()
    else:
        print("*******************Choose correctly!*******************")
        time.sleep(8)
        scene5() 

def scene6():
    global player1
    logging.info(f"{player1} opens the door and go inside. {datetime.datetime.now()}")
    print(f"{player1} creeps around the room. Sun shines through the curtains so you can actually see outside. The are seems vaguely familiar, but you're not sure why. You notice the window is open, you're only on the 2nd floor. Should you try to jump out or stay and find another way out? Choose: Stay or go?")
    a1=input()
    time.sleep(2)
    if(a1.upper()=='STAY'):
        print("You decide to stay and go look for another way out. You head back to the door in which you came in and back out to the hallway.")
        time.sleep(8)
        scene4()
    elif(a1.upper()=='GO'):
        print("You to jump out the window, despite the risks. Fortunately, you land on spongey bushes and make a run for it. You know where you are now, the creepy house just outside of town. You are free and never look back.")
        time.sleep(3)
        print("YOU WIN")
    else:
        print("*******************Choose correctly!*******************")
        time.sleep(8)
        scene6() 

def scene7():
    global player1
    logging.info(f"{player1} decide to stay put. {datetime.datetime.now()}")
    print(f"{player1} can hear the doll inside the room. You decide to lock yourself in the closet until she is gone. The noise slowly fades away. Should you look out or stay longer? Choose look or stay?")
    a1=input()
    time.sleep(2)
    if(a1.upper()=='LOOK'):
        print("You decide to go back out to the room...")
        time.sleep(8)
        scene5()
    elif(a1.upper()=='STAY'):
        print("You decide to stay. Little do you know she's been in the closet with you the whole time! You black out...")
        time.sleep(8)
        scene1()
    else:
        print("*******************Choose correctly!*******************")
        time.sleep(8)
        scene7() 

scene1()
            