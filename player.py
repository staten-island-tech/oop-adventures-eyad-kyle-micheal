from enemies import Enemies
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
    def __init__(self):
        super().__init__("Archer",90,  .35,  1.3,  0.8,  95,  1.1,  15) 
class Assasin(Player):
    def __init__(self,stealth ):
        super().__init__("assasin", 100, 90, 90, 150, 100, 25, 0)
        self.stealth = stealth
assasin = Assasin
print(assasin.__dict__)
print()
