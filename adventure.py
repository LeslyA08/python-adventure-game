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
    print(f"{player1}, you slowly opens your eyes and look around you. The room is cold and dark, nowhere you have been before. \n You ask yourself, how did I get here? You slowly make your way onto the door, your hear sounds coming from the other side. \n Should you go out and investigate or should you stay put? \n Choose: stay or go?")
    a1 = input()
    time.sleep(2)
    if (a1.upper() == 'GO'):
        print("You decide to go out and investigate.")
        scene2()
    elif (a1.upper() == 'STAY'):
        print("You decide to do nothing. Something sinister is already in the room, and it is too late to change your mind.")
        scene1()
    else:
        print("*******************Choose correctly!*******************")
        scene1()

def scene2():
    logging.info(f"Player goes out and investigates. {datetime.datetime.now()}")
    print("The door creeks as you slowly open it. You are cautious at what may lie ahead. \n You look around, but see no one. You go down the hallway, you can't seem to find any light at all. \n A wall stops you in your tracks. You can barely make out that there is two ways to go. To your left is a faint light, to your right is pitch black darkness. Where will you go? Choose: Left or right? ")
    a1 = input()
    time.sleep(2)
    if(a1.upper()== 'LEFT'):
        print("You decide to go left")
        scene3()
    elif(a1.upper()== 'RIGHT'):
        print("You decide to go right")
        scene4()
    else:
        print("*******************Choose correctly!*******************")
        scene2()

def scene3():
    logging.info(f"Player decides to go left. {datetime.datetime.now()}")
    print("As you walk towards the light, you notice a faint figure. You can barely make out a shape of a man... a rotting man. You freeze in place, contemplating what to do. You grab fireplace poker to defend yourself. Should you attack? or should you quietly run and hope he didn't hear you? Choose: Attack or Flee?")
    a1=input()
    time.sleep(2)
    if(a1.upper()=='ATTACK'):
        print("You decide to attempt to attack him with the fireplace poker, but he's dead already! It does absolutely nothing. He grabs you and throws you across the room...")
        scene1()
    elif(a1.upper()=='FLEE'):
        print("You slowly go into the nearest room to you. You're not sure where you are, but you feel much safer in here. ")
        scene5()
    else:
        print("*******************Choose correctly!*******************")
        scene3()

def scene4():
    logging.info(f"{datetime.datetime.now()}")
    print("You walk down the halway in total darkness. You reach out to touch anything in front of you. You feel old furniture here and there, but nothing too concerning...yet. \n you stumble upon a dead end. You still can't see where to go. You feel around for anything at all. You come across a door. Do you think it's safe to go in? \n Choose: Go or Stay?")
    a1=input()
    time.sleep(2)
    if(a1.upper()=='GO'):
        print("You open the door and go inside")
        scene6()
    elif(a1.upper()=='STAY'):
        print("You decide to stay put.")
        scene7()
    else:
        print("*******************Choose correctly!*******************")
        scene4()

def scene5():
    logging.info(f"{datetime.datetime.now()}")
    print("The room seems pretty lived in compared to everywhere else. There is everything a normal bedroom would have, a bed, night stand and dresser. In the middle of the dresser is a doll. \n As you walk around the room you feel eyes diretly on you but you're not sure where it's coming from. \n You go look at the closet to see if there is anything you can use to protect yourself. You hear footsteps rattling around, and as your turn around, you notice the doll is gone. Inside the closet is a hidden doorway. Should you stay in the room or go through the doorway? Choose: Go or Stay?")
    a1=input()
    time.sleep(2)
    if(a1.upper()=='GO'):
        print("You decide to go through the hidden doorway. ")
        scene4()
    elif(a1.upper()=='STAY'):
        print("right")
        scene7()
    else:
        print("*******************Choose correctly!*******************")
        scene5() 

def scene6():
    logging.info(f"{datetime.datetime.now()}")
    print("Hello, left or right")
    a1=input()
    time.sleep(2)
    if(a1.upper()=='LEFT'):
        print("Go")
        scene4()
    elif(a1.upper()=='RIGHT'):
        print("you win")
    else:
        print("*******************Choose correctly!*******************")
        scene6() 

def scene7():
    logging.info(f"{datetime.datetime.now()}")
    print("Hello, left or right")
    a1=input()
    time.sleep(2)
    if(a1.upper()=='LEFT'):
        print("Go")
        scene5()
    elif(a1.upper()=='RIGHT'):
        print("you lose")
        scene1()
    else:
        print("*******************Choose correctly!*******************")
        scene7() 

scene1()
            