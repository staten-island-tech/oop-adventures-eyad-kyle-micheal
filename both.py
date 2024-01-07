#remember to call methods after everything is defined
import random

class PasCommon():
    def c(name, skill_health):
        return (skill_health)
PasDam = random.randint(3, 50)

# Passive Skills
Bleeding = PasCommon.c('Bleed', 0.3)
Regeneration = PasCommon.c('Heal', 0.2)
Poisoned = PasCommon.c('Poison', 0.6)
Burn = PasCommon.c('Burning', 0.4)

# Direct Damage from Passive Skills
Bled = (Bleeding * PasDam)
Regen = (Regeneration * PasDam)
Poison = (Poisoned * PasDam)
Burnt = (Burn * PasDam)

class Active():
    def BaseActive(name, sd):
        return (sd)
    
    def NumberedActive(name, sd, count):
        return (sd * (count))
    
    def adhominum(name, sd, count, count2, count3):
        return (sd * count * count2 * count3)

# GENERAL SKILLS
Stab = Active.BaseActive('Stab', 6 )
Jab = Active.BaseActive('Jab', 4)

#CLASS SKILLS:

count = random.randint(3, 7) # Arrow count
jcount = random.randint(3, 6) # Berserker Jabs

# Warrior
Piercing_Slash = Active.BaseActive('Piercing Slash', 12) #Bleed Chance 1/7
impale = Active.BaseActive('Impale', 8) # Bleed Always
print(Piercing_Slash)
divider = Active.BaseActive('Divider', 17) #Bleed 1/7
slash = Active.BaseActive('Slash', 13) # Bleed 1/2


#Secret Skill | Warrior | Must input specific number to activate
big_sword= Active.BaseActive('Big Sword', 25)

# Fighter
Right_Hook = Active.BaseActive('Right Hook', 12) #Bleed Chance 1/10
Brass_punch = Active.BaseActive('Brass punch', 9) # Always Bleed
# Chain Skill
uppercut = Active.BaseActive('Uppercut', 11) # 1/18 bleed | always chain
kick = Active.BaseActive('Kick', 14) # 1/20 bleed | 1/3 chain
slammer = Active.BaseActive('Slammer', 7) # 1/8 bleed | 1/7 chain
repeated = Active.NumberedActive('Repeated Kicks', 5, jcount)
fighter_skill = [Right_Hook,Brass_punch,uppercut,kick,slammer,repeated]
# Assassin
Slash = Active.BaseActive('Slash', 3) #Bleed Chance 2/3 | Poison Chance 4/5
PStab = Active.BaseActive('Poison Stab', 4) # 1/3 Bleed Chance | Always Poison
dagger_throw = Active.BaseActive('Dagger Throw', 12) # Always Bleed | 1/3 Poison
# Chain Skill
shadow_step = Active.BaseActive('Shadow Step', 4) # 1/2 Poison | Chain chance 1/3
blow_dart = Active.NumberedActive('Blow Darts', 2, count) # Always Poison | Final chain 1/15
silencer = Active.adhominum('Silencer', 7, PasDam, count, jcount)

# Berserker 
Rage_Pound = Active.BaseActive('Pound', 13) # 1/2 Bleed Chance to enemies 
Baby_Rage = Active.BaseActive('Rage', 23) # 3/5 Bleed Chance to enemies
Slam = Active.BaseActive('Slammer', 17) 
RepeatJab = Active.NumberedActive('Jabathon', 4, jcount) 

# Archer
Rain = Active.NumberedActive('Rain', 3, count) #Bleed Chance 1/4 
arrow_kick = Active.BaseActive('Arrow Kick', 7) # Bleed 1/2
gun = Active.NumberedActive('Gun', 2, (PasDam/count)) # Side effects maybe?
# Special Chain move
bow_throw = Active.BaseActive('Bow Throw', 4) #Chance to activate chain skill (1/4)
bow_chain = Active.NumberedActive('Bow Chain', 4, count) #Final skill chance 1/12
hells_arrow = Active.NumberedActive("Hell's arrow", 8, count) #1/5 bleed, 1/8 poison 

lists=[Rain]
print(lists[0])


# Wizard
# Secret skills
Torosion = Active.adhominum('TT', 7, PasDam, PasDam, PasDam)
# Normal Skills
Fireball = Active.NumberedActive('Fireball', 7, Burnt)
Poison_Mist = Active.NumberedActive('Poison Fog', 7, Poisoned)
Staff_Yeet = Active.BaseActive('Staff_Throw', 7)











attacks = {

    'passive': {

        'Bleed': {
        "Bleeding":PasCommon.c('Bleed', 0.3),'Description':'Deals 0.3 bleed damage to target'},

        'Regen':{
        "Regeneration":PasCommon.c('Heal', 0.2),'Description':'Heals 0.2 health to target'},

        'Poison':{
        "Poisoned":PasCommon.c('Poison', 0.6),'Description':'Deals 0.6 poison damage to target'},

        'Burn':{
        "Burnt":PasCommon.c('Burning', 0.4),'Description':'Deals 0.4 burn damage to target'}},


    'active':{

        'General':{
            'Secret':{
                'Stabathon':{
                "Damage":Active.NumberedActive('Stabathon', 6, count), 'Description':'Call me London, deals 6 damage per stab'},

                'Status Hell':{
                "Damage":Active.adhominum('Status Hell', 2, Burnt, Bled, Poison), 'Description':'Shadow Wizard Money Gang | We love casting spells'}},


            'Normal':{
                'Stab':{
                "Damage":Active.BaseActive('Stab', 6), "Description":'Deals 6 damage to the opps'},

                'Jab':{
                "Damage":Active.BaseActive('Jab', 4), "Description":'Deals 4 damage to the opps'},
            
                'Stomp':{
                "Damage":Active.BaseActive('Stomp', 5), "Description":'Deals 5 damage to the opps'}}},


        'Warrior':{

            'Secret':{
                'Divine Slash':{
                "Damage":Active.BaseActive('big_sword', 25), 'Description':'Deals 15 damage to target'}},


            'Normal':{
                'Pierce':{
                "Damage":Active.BaseActive('Piercing Slash', 12), 'Description': 'Deals 12 damage to target | 1/7 Bleed Chance'},

                'Impale':{
                "Damage":Active.BaseActive('Impale', 8), 'Description': 'Deals 8 damage to target + Bleed Damage'},

                'Divide':{
                "Damage":Active.BaseActive('Divider', 17), 'Description': 'Deals 17 damage to target | 1/7 Bleed Chance'},

                'Slash':{
                "Damage":Active.BaseActive('Slash', 13), 'Description': 'Deals 13 damage to target | 1/2 Bleed Chance'}}},

        'Wizard':{
            'Secret':{
                'Torosion':{
                "Damage":Active.adhominum('TT', 7, PasDam, PasDam, PasDam), 'Description': 'Deals massive damage multiplied by 7'}},
            
            'Normal':{
                'Fireball':{
                "Damage":Active.NumberedActive('Fireball', 7, Burnt), 'Description': 'Deals 7 damage + burn damage to target'},
                'Poison Mist':{
                "Damage":Active.NumberedActive('Poison Fog', 7, Poisoned), 'Description': 'Surrounds the enemy in a poison fog, dealing 7 damage + Poison to target'},
                'Staff Yeet':{
                "Damage":Active.BaseActive('Staff_Throw', 7), 'Description': 'Throws staff at target at Mach 7, dealing 7 damage'}}},
    
        'Fighter':{
            'Chain':{
            'Uppercut':{
            "Damage":Active.BaseActive('Uppercut', 11), 'Description':'Deals 11 damage to target | 1/18 Bleed chance'},
            'Kick':{
            "Damage":Active.BaseActive('Kick', 14), 'Description':'Deals 14 damage to target | 1/20 Bleed chance, 1/3 continuation chance'},
            'Slam':{
            "Damage":Active.BaseActive('Slammer', 7), 'Description':'Deals 7 damage to target | 1/8 Bleed chance, 1/7 continuation chance'},
            'Combo':{
            "Damage":Active.NumberedActive('Combo Kicks', 5, jcount), 'Description':'Deals base 5 damage to target 3-6 times'}},

            'Normal':{
            'Right Hook':{
            "Damage":Active.BaseActive('Right Hook', 12), 'Description':'Deals 12 damage to target | 1/10 Bleed Chance'},
            'Brass Punch':{
            "Damage":Active.BaseActive('Brass Punch', 9), 'Description':'Deals 9 damage to target + Bleed'}}},
            
        'Assassin':{
            'Chain':{
            'Shadow Step':{
            "Damage":Active.BaseActive('Shadow Step', 4), 'Description':'Deals 4 damage to target. 1/2 Poison chance'},
            'Blow Dart':{
            "Damage":Active.NumberedActive('Blow Darts', 2, count), 'Description':'Deals 2 damage 3-7 times. Always Poisons'},
            'Silencer':{
            "Damage":Active.adhominum('Silencer', 7, PasDam, count, jcount), 'Description':'Deals 7 damage a minimum of 27 times'}},

            'Normal':{
            'Slash':{
            "Damage":Active.BaseActive('Slash', 3), 'Description':'Deals 3 damage to target, with High Bleed & Poison chance'},
            'Poison Stab':{
            "Damage":Active.BaseActive('Poison Stab', 4), 'Description':'Deals 4 damage to target. 1/3 Bleed chance, Always Poisons'},
            'Dagger Throw':{
            "Damage":Active.BaseActive('Dagger Throw', 12), 'Description':'Deals 12 damage to target. Always Bleed, 1/3 Poison'}}},

        "Berserker":{
            'Normal':{
            'Rage Pound':{
            "Damage":Active.BaseActive('Pound', 13), 'Description':"Deals 13 damage to target. 1/2 Bleed chance"},
            'Baby Rage':{
            "Damage":Active.BaseActive('Rage', 23), 'Description':"Deals 23 damage to target. High Bleed chance"},
            'Slam':{
            "Damage":Active.BaseActive('Slammer', 17), 'Description':"Deals 17 damage to target"},
            'Jabs':{
            "Damage":Active.NumberedActive('Jabathon', 4, jcount), 'Description':"Deals 4 damage to target 3-6 times"}}},

        "Archerattacks" :{
            'Chain':{
            'Bow Throw:Deals 4 damage to target':{
            "Damage":Active.BaseActive('Bow Throw', 4), 'Description':'Deals 4 damage to target'},
            'Bow Chain':{
            "Damage":Active.NumberedActive('Bow Chain', 4, count), 'Description':'Deals 4 damage to target 3-7 times'},
            'Hells Arrow':{
            "Damage":Active.NumberedActive("Hell's arrow", 8, count), 'Description':'Deals 8 damage to target 3-7 times. Low Poison & Bleed chance'}},

            'Normal':{
            'Arrow Rain':{
            "Damage":Active.NumberedActive('Rain', 3, count), 'Description':'Deals 3 damage to target'},
            'Arrow Kick':{
            "Damage":Active.BaseActive('Arrow Kick', 7), 'Description':'Deals 7 damage to target. 1/2 Bleed chance'},
            'Gun':{
            "Damage":Active.NumberedActive('Gun', 2, (PasDam/count)), 'Description':'Deals 2 damage to target (Random) times'}}}}}

has_kills={}
has_kills=attacks['active']['Warrior']['Normal']



class Player():
    displayed_skills =[]
    classes_choice=[]
    potential_classes=[]
    has_skills={}
    def __init__(self,name,health,attack,defense,money):
        self.name = name
        self.health = health
        self.attack =attack
        self.defense = defense
        self.money = money
    def __str__(self):
        return f'''{self.name},Health:{self.health}, attack:{self.attack},money:{self.money}'''

    def print_classes():
        for i, classes in enumerate (Player.classes_choice):
            print(f'{i+1}. {classes}  ')
            print()
    @classmethod
    def better_choose_class(cls):
        while True:
            try:
                choose = int(input("what class are you interested in(put the corresponding number):"))
                number_of_classes=6
                if number_of_classes>=choose>=1:
                    global chosen_skills
                    global displayed_skills
                    if choose == 1:
                        chosen_skills = archer_skill
                        displayed_skills = list(attacks['active']['Archerattacks']['Chain']) + list(attacks['active']['Archerattacks']['Normal'])
                        return archer
                    elif choose == 2:
                        chosen_skills = assasin_skill
                        return assasin
                    elif choose == 3:
                        chosen_skills = warrior_skill
                        return warrior
                    elif choose == 4:
                        chosen_skills = b_skill
                        return b
                    elif choose == 5:
                        chosen_skills = fighter_skill
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
    def assign_skills(chosen):
        if chosen == archer:
            Player.has_skills=archer

    def choose_skill():
        Player.print_skills
        global choice
        try:
            choice = int(input("Choose a skill by entering its number: "))
            if 1 <= choice <= len(chosen_skills):
                return chosen_skills[choice-1]
            else:
                print("Invalid choice. Please enter a valid skill number.")
                return None
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None


class Archer(Player):
    def __init__(self,name,health,attack,defense,money,ranged):
        super().__init__(name,health,attack,defense,money) 
        self.ranged = ranged
    def __str__(self):
        return super().__str__() + f''',range:{self.ranged}'''
class Assasin(Player):
    def __init__(self,name,health,attack,defense,money,stealth ):
        super().__init__(name,health,attack,defense,money)
        self.stealth = stealth
    def __str__(self):
        return super().__str__() + f'''Stealth: {self.stealth}'''
class Warrior(Player):
    def __init__(self,name,health,attack,defense,money,honor):
        super().__init__(name,health,attack,defense,money)
        self.honor = honor
    def __str__(self):
        return super().__str__() + f'''Honor: {self.honor}'''
class Berserker(Player):
    def __init__(self,name,health,attack,defense,money,rage):
        super().__init__(name,health,attack,defense,money)
        self.rage = rage
    def __str__(self):
        return super().__str__() + f'''Rage: {self.rage}'''
class Fighter(Player):
    def __init__(self,name,health,attack,defense,money,fighting_skills):
        super().__init__(name,health,attack,defense,money)
        self.fighting_skills = fighting_skills
    def __str__(self):
        return super().__str__() + f'''Fighting Skill: {self.fighting_skills}'''
class Wizard(Player):
    def __init__(self,name,health,attack,defense,money,magic):
        super().__init__(name,health,attack,defense,money)
        self.magic=magic
    def __str__(self):
        return super().__str__() + f'''Mastery of Magic: {self.magic}'''

Player.classes_choice=[
        Archer("Archer",95,100,100,0,"infinite"),
        Assasin("Assasin", 115,100,100,0,"infinite"),
        Warrior("Warrior",150,100,100,0,"infinite"),
        Berserker("Berserker",100,100,100,1000,"infinite"),
        Fighter("Fighter",150,100,100,0,"infinite"),
        Wizard("Wizard",150,100,100,0,"infinite")
]
archer = Archer("Archer",95,100,100,0,"infinite")
assasin = Assasin("Assasin", 115,100,100,0,"infinite")
warrior = Warrior("Warrior",150,100,100,0,"infinite")
b = Berserker("Berserker",100,100,100,0,"infinite")
fighter = Fighter("Fighter",150,100,100,0,"infinite")
wizard = Wizard("Wizard",150,100,100,0,"infinite")



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
archer_skill = [bow_throw,bow_chain,hells_arrow,arrow_kick ,gun]
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
                    print(enemy.__dict__)
                    print()
                    Player.print_skills()
                    Player.choose_skill()
                    


                elif enemy.health <=0:
                    print("youve defeated the enemy,move on")
                    print(f"you have gained {coins_recieved} coins")
                    print(f"your balance is now {player.money+coins_recieved}")
                    break
            if player.health <=0:
                print("youve died")
Player.print_classes()
Player.better_choose_class()
Player.print_skills()
chosen_attack = Player.choose_skill()
print(displayed_skills[choice-1])
