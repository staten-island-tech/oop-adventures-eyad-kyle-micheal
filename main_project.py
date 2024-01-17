from player import *
from SBox import *
from shop import *
Game_over=False
def tutorial_tiny():
    print("Hello adventurer! You have made it to the tower of challenges Before doing anything else, you will have to learn the basics. First, you'll have to choose your class")
tutorial_tiny()
Player.print_classes()
chosen = Player.better_choose_class()


def actual():
    print(f"""Great! You've sucessfullay chosen a class ! Here aare your stats \n {chosen.__dict__} """)
    print(f'''The "attack" stat is a multiplier as to how much damage you will do. For example, since you have an attak stat of {chosen.attack} you will deal {chosen.attack} times damage on you attacks. 
          That being said, these attacks will also go through the enemies defense stat,meaning that if you do an attack of 10 damage, you will actually do an attack of 10*{chosen.attack} * enenmy defense.
          You also have a "mana" which is similar to you health. You consume mana when attacking. The more damage you do, the more mana you consume. If your mana reaches 0, you will die; similarly to if your health reaches 0. ''')
    print(f"\nNow that you've chosen a class, you should learn how to fight. Here's a goblin to start with. Be carful, you only have one life so if you die you'll have to restart.")
    Player.encounter(goblin,chosen,15)
    Player.encounter(slime,chosen,10)
actual()
Shop.buying(chosen)


def floor1():
    print(f"Great! Now that we've finished the tutorial, we can now move on to floor 1. Good luck!")
    Player.encounter(goblin,chosen,30)
    Player.encounter(goblin,chosen,10)
    Player.encounter(wolf,chosen,10)
    Player.encounter(troll,chosen,20)
floor1()
c=Shop.buying(chosen)


def floor2():
    print(f"Congrats! You've sucessfully cleared floor one. Now time for floor 2")
    Player.encounter(troll,chosen,15)
    Player.encounter(ogre,chosen,25)
    Player.encounter(Dragon,chosen,20)
    c
    
floor2()

def floor3():
    print(f'Floor 3 start:\n')
    Player.encounter(giant,chosen,30)
    Player.encounter(Dragon,chosen,25)
    Player.encounter(troll,chosen,10)
    Player.encounter(giant,chosen,50)
    c
floor3()
def floor4():
    print(f'floor 4 starts\n')
    Player.encounter(Dragon,chosen,20)
    Player.encounter(Dragon,chosen,20)
    Player.encounter(troll,chosen,20)
    Player.encounter(Dragon,chosen,40)
    Player.encounter(Dragon,chosen,10)
    Player.encounter(slime,chosen,2)
    c
floor4()
def floor5():
    print(f'Floor five start:')
    Player.encounetr(giant,chosen,30)
    Player.encounter(Dragon,chosen,20)
    Player.encounter(troll,chosen,15)
    Player.encounter(troll,chosen,20)
    Player.encounter(giant,chosen,10)
    Player.encounter(goblin,chosen,5)
    c
floor5()
def final_floor():
    print("Final floor:")
    Player.encounter(super_giant,chosen,30)
    Player.encounter(super_giant, chosen,30)
    Player.encounter(super_giant,chosen,30)
final_floor()






