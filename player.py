
class Player():
    classes_choice=[]
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
        return (f'{self.name},Health:{self.health},melee_attack:{self.melee_attack},ranged_attack:{self.ranged_attack},speed:{self.speed},intelligense:{self.intelligence},magic talent:{self.magic_talent},money:{self.money}')
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
                    return Player.classes_choice[choose-1]
                else:
                    print("It seems this wasn't one of the choices.Please enter a valid number.")
            except ValueError:
                print("Please enter an integer")
            
chosen = Player.better_choose_class
class Archer(Player):
    def __init__(self,name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money,suuper):
        super().__init__(name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money) 
        self.suuper = suuper
    def __str__(self):
        return super().__str__() + f',Ranged:{self.suuper}'
class Assasin(Player):
    def __init__(self,name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money,stealth ):
        super().__init__(name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money)
        self.stealth = stealth
    def __str__(self):
        return super().__str__() + f",Stealth {self.stealth}"
class Warrior(Player):
    def __init__(self,name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money,honor):
        super().__init__(name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money)
        self.honor = honor
    def __str__(self):
        return super().__str__() + f",honor {self.honor}"
class Berserker(Player):
    def __init__(self,name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money,rage):
        super().__init__(name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money)
        self.rage = rage
    def __str__(self):
        return super().__str__() + f",rage {self.rage}"
class Fighter(Player):
    def __init__(self,name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money,skillss):
        super().__init__(name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money)
        self.skilss = skillss
    def __str__(self):
        return super().__str__() + f",fighting skill {self.skilss}"
class Wizard(Player):
    def __init__(self,name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money,magic):
        super().__init__(name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money)
        self.magic=magic
    def __str__(self):
        return super().__str__() + f",mastery of magic {self.magic}"
class SecretClass(Player):
    def __init__(self,name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money,secrets):
        super().__init__(name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money)
        self.secrets = secrets
    def __str__(self):
        return super().__str__() + f",Stealth {self.secrets}"
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
Player.print_classes()
chosen_thing = chosen()
chosen_thing
print(chosen_thing.__dict__)