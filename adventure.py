import time 

def scene1():
    print("You slowly open your eyes and look around you. The room is cold and dark, nowhere you have been before. \n You ask yourself, how did I get here? You slowly make your way onto the door, your hear sounds coming from the other side. \n Should you go out and investigate or should you stay put? \n Choose: stay or go?")
    a1 = input()
    time.sleep(2)
    if (a1.upper() == 'GO'):
        print("You decide to go out and investigate.")
        scene2()
    elif (a1.upper() == 'STAY'):
        print("You decide to do nothing. Something sinister is already in the room, and it is too late to change your mind.")
    else:
        print("*******************Choose correctly!*******************")
        scene1()

def scene2():
    print("The door creeks as you slowly open it. You are cautious at what may lie ahead. \n You look around, but see no one. You go down the hallway, you can't seem to find any light at all. \n A wall stops you in your tracks. You can barely make out that there is two ways to go. To your left is a faint light, to your right is pitch black darkness. Where will you go? Choose: Left or right? ")
    a1 = input()
    time.sleep(2)
    if(a1.upper()== 'LEFT'):
        print("You go decide to go left")
        scene3()
    elif(a1.upper()== 'RIGHT'):
        print("You decide to go right")
        scene4()
    else:
        print("*******************Choose correctly!*******************")
        scene2()
def scene3():
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

scene1()
            