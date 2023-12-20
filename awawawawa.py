#import random
#random_thing = random.randint(1,2)
#if random_thing == 1:
 #   print("hi")
#elif random_thing == 2:
#   print("bye")

coins = 100
class mooney:
    def __init__(self, name, amount):
        self.amount = amount
        self.name = name
Health_Potion = mooney("Health Potion", 10)
Flimsy_Wooden_Sword = mooney("Flimsy Wooden Sword", 40)
Flimsy_Steel_Sword = mooney("Flimsy Steel Sword", 60)

shop_inventory = ["Health Potion", "Flimsy Wooden Sword", "Flimsy Steel Sword"]
inventory = []

#class merchant():
   # def __init__(self, name, products):
   # coins = 100
def user_warning_1(coins):
    if coins < 0:
        print("You do not have enough money to afford this")
        coins+=Health_Potion.amount
        sell_1(coins)

def user_warning_2(coins):
    if coins < 0:
        print("You do not have enough money to afford this")
        coins+=Flimsy_Wooden_Sword.amount
        sell_1(coins)

def user_warning_3(coins):
    if coins < 0:
        print("You do not have enough money to afford this")
        coins+=Flimsy_Steel_Sword.amount
        sell_1(coins)

def sell_1(coins):
    print("Items for sale:")
    if "Health Potion" in shop_inventory:
        print(f"{Health_Potion.name}: {Health_Potion.amount}")
    if "Flimsy Wooden Sword" in shop_inventory:
        print(f"{Flimsy_Wooden_Sword.name}: {Flimsy_Wooden_Sword.amount}")
    if "Flimsy Steel Sword" in shop_inventory:
        print(f"{Flimsy_Steel_Sword.name}: {Flimsy_Steel_Sword.amount}")
    while 1:
        print(f"This is the amount of money you have: {coins}")
        user_purchase = input("What would you like to buy?(Type Exit if you want to leave.): ")
        if not shop_inventory:
            print("There is nothing to buy")
            exit()
        if user_purchase == "Exit":
            print("You left the shop...")
            exit()
        if user_purchase == "Health Potion":
            coins-=Health_Potion.amount
            user_warning_1(coins)
            print(f"You have purchased a {Health_Potion.name}")
            shop_inventory.remove("Health Potion")
            inventory.append("Health Potion")
            print(f"This is your inventory: {inventory}")
            if coins == 0:
                print("You ran out of money")
                print("You left the shop...")
                exit()
            sell_1(coins)
        if user_purchase == "Flimsy Wooden Sword":
            coins-=Flimsy_Wooden_Sword.amount
            user_warning_2(coins)
            print(f"You have purchased a {Flimsy_Wooden_Sword.name}")
            shop_inventory.remove("Flimsy Wooden Sword")
            inventory.append("Flimsy Wooden Sword")
            print(f"This is your inventory: {inventory}")
            if coins == 0:
                print("You ran out of money")
                print("You left the shop...")
                exit()
            sell_1(coins)
        if user_purchase == "Flimsy Steel Sword":
            coins-=Flimsy_Steel_Sword.amount
            user_warning_3(coins)
            print(f"You have purhcased a {Flimsy_Steel_Sword.name}")
            shop_inventory.remove("Flimsy Steel Sword")
            inventory.append("Flimsy Steel Sword")
            print(f"This is your inventory: {inventory}")
            if coins == 0:
                print("You ran out of money")
                print("You left the shop...")
                exit()
            sell_1(coins)
        else:
            print("Incorrect Input, Item is not in shop")
            sell_1(coins)
    return(sell_1)