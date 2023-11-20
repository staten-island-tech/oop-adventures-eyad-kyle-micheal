from enemies import Enemies
from player import Player
goblin = Enemies("Goblin",100,0.4,0.8,100)    
class TestAttack():
    def __init__(self,name,base_damage):
        self.name = name
        self.base_damage = base_damage
quick_attack = TestAttack("quick_attack",120)
coins = 7
def attack():
    while goblin.health > 0:
        x=input("what attack:")
        if x == ("quick attack"):
            goblin.health = max(0,goblin.health -(quick_attack.base_damage-(quick_attack.base_damage*goblin.defense)))
            print(goblin.__dict__)
        else:
            print(input("sorry thats not an attack try again"))
    if goblin.health ==0 or goblin.health <0:
        print("youve defeated the enemy,move on")
        print(f"you have gained {coins} coins")
attack()
