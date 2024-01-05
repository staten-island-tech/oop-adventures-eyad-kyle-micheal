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
def no_money(coins):
        if coins == 0:
            print("You ran out of money")
            print("You left the shop...")
            exit()
def money_check(coins):
    if coins == 0:
        print("You ran out of money")
        print("You left the shop...")
        exit()
def user_warning_1(coins):
    if coins < 0:
        print("You do not have enough money to afford this")
        coins+=Health_Potion.amount
        sell(coins)

def user_warning_2(coins):
    if coins < 0:
        print("You do not have enough money to afford this")
        coins+=Flimsy_Wooden_Sword.amount
        sell(coins)

def user_warning_3(coins):
    if coins < 0:
        print("You do not have enough money to afford this")
        coins+=Flimsy_Steel_Sword.amount
        sell(coins)

def shop_inventory_check(coins):
    print("Items for sale:")
    if "Health Potion" in shop_inventory:
        print(f"{Health_Potion.name}: {Health_Potion.amount}")
    if "Flimsy Wooden Sword" in shop_inventory:
        print(f"{Flimsy_Wooden_Sword.name}: {Flimsy_Wooden_Sword.amount}")
    if "Flimsy Steel Sword" in shop_inventory:
        print(f"{Flimsy_Steel_Sword.name}: {Flimsy_Steel_Sword.amount}")
def shop_checker():
    if not shop_inventory:
        print("There is nothing to buy...")
        exit()
def sell(coins):
    print(f"This is the amount of money you have: {coins}")
    shop_inventory_check(coins)
    user_purchase = input("What would you like to buy?(Type Exit if you want to leave.): ")
    if user_purchase == "Health Potion":
        coins-=Health_Potion.amount
        user_warning_1(coins)
        print(f"You have purchased a {Health_Potion.name}")
        shop_inventory.remove("Health Potion")
        inventory.append("Health Potion")
        print(f"This is your inventory: {inventory}")
        money_check(coins)
        no_money(coins)
        sell(coins)
    if user_purchase == "Flimsy Wooden Sword":
        coins-=Flimsy_Wooden_Sword.amount
        user_warning_2(coins)
        print(f"You have purchased a {Flimsy_Wooden_Sword.name}")
        shop_inventory.remove("Flimsy Wooden Sword")
        inventory.append("Flimsy Wooden Sword")
        print(f"This is your inventory: {inventory}")
        money_check(coins)
        no_money(coins)
        sell(coins)
    if user_purchase == "Flimsy Steel Sword":
        coins-=Flimsy_Steel_Sword.amount
        user_warning_3(coins)
        print(f"You have purhcased a {Flimsy_Steel_Sword.name}")
        shop_inventory.remove("Flimsy Steel Sword")
        inventory.append("Flimsy Steel Sword")
        print(f"This is your inventory: {inventory}")
        money_check(coins)
        no_money(coins)
        sell(coins)
    if user_purchase == "Exit":
        print("You left the shop...")
        exit()
    else:
        print("Incorrect Input, Item is not in shop")
        sell(coins)
sell(coins)

#for importing:
#from awawawawa import mooney,money_check,sell,no_money,user_warning_1,user_warning_2,user_warning_3,shop_inventory_check
#sell()