from stuff import Player,Archer,Assasin,Warrior,Berserker,Fighter,Wizard,Enemies,TestAttack
import random
#defining the choose class method to be reusable
Player.print_classes()
chosen = Player.better_choose_class()

def tutorial():
    has_skills=[
        TestAttack("yes",100)
    ]
    if chosen:
        print(f'Your chosen class is {chosen.name}')
    Player.print_skills()
    
tutorial()
