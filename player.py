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
    def __str__(self):
        return (f'{self.name},Health:{self.health},melee_attack:{self.melee_attack},ranged_attack:{self.ranged_attack},speed:{self.speed},intelligense:{self.intelligence},magic talent:{self.magic_talent},money:{self.money}')
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
    def __init__(self,name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money,fighting_skills):
        super().__init__(name,health,melee_attack,ranged_attack,speed,intelligence,magic_talent,money)
        self.fighting_skills = fighting_skills
    def __str__(self):
        return super().__str__() + f",fighting skill {self.fighting_skills}"
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

