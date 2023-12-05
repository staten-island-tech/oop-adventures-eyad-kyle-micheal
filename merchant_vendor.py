cost_1 = 10
cost_2 = 30
amount = 10

def user_warning(amount):
    if amount < 0:
        print("You do not have enough money to afford this")
        amount+=cost_2
        sell_1(amount)

def leave_shop():
    exit()

shop_inventory = ["Health Potion", "Flimsy Wooden Sword"]
inventory = []
class mooney():
    def __init__(self, amount):
        self.amount = amount

stage_1 = 1
stage_2 = 2
def sell_2(amount):
    if not shop_inventory:
        print("There is nothing to buy")
        leave_shop()
    while stage_2 == 2:
        print(shop_inventory)
        redo = input("Do you want to buy anything else? (Yes or No): ")
        if redo == "Yes":
            sell_1(amount)
        if redo == "No":
            exit()

def sell_1(amount):
    print(shop_inventory)
    while stage_1 == 1:
        user_purchase = input("What would you like to buy?: ")
        if user_purchase not in shop_inventory:
            print("Incorrect Input, Item is not in shop")
            sell_1(amount)
        if user_purchase == "Health Potion":
            amount-=cost_1
            user_warning(amount)
            print("You have purchased a Heath Potion")
            shop_inventory.remove("Health Potion")
            inventory.append("Health Potion")
            print(inventory)
            print(amount)
            if amount == 0:
                print("You ran out of money!")
                exit()
            sell_2(amount)
        if user_purchase == "Flimsy Wooden Sword":
            amount-=cost_2
            user_warning(amount)
        print("You have purchased a Flimsy Wooden Sword")
        print(inventory)
        print(amount)
        shop_inventory.remove("Flimsy Wooden Sword")
        inventory.append("Flimsy Wooden Sword")
        if amount == 0:
            print("You ran out of money")
            exit()
    sell_2(amount)
sell_1(amount)




