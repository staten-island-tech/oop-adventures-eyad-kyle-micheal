from enemies import Enemies
class Player():
    def __init__(self,health,melee_attack,ranged_attack,defense,speed,intelligence,magic_talent):
        self.health = health
        self.melee_attack = melee_attack
        self.ranged_attack =ranged_attack
        self.defense = defense
        self.speed = speed
        self.intelligence = intelligence
        self.magic_talent = magic_talent
        
Archer =(90, .35, 1.3, 0.8, 95, 1.1,15)
Warrior = (150, 1.35,.20, 1.1, 50,.60,5)
Mage = (100,.05,2,.9,.5,1,2,100)

goblin =Enemies ("Goblin",100,0.4,0.8,100)    

x = input("You've encountered an enemy!What would you like to do ")
player_encounter = True 
if player_encounter == True:
    print(x)
    if x == ("attack"):
        print("the attack was successful!" + str(goblin.__dict__)) 

