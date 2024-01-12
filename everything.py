#remember to call methods after everything is defined
import random

class PasCommon():
    def c(name, skill_health):
        return (skill_health)
    
PasDam = random.randint(3, 50)

# Passive things
Bleeding = PasCommon.c('Bleed', 0.3)
Poisoned = PasCommon.c('Poison', 0.6)
Bled = (Bleeding * PasDam)
Poison = (Poisoned * PasDam)

class Active():
    def BaseActive(name, sd):
        return (sd)
    
    def NumberedActive(name, sd, count):
        return (sd * (count))
    
    def adhominum(name, sd, count, count2, count3):
        return (sd * count * count2 * count3)

# test zone
half = random.randint(1,2)
third = random.randint(1,3)
quarter = random.randint(1,4)
seventh = random.randint(1,7)
tenth = random.randint(1,10)

class Statis():
    def calc(percentage, name):
        x = random.randint(1, percentage)
        if x == percentage:
            return name
        else:
            return 0


# GENERAL SKILLS
Stab = Active.BaseActive('Stab', 6 )
Jab = Active.BaseActive('Jab', 4)

#CLASS SKILLS:
count = random.randint(3, 7) # Arrow count
jcount = random.randint(3, 6) # Berserker Jabs

# Warrior
Piercing_Slash = Active.BaseActive('Piercing Slash', 12) + Statis.calc(7, Bled)
impale = Active.BaseActive('Impale', 8) + Bled
divider = Active.BaseActive('Divider', 17) + Statis.calc(7, Bled)
slash = Active.BaseActive('Slash', 13) + Statis.calc(2, Bled)
big_sword= Active.BaseActive('Big Sword', 25) + Bled

# Fighter
Right_Hook = Active.BaseActive('Right Hook', 12) + Statis.calc(10, Bled)
Brass_punch = Active.BaseActive('Brass punch', 9) + Bled
# Chain Skill
uppercut = Active.BaseActive('Uppercut', 11) # 1/18 bleed | always chain
kick = Active.BaseActive('Kick', 14) # 1/20 bleed | 1/3 chain
slammer = Active.BaseActive('Slammer', 7) # 1/8 bleed | 1/7 chain
repeated = Active.NumberedActive('Repeated Kicks', 5, jcount)
fighter_skill = [Right_Hook,Brass_punch,uppercut,kick,slammer,repeated]


# Assassin
Slash = Active.BaseActive('Slash', 3) + Statis.calc(3, Bled) + Statis.calc(4, Poison)
PStab = Active.BaseActive('Poison Stab', 4) + Statis.calc(3, Bled) + Poison
dagger_throw = Active.BaseActive('Dagger Throw', 12) + Bled + Statis.calc(3, Poison)
# Chain Skill
shadow_step = Active.BaseActive('Shadow Step', 4) # 1/2 Poison | Chain chance 1/3
blow_dart = Active.NumberedActive('Blow Darts', 2, count) # Always Poison | Final chain 1/15
silencer = Active.adhominum('Silencer', 7, PasDam, count, jcount)

# Berserker 
Rage_Pound = Active.BaseActive('Pound', 13) + Statis.calc(2, Bled)
Baby_Rage = Active.BaseActive('Rage', 23) + Statis.calc(2, Bled)
Slam = Active.BaseActive('Slammer', 17) 
RepeatJab = Active.NumberedActive('Jabathon', 4, jcount) 

# Archer
Rain = Active.NumberedActive('Rain', 3, count) + Statis.calc(4, Bled)
arrow_kick = Active.BaseActive('Arrow Kick', 7) + Statis.calc(2, Bled)
gun = Active.NumberedActive('Gun', 2, (PasDam/count))

# Special Chain move
def archerchain():
    bow_chain = Active.NumberedActive('Bow Chain', 4, count)
    hells_arrow = Active.NumberedActive("Hell's arrow", 8, count) + Statis.calc(4, Bled) + Statis.calc(7, Poison)
    if quarter == 4:
        if tenth == 10:
            return hells_arrow
        else: return bow_chain
    else:
        return 0
bow_throw = Active.BaseActive('Bow Throw', 4) + archerchain()




lists=[Rain]
print(lists[0])


#used literally once
Burn = PasCommon.c('Burning', 0.4)
Burnt = (Burn * PasDam)

# Wizard
# Secret skills
Torosion = Active.adhominum('TT', 7, PasDam, PasDam, PasDam)
# Normal Skills
Fireball = Active.NumberedActive('Fireball', 7, Burnt)
Poison_Mist = Active.NumberedActive('Poison Fog', 7, Poisoned)
Staff_Yeet = Active.BaseActive('Staff_Throw', 7)










attacks = {



        'Warrior':{

                'Pierce:Deals 12 damage to target | 1/7 Bleed Chance',

                'Impale:Deals 8 damage to target + Bleed Damage',

                'Divide:Deals 17 damage to target | 1/7 Bleed Chance',

                'Slash:Deals 13 damage to target | 1/2 Bleed Chance'},

        'Wizard':{

                'Fireball:Deals 7 damage + burn damage to target',
                'Poison Mist: Surrounds the enemy in a poison fog, dealing 7 damage + Poison to target',
                'Staff Yeet:Throws staff at target at Mach 7, dealing 7 damage'},
    
        'Fighter':{

            'Uppercut:Deals 11 damage to target | 1/18 Bleed chance',
            'Kick:Deals 14 damage to target | 1/20 Bleed chance, 1/3 continuation chance',
            'Slam:Deals 7 damage to target | 1/8 Bleed chance, 1/7 continuation chance',
            'Combo:Deals base 5 damage to target 3-6 times',
            'Right Hook:Deals 12 damage to target | 1/10 Bleed Chance',
            'Brass Punch:Deals 9 damage to target + Bleed'},
            
        'Assassin':{

            'Shadow Step:Deals 4 damage to target. 1/2 Poison chance',
            'Blow DartDeals 2 damage 3-7 times. Always Poisons',
            'Silencer:Deals 7 damage a minimum of 27 times',
            'Slash:Deals 3 damage to target, with High Bleed & Poison chance',
            'Poison Stab 4 damage to target. 1/3 Bleed chance, Always Poisons',
            'Dagger Throw:Deals 12 damage to target. Always Bleed, 1/3 Poison'},

        "Berserker":{
            'Rage Pound:Deals 13 damage to target. 1/2 Bleed chance',
            'Baby Rage:Deals 23 damage to target. High Bleed chance',
            'Slam:Deals 17 damage to target',
            'Jabs:Deals 4 damage to target 3-6 times'},

        "Archerattacks" :{

            'Bow Throw:Deals 4 damage to target',
            'Arrow Rain:Deals 3 damage to target',
            'Arrow Kick:Deals 7 damage to target. 1/2 Bleed chance',
            'Gun:Deals 2 damage to target (Random) times'}}


has_kills=list(attacks['Archerattacks'])
assasin_skill =[shadow_step,blow_dart,silencer,slash,PStab,dagger_throw]
archer_skill = [bow_throw,Rain,arrow_kick ,gun]
b_skill = [Rage_Pound,Baby_Rage,Slam,RepeatJab]
warrior_skill = [Piercing_Slash,impale,divider,slash]

    



class TestAttack():
    def __init__(self,name,base_damage):
        self.name = name
        self.base_damage = base_damage
    def calculate(self,enemy): 
        return self.base_damage-(self.base_damage-(self.base_damage*enemy.defense))
    def __str__(self):
        return (f'name:{self.name};damage:{self.base_damage}')
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
    def printing_skills():
        for i,skill in enumerate(has_kills):
            print(f'{i+1}.{skill}')
    def choice():
        while True:
            try:
                x=(input(":::"))
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



goblin = Enemies("goblin","ewf",100,100,100)
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

assasin_skill =[shadow_step,blow_dart,silencer,slash,PStab,dagger_throw]
archer_skill = [bow_throw,Rain,arrow_kick ,gun]
b_skill = [Rage_Pound,Baby_Rage,Slam,RepeatJab]
warrior_skill = [Piercing_Slash,impale,divider,slash]
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
            while player.health >0:
                
                if enemy.health > 0:
                    print(f'youve encountered a {enemy.name}. Defeat it to win!')
                    print(enemy.__dict__)
                    print()
                    Player.print_skills()
                    enemy.health-=Player.choice()
                    print(enemy.__dict__)
                    enemy_attack = random.randint(15,20)
                    player.health-=enemy_attack.calculate
                    print(player.__dict__)
                elif enemy.health <=0:
                    print("youve defeated the enemy,move on")
                    print(f"you have gained {coins_recieved} coins")
                    print(f"your balance is now {player.money+coins_recieved}")
                    break
            if player.health <=0:
                print("youve died. Now you have to restart the game all over again because code is difficult.")                                                               

                






