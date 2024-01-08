#remember to call methods after everything is defined
from SBox import PasCommon,PasDam,Active,jcount,count,attacks
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
                        displayed_skills = list(attacks['active']['Archerattacks']['Normal'])
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
Piercing_Slash = Active.BaseActive('Piercing Slash', 12) #Bleed Chance 1/7
impale = Active.BaseActive('Impale', 8) # Bleed Always
print(Piercing_Slash)
divider = Active.BaseActive('Divider', 17) #Bleed 1/7
slash = Active.BaseActive('Slash', 13) # Bleed 1/2


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
print(Player.displayed_skills[choice-1])





