from enemies import Enemies
class Player():
    def __init__(self,name,health,melee_attack,ranged_attack,defense,speed,intelligence,magic_talent):
        self.name = name
        self.health = health
        self.melee_attack = melee_attack
        self.ranged_attack =ranged_attack
        self.defense = defense
        self.speed = speed
        self.intelligence = intelligence
        self.magic_talent = magic_talent
        
Archer =Player("Archer",90,  .35,  1.3,  0.8,  95,  1.1,  15)
print(Archer.__dict__)
Warrior = Player("Warrior",150, 1.35,  .20,   1.1,   50,  .60,  5)
print(Warrior.__dict__)
Mage = Player("Mage",100, .05, 2, .9, 50, 1, 100)
print(Mage.__dict__)
Fighter = Player("Fighter",130, 1.3, 1,0.7 ,120, 1.05, 15)
print(Fighter.__dict__)
Berserker = Player("Berserker",50,  2.5,  0,  1,  200,  1,  1)
print(Berserker.__dict__)
Assasin = Player("Assasin",80, 1.2,0.8, 0.35, 240, 1.25,  20 )
print(Assasin.__dict__)




