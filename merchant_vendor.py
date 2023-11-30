coins = 100

shop_inventory = ["Health Potion", "Flimsy Wooden Sword"]
inventory = []
class Merchant:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

stage_1 = 1
stage_2 = 2
def sell_2():
    while stage_2 == 2:
        redo = input("Do you want to buy anything else? (Yes or No): ")
    if redo == "Yes":
        sell_1()

def sell_1():
    print(shop_inventory)
    while stage_1 == 1:
        user_purchase = input("What would you like to buy?: ")
        if user_purchase == "Health Potion":
            print("You have purchased a Heath Potion")
            shop_inventory.remove("Health Potion")
            inventory.append("Health Potion")
            print(inventory)
            sell_2()
        else:
            print("Incorrect Input, Please try again")
sell_1()




health_potion = Merchant("Health Potion", 10)

