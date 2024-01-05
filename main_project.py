from working import Player,Archer,Assasin,Warrior,Berserker,Wizard,Fighter,Enemies,Floors
from SBox import Active,PasCommon,archer_skill,warrior_skill,b_skill,assasin_skill,fighter_skill
from merchant_vendor import mooney

def tutorial():
    print("Helo adventurer! You have made it to the tower of chellenges")
shop = ["Helaht","Damage"]
inventory=[]
def printint():
    for i, it in enumerate(shop):
        print(f'{i+1},{it}')

def adding():
    printint()
    y = int(input(""))
    if 2>=y<=1:
        inventory.append(shop[y-1])
adding()
print(inventory[0])