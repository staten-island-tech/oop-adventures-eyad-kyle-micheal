coins = 100
class mooney:
    def __init__(self, name, amount):
        self.amount = amount
        self.name = name
Health_Potion = mooney("Health Potion", 10)
Flimsy_Wooden_Sword = mooney("Flimsy Wooden Sword", 40)
Flimsy_Steel_Sword = mooney("Flimsy Steel Sword", 60)
shop = [Health_Potion.name, Flimsy_Wooden_Sword.name, Flimsy_Steel_Sword.name]
def buy():
    thing=input("buy")
    if thing in shop:
        shop.remove(str(thing))
        print(str(thing.amount))
        print(shop)
buy()