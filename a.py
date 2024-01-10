class mooney:
    def __init__(self, name, amount):
        self.amount = amount
        self.name = name

    def buy(x,item,item2,item3):
        if begin in shop_invo:
            shop_invo.remove(str(begin))
            player.append(str(begin))
            coins = x -item.amount
            print(coins)
            print(shop_invo)
            print(player)
        else:
            print("no")
    
Health_Potion = mooney("Health Potion", 10)
Flimsy_Wooden_Sword = mooney("Flimsy Wooden Sword", 40)
Flimsy_Steel_Sword = mooney("Flimsy Steel Sword", 60)

shop_invo = [Health_Potion.name, Flimsy_Wooden_Sword.name, Flimsy_Steel_Sword.name]
def silly():
    if not shop_invo:
        print("you left")
        exit()
player = []
begin = input("buy item: ")
mooney.buy(100,Health_Potion,Flimsy_Wooden_Sword,Flimsy_Steel_Sword)
