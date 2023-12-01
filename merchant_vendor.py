def leave_shop():
    exit()

shop_inventory = ["Health Potion", "Flimsy Wooden Sword"]
inventory = []
class Merchant:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

stage_1 = 1
stage_2 = 2
def sell_2():
    if not shop_inventory:
        print("There is nothing to buy")
        leave_shop()
    while stage_2 == 2:
        print(shop_inventory)
        redo = input("Do you want to buy anything else? (Yes or No): ")
        if redo == "Yes":
            sell_1()
        if redo == "No":
            exit()

coins = 100

def sell_1():
    print(shop_inventory)
    while stage_1 == 1:
        user_purchase = input("What would you like to buy?: ")
        if user_purchase not in shop_inventory:
            print("Incorrect Input, Item is not in shop")
            sell_1()
        if user_purchase == "Health Potion":
            print("You have purchased a Heath Potion")
            shop_inventory.remove("Health Potion")
            inventory.append("Health Potion")
            print(coins)
            print(inventory)

            sell_2()
        if user_purchase == "Flimsy Wooden Sword":
            print("You have purchased a Flimsy Wooden Sword")
            shop_inventory.remove("Flimsy Wooden Sword")
            inventory.append("Flimsy Wooden Sword")
            print(coins)
            print(inventory)
            sell_2()
sell_1()



health_potion = Merchant("Health Potion", 10)
