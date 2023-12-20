from stuff import Player,Archer,Assasin,Warrior,Berserker,Fighter,Wizard,Enemies,TestAttack
import random
#defining the choose class method to be reusable
Player.print_classes()
chosen = Player.better_choose_class()
Player.print_your_class(chosen)
