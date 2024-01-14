from everything import *
from SBox import *
from shop import Shop

def tutorial_tiny():
    print("Helo adventurer! You have made it to the tower of chellenges Before doing anything else, you will have to learn the basics. First, you'll have to choose your class")
Player.print_classes()
chosen = Player.better_choose_class()
Enemies.donig_adapting(chosen)
tutorial_tiny()

def actual():
    print(f"""Great! You've sucessfullay chosen a class ! Here aare your stats \n {chosen.__dict__} """)
    print(f'''The "attack" stat is a multiplier as to how much damage you will do. For example, since you have an attak stat of {chosen.attack} you will deal {chosen.attack} times damage on you attacks. 
          That being said, these attacks will also go through the enemies defense stat,meaning that if you do an attack of 10 damage, you will actually do an attack of 10*{chosen.attack} * enenmy defense.
          You also have a "mana" which is similar to you health. You consume mana when attacking. If your mana reaches 0, you will die; similarly to if your health reaches 0. ''')
    print(f"\nNow that you've chosen a class, you should learn how to fight. Here's a goblin to start with. Be carful, you only have one life so if you die you'll have to restart.")
    Player.encounter(goblin,chosen,15)
    print(f"Good job! If you noticed, you gained some exp and coins there. Coins can be used in the shop to buy better items. Be careful what you buy however, because you cna only buy one item perfloor. In regards to exp, you recieve exp after killing an enemy. If you get 100 exp, you'll level up and get extra stats.")
    print(f"Before we go to the shop, lets fight another enemy; this time a slime")
    Player.encounter(slime,chosen,10)
    print(f"Nice! Lets go to the shop now")
actual()
<<<<<<< Updated upstream
int
=======
def shop_tutorial():
    Shop.prices=[25]
    Shop.displayed_shop_inventory=["Health potion: Heals 20 hp"]
    Shop.buying(chosen)



>>>>>>> Stashed changes

