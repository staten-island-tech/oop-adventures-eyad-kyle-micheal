from enemies import Enemies
from player import Player,Archer,Assasin
goblin = Enemies("Goblin",100,0.4,0.8,100)    
archer = ("Archer",90,  .35,  1.3,  0.8,  95,  1.1,  15) 

class TestAttack():
    def __init__(self,name,base_damage):
        self.name = name
        self.base_damage = base_damage
    def calculate(self,enemy): 
        return self.base_damage-(self.base_damage*enemy.defense)
quick_attack = TestAttack("quick_attack",120)
coins = 7
archer = Archer("Archer",90,  .35,  1.3,  0.8,  95,  1.1,  15)
assasin=Assasin("assasin", 100, 90, 90, 150, 100, 25, 0,1000)

def choose_your_class():
    choose = input("what:")
    if choose == ("archer"):
        print(f"youre chosen class is {choose}")
        global chosen
        chosen=archer
        print(chosen.__dict__)
choose_your_class()
def attack(enemy,player):
    while player.health >0:
        while enemy.health > 0:
            x=input("what attack:")
            if x == ("quick attack"):
                damage = quick_attack.calculate(enemy)
                enemy.health = max(0,enemy.health - 0)
                print(enemy.__dict__)
                player.health = max(0,player.health - 10)
                print(chosen.__dict__)
            else:
                print(input("sorry thats not an attack try again "))
        if enemy.health <=0:
            print("youve defeated the enemy,move on")
            print(f"you have gained {coins} coins")
    if player.health <=0:
        print("youve died")
    
attack(goblin,chosen)
