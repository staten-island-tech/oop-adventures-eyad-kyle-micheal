<<<<<<< HEAD
=======
coins = 100
>>>>>>> 29ab7de321646d27886feaf3186dd8406296a66d
class mooney:
    def __init__(self, name, amount):
        self.amount = amount
        self.name = name
<<<<<<< HEAD
    def buy(x,item):
     if begin in a:
            a.remove(str(begin))
            player.append(str(begin))
            coins = x -item.amount
            print(coins)
            print(a)
            print(player)
Health_Potion = mooney("Health Potion", 10)
Flimsy_Wooden_Sword = mooney("Flimsy Wooden Sword", 40)
Flimsy_Steel_Sword = mooney("Flimsy Steel Sword", 60)

a = [Health_Potion.name, Flimsy_Wooden_Sword.name]
player = []
begin = input("buy item")
mooney.buy(100,Health_Potion)
=======
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
>>>>>>> 29ab7de321646d27886feaf3186dd8406296a66d
