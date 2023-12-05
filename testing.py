from enemies import Enemies,Whalen
from player import Player,Archer,Assasin,Warrior,Berserker,Fighter,Wizard
goblin = Enemies("Goblin","a little green thing;embarrising if you die to it",100,0.4,0.8,100)   
troll = Enemies("Troll","a slightly bigger thing;would be less embarrisiing", 200, 2, 1, 0.05)
giant = Enemies("Giant", "this is a big boy",1000, 10,1,0)
wolf = Enemies("Wolf","...its a wolf",75,0.5,0.5,100)
ogre = Enemies("ogre","this is a very very very big thing",210,1.9,1.2,0.1)
whalen = Whalen("Whalen","this is the final boss; you are most definity going to die; you will also fail his class",2000,300,500,100,9999999999999)
a_british_person =Enemies("a british person","horrible teeth",15,0.8,0.1,90)
a_french_person =Enemies("A french man","dont let it near you government",20,0.9,0.1,100)
slime = Enemies("slime","sliiiiime",10,5,0.1,100)
Dragon = Enemies("dragon","breathes fire and stuff",250,0.2,0.8,90)

class TestAttack():
    def __init__(self,name,base_damage):
        self.name = name
        self.base_damage = base_damage
    def calculate(self,enemy): 
        return self.base_damage-(self.base_damage-(self.base_damage*enemy.defense))
quick_attack = TestAttack("quick_attack",120)

archer = Archer("Archer",90,  .35,  1.3,  0.8,  95,  1.1,  15)
assasin=Assasin("assasin", 100, 90, 90, 150, 100, 25, 0,1000)
warrior=Warrior("warrior",150,125,75,100,100,75,0,1000)
b = Berserker("Berserker",100,150,30,75,100,15,0,1000000)
fighter = Fighter("fighter",150,100,1,175,100,10,0,100000)
wizard = Wizard("Wizard",150,10,100,100,150,300,0,10000000)
classes=["archer","assasin","warrior","berserker","fighter"]
print(whalen.__dict__)
def choose_your_class():
    choose = input("what:")
    if choose.lower() == ("archer"):
        return archer
    elif choose.lower() == ("warrior"):
        return warrior 
    elif choose.lower() == ("assasin"):
        return assasin
    elif choose.lower() == ("b"):
        return b
    elif choose.lower() == ("fighter"):
        return fighter
    elif choose.lower() == ("wizard"):
        return wizard
    else:
        print("invalid choice.try again")
        chose = input('what: ')
        chose = choose

chosen = choose_your_class()


def adapting():
    global goblin
    if chosen == archer:
        goblin = Enemies("Goblin","a little green thing;embarrising if you die to it",99,0.4,0.8,99) 
        
    elif chosen == warrior:
        goblin = Enemies("Goblin","a little green thing;embarrising if you die to it",98,0.4,0.8,98)



if chosen:
    print("Here is your class:")
    print(chosen.__dict__)



def encounter(enemy,player,coins):
    while player.health >0:
        if enemy.health > 0:
            x=input("what attack:")
            if x == ("quick attack"):
                damage = quick_attack.calculate(enemy)
                enemy.health = max(0,enemy.health - damage)
                print(enemy.__dict__)
                player.health = max(0,player.health - 10)
                print(player.__dict__)
            else:
                print(input("sorry thats not an attack try again "))
        elif enemy.health <=0:
            print("youve defeated the enemy,move on")
            print(f"you have gained {coins} coins")
            break
    if player.health <=0:
        print("youve died")

