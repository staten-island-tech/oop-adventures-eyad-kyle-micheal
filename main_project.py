from working import Player,Archer,Assasin,Warrior,Berserker,Wizard,Fighter,Enemies,Floors
from SBox import Active,PasCommon,archer_skill,warrior_skill,b_skill,assasin_skill,fighter_skill
from merchant_vendor import mooney

def tutorial_tiny():
    print("Helo adventurer! You have made it to the tower of chellenges Before doing anything else, you will have to learn the basics. First, you'll have to choose your class")
Player.print_classes()
chosen = Player.better_choose_class()
def actual():
    print(f"""Great! You've sucessfullay chosen a class ! Here aare your stats 
          {chosen.__dict__} """)

actual()