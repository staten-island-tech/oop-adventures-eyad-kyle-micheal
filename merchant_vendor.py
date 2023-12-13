coins = 100
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

shop_inventory = ["Health Potion", "Flimsy Wooden Sword", "Flimsy Steel Sword"]
inventory = []
class mooney():
    def __init__(self, name, amount):
        self.amount = amount
        self.name = name
Health_Potion = mooney("Health Potion", 10)
Flimsy_Wooden_Sword = mooney("Flimsy Wooden Sword", 40)
Flimsy_Steel_Sword = mooney("Flimsy Steel Sword", 60)
i=str(Health_Potion.name+Health_Potion.amount)
stage_1 = 1
def sell_1(coins):
    print("Items for sale:")
    if "Health Potion" in shop_inventory:
        print(Health_Potion.name)
        print(Health_Potion.amount)
        print(i)
    if "Flimsy Wooden Sword" in shop_inventory:
        print(Flimsy_Wooden_Sword.name)
        print(Flimsy_Wooden_Sword.amount)
    if "Flimsy Steel Sword" in shop_inventory:
        print(Flimsy_Steel_Sword.name)
        print(Flimsy_Steel_Sword.amount)
    while stage_1 == 1:
        print("This is the amount of money you have:")
        print(coins)
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
            print("You have purchased a Heath Potion")
            shop_inventory.remove("Health Potion")
            inventory.append("Health Potion")
            print("This is your inventory:")
            print(inventory)
            if coins == 0:
                print("You ran out of money")
                print("You left the shop...")
                exit()
            sell_1(coins)
        if user_purchase == "Flimsy Wooden Sword":
            coins-=Flimsy_Wooden_Sword.amount
            user_warning_2(coins)
            print("You have purchased a Flimsy Wooden Sword")
            shop_inventory.remove("Flimsy Wooden Sword")
            inventory.append("Flimsy Wooden Sword")
            print("This is your inventory:")
            print(inventory)
            if coins == 0:
                print("You ran out of money")
                print("You left the shop...")
                exit()
            sell_1(coins)
        if user_purchase == "Flimsy Steel Sword":
            coins-=Flimsy_Steel_Sword.amount
            user_warning_3(coins)
            print("You have purhcased a Flimsy Steel Sword")
            shop_inventory.remove("Flimsy Steel Sword")
            inventory.append("Flimsy Steel Sword")
            print("This is your inventory:")
            print(inventory)
            if coins == 0:
                print("You ran out of money")
                print("You left the shop...")
                exit()
            sell_1(coins)
        else:
            print("Incorrect Input, Item is not in shop")
            sell_1(coins)
sell_1(coins)

