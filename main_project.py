from working import Player,Archer,Assasin,Warrior,Berserker,Wizard,Fighter,Enemies,Floors

from merchant_vendor import mooney

def tutorial_tiny():
    print("Helo adventurer! You have made it to the tower of chellenges Before doing anything else, you will have to learn the basics. First, you'll have to choose your class")
Player.print_classes()
chosen = Player.better_choose_class()
def actual():
    print(f"""Great! You've sucessfullay chosen a class ! Here aare your stats 
          {chosen.__dict__} """)
    print(f"Now, it's time to show you how to battle!")

actual()