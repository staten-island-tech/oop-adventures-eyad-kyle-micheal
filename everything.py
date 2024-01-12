#remember to call methods after everything is defined
import random
from SBox import *


assasin_skill =[shadow_step,slash,PStab,dagger_throw]
archer_skill = [bow_throw,Rain,arrow_kick ,gun]
b_skill = [Rage_Pound,Baby_Rage,Slam,RepeatJab]
warrior_skill = [Piercing_Slash,impale,divider,slash]
wizard = [Fireball,Poison_Mist,Staff_Yeet]
fighter_skill=[Right_Hook,Brass_punch,uppercut]
    



class Player():
    displayed_skills =[]
    classes_choice=[]
    def __init__(self,name,health,attack,defense,mana,exp,money):
        self.name = name
        self.health = health
        self.attack =attack
        self.defense = defense
        self.mana = mana
        self.exp = exp
        self.money = money
    def __str__(self):
        return f'''{self.name},Health:{self.health}, attack:{self.attack},mana : {self.mana}, exp :{self.exp}money:{self.money}'''

    def print_classes():
        for i, classes in enumerate (Player.classes_choice):
            print(f'{i+1}. {classes}  ')
            print()

    def better_choose_class():
        while True:
            try:
                choose = int(input("what class are you interested in(put the corresponding number):"))
                number_of_classes=6
                if number_of_classes>=choose>=1:
                    global chosen_skills
                    global displayed_skills
                    if choose == 1:
                        chosen_skills = archer_skill
                        displayed_skills = list(attacks['Archerattacks'])
                        return archer
                    elif choose == 2:
                        chosen_skills = assasin_skill
                        displayed_skills = list(attacks['Assassin'])
                        return assasin
                    elif choose == 3:
                        chosen_skills = warrior_skill
                        displayed_skills = list(attacks['Warrior'])
                        return warrior
                    elif choose == 4:
                        chosen_skills = b_skill
                        displayed_skills = list(attacks['Berserker'])
                        return b
                    elif choose == 5:
                        chosen_skills = fighter_skill
                        displayed_skills = list (attacks['Fighter'])
                        return fighter
                    elif choose ==6:
                        return wizard
                else:
                    print("It seems this wasn't one of the choices.Please enter a valid number.")
            except ValueError:
                print("Please enter an integer")
    def print_your_class(chosen):
        if chosen:
            print(chosen.__dict__)
    def print_skills():
        for i, skills in enumerate (displayed_skills):
            print(f'{i+1}. {skills}  ')
            print()
    def choice():
        while True:
            try:
                x=(input("What skill do you want to use (check the corresponding number):"))
                x = int(x)
                if x <=len(displayed_skills):
                    print(f'You chose the skill \n{displayed_skills[x-1]}')
                    return chosen_skills[x-1]
                else:
                    print(":(")
            except ValueError:
                print("uh oh")
    def calculate_damage(player,enemy,damage):
        return player.attack*enemy.defense*damage
    def level(player):
        if player.exp>=100:
            player.mana_+=35
    




class Archer(Player):
    def __init__(self,name,health,attack,defense,mana,exp,money,ranged):
        super().__init__(name,health,attack,defense,mana,exp,money) 
        self.ranged = ranged
    def __str__(self):
        return super().__str__() + f''',range:{self.ranged}'''
class Assasin(Player):
    def __init__(self,name,health,attack,defense,mana,exp,money,stealth ):
        super().__init__(name,health,attack,defense,mana,exp,money)
        self.stealth = stealth
    def __str__(self):
        return super().__str__() + f'''Stealth: {self.stealth}'''
class Warrior(Player):
    def __init__(self,name,health,attack,defense,mana,exp,money,honor):
        super().__init__(name,health,attack,defense,mana,exp,money)
        self.honor = honor
    def __str__(self):
        return super().__str__() + f'''Honor: {self.honor}'''
class Berserker(Player):
    def __init__(self,name,health,attack,defense,mana,exp,money,rage):
        super().__init__(name,health,attack,defense,mana,exp,money)
        self.rage = rage
    def __str__(self):
        return super().__str__() + f'''Rage: {self.rage}'''
class Fighter(Player):
    def __init__(self,name,health,attack,defense,mana,exp,money,fighting_skills):
        super().__init__(name,health,attack,defense,mana,exp,money)
        self.fighting_skills = fighting_skills
    def __str__(self):
        return super().__str__() + f'''Fighting Skill: {self.fighting_skills}'''
class Wizard(Player):
    def __init__(self,name,health,attack,defense,mana,exp,money,magic):
        super().__init__(name,health,attack,defense,mana,exp,money)
        self.magic=magic
    def __str__(self):
        return super().__str__() + f'''Mastery of Magic: {self.magic}'''

Player.classes_choice=[
    Archer("Archer", 95, 1.15, 1.05,150, 0, 30, "infinite"),
    Assasin("Assasin", 115, 1.2, 1.1, 100, 0, 35, "infinite"),
    Warrior("Warrior",140,1.25,1.15,120,0,40,"infinite"),
    Berserker("Berserker",160,1.4,0.8,175,0,10,"infinite"),
    Fighter("Fighter",130,1.2,1.2,100,0,10,"infinite"),
    Wizard("Wizard",100,1.5,1.4,200,0,10,"infinite")



    
]
Player.print_classes()
archer = Archer("Archer", 95, 1.15, 1.05,150, 0, 30, "infinite")
assasin = Assasin("Assasin", 115, 1.2, 1.1, 100, 0, 35, "infinite")
warrior = Warrior("Warrior",140,1.25,1.15,120,0,40,"infinite")
b = Berserker("Berserker",160,1.4,0.8,175,0,10,"infinite")
fighter = Fighter("Fighter",130,1.2,1.2,100,0,10,"infinite")
wizard =Wizard("Wizard",100,1.5,1.4,200,0,10,"infinite")



class Enemies():
    def __init__(self,name,descripton,health,attack,defense):
        self.name = name
        self.description = descripton
        self.health = health
        self.attack = attack
        self.defense = defense

    
    def __str__(self):
        return f'Name:{self.name},Description:{self.description},Health:{self.health},Attack:{self.attack},Defense:{self.defense},'

    def adapting(player,enemy):
        for enemy in Enemies.enemies_list: 
            if player == archer:
                enemy.attack *= 1.5
                enemy.attack = round(enemy.attack,2)
            elif player == assasin:
                enemy.health *= 1.5
                enemy.health = round(enemy.health,2)
            elif player == warrior:
                enemy.defense *= 2
                enemy.defense =  round(enemy.defense,1)
            elif player == b:
                enemy.defense *= 2
                enemy.defense = round(enemy.defense,2)
            elif player == fighter:
                enemy.defense *=1.4
                enemy.defense=round(enemy.defense,2)
                enemy.attack*=1.8
                enemy.attack=round(enemy.attack,2)
            else:
                enemy.attack *=1.5
                enemy.attack=round(enemy.attack,2)
                enemy.defense*=1.1
                enemy.defense=round(enemy.defense,2)
    def donig_adapting(chosen):
        for i in range(1):
                Enemies.adapting(chosen,Enemies.enemies_list[i])
    def test_print_enemy():
        for i,enemy in enumerate(Enemies.enemies_list):
            print(f'{i+1}. {enemy.__dict__}')
    def calculate_damage(player,enemy,damage):
        return enemy.attack*player.defense*damage

print(Slash)

goblin = Enemies("goblin","ewf",100,0.8,0.6)
print(type(archer)) 
# troll = Enemies("Troll","a slightly bigger thing;would be less embarrisiing", 200, 2, 1, )
# giant = Enemies("Giant", "this is a big boy",1000, 10,1,0)
# wolf = Enemies("Wolf","...its a wolf",75,0.5,0.5,100)
# ogre = Enemies("ogre","this is a very very very big thing",210,1.9,1.2,0.1)
# a_british_person =Enemies("a british person","horrible teeth",15,0.8,0.1,90)
# a_french_person =Enemies("A french man","dont let it near you government",20,0.9,0.1,100)
# slime = Enemies("slime","sliiiiime",10,5,0.1,100)
# Dragon = Enemies("dragon","breathes fire and stuff",250,0.2,0.8,90)
# Enemies.enemies_list=[goblin,troll,giant,wolf,ogre,a_british_person,a_french_person,slime,Dragon]



class Floors():
    def __init__(self,number_of_enemies,order_of_enemies):
        self.number_of_enemies = number_of_enemies
        self.order_of_enemies = order_of_enemies
    def floor_over(floor):
        if floor.number_of_enemies >= 1:
            print("works")
        else:
            print("floors over!")
    def fighting():
        pass
    def encounter(enemy,player,coins_recieved):
            while player.health >0 and player.mana >0:
                
                if enemy.health > 0:
                    print(f'youve encountered a {enemy.name}. Defeat it to win!')
                    print(enemy.__dict__)
                    print()
                    Player.print_skills()
                    enemy.health-=Player.choice()
                    player.mana-=random.randint(20,30)
                    print(enemy.__dict__)
                    enemy_attack = random.randint(1,2)
                    player.health-=Enemies.calculate_damage(player,enemy,enemy_attack)
                    print(player.__dict__)
                elif enemy.health <=0:
                    print("youve defeated the enemy,move on")
                    print(f"you have gained {coins_recieved} coins")
                    print(f"your balance is now {player.money+coins_recieved}")
                    print(f'you now have {player.exp + random.randint(10,25)} experience')
                    break
            if player.health <=0 and player.mana <=0:
                print("youve died. Now you have to restart the game all over again because code is difficult.")                                                               

                






