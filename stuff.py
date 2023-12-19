#remember to call methods after everything is defined
class TestAttack():
    def __init__(self,name,base_damage):
        self.name = name
        self.base_damage = base_damage
    def calculate(self,enemy): 
        return self.base_damage-(self.base_damage-(self.base_damage*enemy.defense))
    def __str__(self):
        return (f'name:{self.name};damage:{self.base_damage}')
class Player():
    classes_choice=[]
    potential_classes=[]
    has_skills=[]
    def __init__(self,name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money):
        self.name = name
        self.health = health
        self.melee_attack = melee_attack
        self.ranged_attack =ranged_attack
        self.speed = speed
        self.intelligence = intelligence
        self.magic_talent = magic_talent
        self.money = money
    def __str__(self):
        return f'''{self.name},Health:{self.health},melee attack:{self.melee_attack},ranged attack:{self.ranged_attack},speed:{self.speed},intelligense:{self.intelligence},magic talent:{self.magic_talent},money:{self.money}'''
    @classmethod
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
                    if choose == 1:
                        return archer
                    elif choose == 2:
                        return assasin
                    elif choose == 3:
                        return warrior
                    elif choose == 4:
                        return b
                    elif choose == 5:
                        return fighter
                    elif choose ==6:
                        return wizard
                else:
                    print("It seems this wasn't one of the choices.Please enter a valid number.")
            except ValueError:
                print("Please enter an integer")
    def print_skills():
        for i, skills in enumerate (Player.has_skiils):
            print(f'{i+1}. {skills}  ')
            print()
    def choose_skill():
        Player.print_skills()

        try:
            choice = int(input("Choose a skill by entering its number: "))
            if 1 <= choice <= len(Player.has_skills):
                return Player.has_skills[choice - 1]
            else:
                print("Invalid choice. Please enter a valid skill number.")
                return None
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None


class Archer(Player):
    def __init__(self,name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money,suuper):
        super().__init__(name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money) 
        self.suuper = suuper
    def __str__(self):
        return super().__str__() + f''',Ranged:{self.suuper}'''
class Assasin(Player):
    def __init__(self,name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money,stealth ):
        super().__init__(name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money)
        self.stealth = stealth
    def __str__(self):
        return super().__str__() + f'''Stealth: {self.stealth}'''
class Warrior(Player):
    def __init__(self,name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money,honor):
        super().__init__(name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money)
        self.honor = honor
    def __str__(self):
        return super().__str__() + f'''Honor: {self.honor}'''
class Berserker(Player):
    def __init__(self,name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money,rage):
        super().__init__(name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money)
        self.rage = rage
    def __str__(self):
        return super().__str__() + f'''Rage: {self.rage}'''
class Fighter(Player):
    def __init__(self,name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money,fighting_skills):
        super().__init__(name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money)
        self.fighting_skills = fighting_skills
    def __str__(self):
        return super().__str__() + f'''Fighting Skill: {self.fighting_skills}'''
class Wizard(Player):
    def __init__(self,name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money,magic):
        super().__init__(name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money)
        self.magic=magic
    def __str__(self):
        return super().__str__() + f'''Mastery of Magic: {self.magic}'''
class SecretClass(Player):
    def __init__(self,name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money,secrets):
        super().__init__(name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money)
        self.secrets = secrets
    def __str__(self):
        return super().__str__() + f''',Secrets:{self.secrets}'''
Player.classes_choice=[
        Archer("Archer",90,  .35,  1.3,  0.8,  95,  1.1,  15,"infinite"),
        Assasin("Assasin", 100, 90, 90, 150, 100, 25, 0,1000),
        Warrior("Warrior",150,125,75,100,100,75,0,1000),
        Berserker("Berserker",100,150,30,75,100,15,0,1000000),
        Fighter("Fighter",150,100,1,175,100,10,0,100000),
        Wizard("Wizard",150,10,100,100,150,300,0,10000000),
]
archer = Archer("Archer",90,  .35,  1.3,  0.8,  95,  1.1,  15,"infinite")
assasin=Assasin("assasin", 100, 90, 90, 150, 100, 25, 0,1000)
warrior=Warrior("warrior",150,125,75,100,100,75,0,1000)
b = Berserker("Berserker",100,150,30,75,100,15,0,1000000)
fighter = Fighter("fighter",150,100,1,175,100,10,0,100000)
wizard = Wizard("Wizard",150,10,100,100,150,300,0,10000000)



class Enemies():
    def __init__(self,name,descripton,health,attack,defense, speed):
        self.name = name
        self.description = descripton
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
    
    def __str__(self):
        return f'''Name:{self.name},
Description:{self.description},
Health:{self.health},
Attack:{self.attack},
Defense:{self.defense},
speed:{self.speed}'''

    def adapting(player,enemy):
        for enemy in Enemies.enemies_list: 
            if player == archer:
                enemy.attack *= 1.5
                enemy.attack = round(enemy.attack,2)
            elif player == assasin:
                enemy.health *= 1.5
                enemy.health = round(enemy.health,2)
            elif player == warrior:
                enemy.speed *= 2
                enemy.speed =  round(enemy.speed,1)
            elif player == b:
                enemy.defense *= 2
                enemy.defense = round(enemy.defense,2)
            elif player == fighter:
                enemy.defense *=1.4
                enemy.defense=round(enemy.defense,2)
                enemy.speed*=1.8
                enemy.speed=round(enemy.speed,2)
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



goblin = Enemies("Goblin","a little green thing;embarrising if you die to it",0,0.4,0.8,100)   
troll = Enemies("Troll","a slightly bigger thing;would be less embarrisiing", 200, 2, 1, 0.05)
giant = Enemies("Giant", "this is a big boy",1000, 10,1,0)
wolf = Enemies("Wolf","...its a wolf",75,0.5,0.5,100)
ogre = Enemies("ogre","this is a very very very big thing",210,1.9,1.2,0.1)
a_british_person =Enemies("a british person","horrible teeth",15,0.8,0.1,90)
a_french_person =Enemies("A french man","dont let it near you government",20,0.9,0.1,100)
slime = Enemies("slime","sliiiiime",10,5,0.1,100)
Dragon = Enemies("dragon","breathes fire and stuff",250,0.2,0.8,90)
Enemies.enemies_list=[goblin,troll,giant,wolf,ogre,a_british_person,a_french_person,slime,Dragon]

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
                    Player.choose_skiil()


                elif enemy.health <=0:
                    print("youve defeated the enemy,move on")
                    print(f"you have gained {coins_recieved} coins")
                    print(f"your balance is now {player.money+coins_recieved}")
                    break
            if player.health <=0:
                print("youve died")

Floors.encounter(goblin,archer,3)
