from enemies import Enemies
from player import Player
goblin = Enemies("Goblin",100,0.4,0.8,100)    
archer = ("Archer",90,  .35,  1.3,  0.8,  95,  1.1,  15) 
archer = ("archer")
class TestAttack():
    def __init__(self,name,base_damage):
        self.name = name
        self.base_damage = base_damage
quick_attack = TestAttack("quick_attack",120)
coins = 7
classes = [archer]
def class_choice():
    choose=input("what class are you?:")
    if choose in classes:
        global selected_class
        selected_class = choose
class_choice()
print(selected_class)




def attack(enemy,player):
    while enemy.health > 0:
        x=input("what attack:")
        if x == ("quick attack"):
            enemy.health = max(0,enemy.health -(quick_attack.base_damage-(quick_attack.base_damage*enemy.defense)))
            print(enemy.__dict__)
        else:
            print(input("sorry thats not an attack try again"))
    if enemy.health ==0 or enemy.health <0:
        print("youve defeated the enemy,move on")
        print(f"you have gained {coins} coins")

attack(goblin,archer)