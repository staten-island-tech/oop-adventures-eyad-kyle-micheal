from everything import *

def tutorial_tiny():
    print("Helo adventurer! You have made it to the tower of chellenges Before doing anything else, you will have to learn the basics. First, you'll have to choose your class")
Player.print_classes()
chosen = Player.better_choose_class()
def actual():
    print(f"""Great! You've sucessfullay chosen a class ! Here aare your stats \n {chosen.__dict__} """)
    print(f'The "attack" stat is a multiplier as to how much damage you will do. For example, since you have an attak stat of {chosen.attack} you will deal {chosen.attack} times damage on you attacks. That being said, these attacks will also go through the enemies defense stat,meaning that if you do an attack of 10 damage, you will actually do an attack of 10*{chosen.attack} * enenmy defense.')
    print(f"\nNow that you've chosen a class, you should learn how to fight. Here's a goblin to start with")
    Floors.encounter(goblin,chosen,5)
    

actual()


