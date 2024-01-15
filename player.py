#remember to call methods after everything is defined
import random
import sys
from SBox import *
from shop import *

Game_over=False

recover = 30
recover_health = 25
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
        return f'''Class:{self.name},Health:{self.health}, attack:{self.attack},mana : {self.mana}, exp :{self.exp},money:{self.money}'''

    def print_classes():
        for i, classes in enumerate (Player.classes_choice):
            print(f'{i+1}. {classes}  \n')
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
                        chosen_skills = wizard_skill
                        displayed_skills = list(attacks['Wizard'])
                        return wizard
                else:
                    print("It seems this wasn't one of the choices.Please enter a valid number.")
            except ValueError:
                print("Please enter an integer")
    def print_skills():
        for i, skills in enumerate (displayed_skills):
            print(f'{i+1}. {skills}  ')
        length=len(displayed_skills)+1
        length2=len(displayed_skills)+2
        print(f'{length}.Recover:recovers 30 mana')
        print(f'{length2}.Recover Helath: recover health')

    def calculate_damage(player,enemy,damage):
        damage = max(0,damage*player.attack-enemy.defense)
        return damage
    def level(player):
        if player.exp>=100:
            player.mana+=35
            player.exp-=100
    def reset(player):
        if player == archer:
            player.health = 95
            player.mana = 150
        elif player == assasin:
            player.health = 115
            player.mana = 100
        elif player == warrior:
            player.health = 140
            player.mana = 120
        elif player == b:
            player.health = 160
            player.mana = 175
        elif player == fighter:
            player.health = 130
            player.mana = 100
        elif player == wizard:
            player.health = 100
            player.mana = 200
    def choice():
        while True:
            try:
                a=int(input("What skill do you want to use (check the corresponding number):"))
                if 1<=a <=len(displayed_skills)+2:
                    if 1<=a<=len(displayed_skills):
                        print(f'You chose the skill \n{displayed_skills[a-1]}')
                        return chosen_skills[a-1]
                    elif a == len(displayed_skills)+1:
                        return recover
                    elif a == len(displayed_skills) +2:
                        return recover_health
                else:
                    print(":(")
            except ValueError:
                print("uh oh")

    
    def encounter(enemy,player,coins_recieved):
            x = random.randint(20,40)
            global Game_over
            if player.health<=0 or player.mana<=0:
                if not Game_over:
                    print("game over")
                    Game_over = True
                    sys.exit()

            while player.health >0 and player.mana >0:
                    if enemy.health > 0:
                        print(player.health)
                        print(f'youve encountered a {enemy.name}. Defeat it to win!')
                        print()
                        Player.print_skills()
                        choosing_skill = Player.choice()
                        if choosing_skill== recover:
                            player.mana +=recover
                            enemy_attack=random.randint(15,20)
                            player.health -= Enemies.calculate_damage(player,enemy,enemy_attack)
                            player.health = round(player.health,2)
                            print(player.__dict__)
                        elif choosing_skill == recover_health:
                            print(player.health)
                            player.health +=recover_health
                            player.mana -=10
                            player.health = round(player.health,2)
                            print(player.__dict__)

                        else:
                            abc=Player.calculate_damage(player,enemy,choosing_skill)
                            enemy.health-=abc
                            enemy.health = round(enemy.health,2)
                            player.mana-=random.randint(20,30)
                            print(enemy.__dict__)
                            enemy_attack = random.randint(1,2)
                            player.health-=Enemies.calculate_damage(player,enemy,enemy_attack)
                            player.health = round(player.health,2)
                            print(player.__dict__)
                    elif enemy.health <=0:
                        print("youve defeated the enemy,move on")
                        print(f"you have gained {coins_recieved} coins")
                        print(f"your balance is now {player.money+coins_recieved}")
                        print(f'you now have {(player.exp + x)} experience')
                        player.money+=coins_recieved
                        player.exp+=x
                        Player.level(player)
                        Player.reset(player)
                        Enemies.reset_enemy_pro(enemy)
                        print(enemy.health)
                        break
            if player.health <=0 or player.mana <=0:
                    print("youve died. Now you have to restart the game all over again because code is difficult.")
                    









assasin_skill =[shadow_step,slash,PStab,dagger_throw]
archer_skill = [bow_throw,Rain,arrow_kick ,gun]
b_skill = [Rage_Pound,Baby_Rage,Slam,RepeatJab]
warrior_skill = [Piercing_Slash,impale,divider,slash]
wizard_skill = [Fireball,Poison_Mist,Staff_Yeet]
fighter_skill=[Right_Hook,Brass_punch,uppercut]


Player.classes_choice=[
    Player("Archer", 95, 1.15, 1.05,150, 0, 30),
    Player("Assasin", 115, 1.2, 1.1, 100, 0, 35),
    Player("Warrior",140,1.25,1.15,120,0,40),
    Player("Berserker",160,1.4,0.8,175,0,10),
    Player("Fighter",130,1.2,1.2,100,0,10),
    Player("Wizard",100,1.5,1.4,200,0,10)]



archer = Player("Archer", 95, 1.15, 1.05,150, 0, 30 )
assasin = Player("Assasin", 115, 1.2, 1.1, 100, 0, 35 )
warrior = Player("Warrior",140,1.25,1.15,120,0,40)
b = Player("Berserker",160,1.4,0.8,175,0,10)
fighter = Player("Fighter",130,1.2,1.2,100,0,10)
wizard =Player("Wizard",100,1.5,1.4,200,0,10)

enemy_health=[100,150,250,75,210,10,250]

class Enemies():
    def __init__(self,name,descripton,health,attack,defense,value):
        self.name = name
        self.description = descripton
        self.health = health
        self.attack = attack
        self.defense = defense
        self.value = value

    
    def __str__(self):
        return f'Name:{self.name},Description:{self.description},Health:{self.health},Attack:{self.attack},Defense:{self.defense},'
    def calculate_damage(player,enemy,base_damage):
        damage=max(0,base_damage*player.attack-enemy.defense)
        return damage
    def reset_enemy(enemy):
        if enemy == goblin:
            enemy.health = 100
        elif enemy == troll:
            enemy.health = 150
        elif enemy == slime:
            enemy.health = 10
        elif enemy == giant:
            enemy.health = 250
        elif enemy == wolf:
            enemy.health = 75
        elif enemy== ogre:
            enemy.health = 210
        elif enemy == Dragon:
            enemy.health = 250
        elif enemy == super_giant:
            enemy.health = 1000
    def reset_enemy_pro(enemy):
        if isinstance(enemy,Enemies):
            enemy.health = enemy_health[enemy.value]
            



testing_class=Player("::",10000,10,10,1000,10,0)

goblin = Enemies("goblin","ewf",100,0.8,0.6,0)
troll = Enemies("Troll","a slightly bigger thing;would be less embarrisiing", 150,1.2,1.4,1 )
giant = Enemies("Giant", "very tanky, high attack, low defense",250,2,0.5,2)
wolf = Enemies("Wolf","...its a wolf",75,0.5,0.5,3)
ogre = Enemies("ogre","this is a very very very big thing",210,1.4,1,4)
slime = Enemies("slime","sliiiiime",10,1.01,0.1,5)
Dragon = Enemies("dragon","breathes fire and stuff",250,1.2,0.8,6)


                                         
super_giant = Enemies("Supergiant","bigger giant",1000,1.3,0.5,7)
                






