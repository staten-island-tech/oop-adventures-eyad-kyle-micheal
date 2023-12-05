class Player():
    def __init__(self,name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money):
        self.name = name
        self.health = health
        self.melee_attack = melee_attack
        self.ranged_attack =ranged_attack
        self.speed = speed
        self.intelligence = intelligence
        self.magic_talent = magic_talent
        self.money = money
class Archer(Player):
    def __init__(self,name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money):
        super().__init__(name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money) 
class Assasin(Player):
    def __init__(self,name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money,stealth ):
        super().__init__(name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money)
        self.stealth = stealth
class Warrior(Player):
    def __init__(self,name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money,honor):
        super().__init__(name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money)
        self.honor = honor
class Berserker(Player):
    def __init__(self,name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money,rage):
        super().__init__(name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money)
        self.rage = rage
class Fighter(Player):
    def __init__(self,name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money,skillss):
        super().__init__(name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money)
        self.skilss = skillss
class Wizard(Player):
    def __init__(self,name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money,magic):
        super().__init__(name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money)
        self.magic=magic
class SecretClass(Player):
    def __init__(self,name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money,secrets):
        super().__init__(name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money)
        self.secrets = secrets

