from enemies import Enemies,Whalen
from player import Player,Archer,Assasin,Warrior,Berserker,Fighter,Wizard
import random
chosen = Player.better_choose_class
chosen_use=chosen()
#all enemies
goblin = Enemies("Goblin","a little green thing;embarrising if you die to it",100,0.4,0.8,100)   
troll = Enemies("Troll","a slightly bigger thing;would be less embarrisiing", 200, 2, 1, 0.05)
giant = Enemies("Giant", "this is a big boy",1000, 10,1,0)
wolf = Enemies("Wolf","...its a wolf",75,0.5,0.5,100)
ogre = Enemies("ogre","this is a very very very big thing",210,1.9,1.2,0.1)
whalen = Whalen("Whalen","this is the final boss; you are most definity going to die; you will also fail his class",2000,300,500,100,9999999999999)
a_british_person =Enemies("a british person","horrible teeth",15,0.8,0.1,90)
a_french_person =Enemies("A french man","dont let it near you government",20,0.9,0.1,100)
slime = Enemies("slime","sliiiiime",10,5,0.1,100)
Dragon = Enemies("dragon","breathes fire and stuff",250,0.2,0.8,90)

#all classes
archer = Archer("Archer",90,  .35,  1.3,  0.8,  95,  1.1,  15,"infinite")
assasin=Assasin("assasin", 100, 90, 90, 150, 100, 25, 0,1000)
warrior=Warrior("warrior",150,125,75,100,100,75,0,1000)
b = Berserker("Berserker",100,150,30,75,100,15,0,1000000)
fighter = Fighter("fighter",150,100,1,175,100,10,0,100000)
wizard = Wizard("Wizard",150,10,100,100,150,300,0,10000000)
class TestAttack():
    def __init__(self,name,base_damage):
        self.name = name
        self.base_damage = base_damage
    def calculate(self,enemy): 
        return self.base_damage-(self.base_damage-(self.base_damage*enemy.defense))
    def __str__(self):
        return (f'name:{self.name};damage:{self.base_damage}')


attacks=[
    TestAttack("fireball",10),
    TestAttack("quick attack",20),
    TestAttack("heavy attack",30)
]

fireball = TestAttack("fireball",10)
quick_attack=TestAttack("quick attack",20)
heavy_attack = TestAttack("heavy attack",30)




def print_skills():
    for i,skillss in enumerate(attacks):
        print(f'{i+1}:{skillss.__dict__}')
        print()
print_skills()
def choose_skill():
    while True:
        try:
            choose_skills = int(input("what skill are you interested in(put the corresponding number):"))
            number_of_skills=3
            if number_of_skills>=choose_skills>=1:
                if choose_skills == 1:
                    return fireball
                elif choose_skills == 2:
                    return quick_attack
                elif choose_skills==3:
                    return heavy_attack
                else:
                    print("no1")
            else:
                print("It seems this wasn't one of the choices.Please enter a valid number.")
        except ValueError:
            print("Please enter an integer")




def adapting():
    global goblin
    if chosen == archer:
        goblin = Enemies("Goblin","a little green thing;embarrising if you die to it",99,0.4,0.8,99) 
        
    elif chosen == warrior:
        goblin = Enemies("Goblin","a little green thing;embarrising if you die to it",98,0.4,0.8,98)
adapting


if chosen:
    print("Here is your class:")
    print(chosen.__dict__)

def enemy_attack(player):
    random_skill=random.choice(attacks)
    player.health = player.health - random_skill.base_damage

def encounter(enemy,player):
    while player.health >0:
        if enemy.health > 0:
            print(enemy.__dict__)
            choose_skill()
            enemy.health = enemy.health - chosen_skill.base_damage
            print(enemy.health)

        elif enemy.health <=0:
            print("youve defeated the enemy,move on")
            print(f"you have gained {player.money} coins")
            break
    if player.health <=0:
        print("youve died")
chosen_skill=choose_skill()
encounter(goblin,chosen)