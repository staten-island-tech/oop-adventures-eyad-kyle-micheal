coins = 20
class mooney:
    def __init__(self, name, amount):
        self.amount = amount
        self.name = name

    def buy(coins,item,item2,item3):
        mooney.silly_funny(coins,Health_Potion,Flimsy_Wooden_Sword,Flimsy_Steel_Sword)
        mooney.silly(coins,Health_Potion,Flimsy_Wooden_Sword,Flimsy_Steel_Sword)
        print(shop_invo)
        begin = input("buy item: ")
        if begin in shop_invo:
            shop_invo.remove(begin)
            player.append(begin)
            coins-=10
            print(coins)
            print(player)
            mooney.buy(coins,Health_Potion,Flimsy_Wooden_Sword,Flimsy_Steel_Sword)
        elif begin == "exit":
            print("bye")
        else:
            print("no")
            mooney.buy(coins,Health_Potion,Flimsy_Wooden_Sword,Flimsy_Steel_Sword)
            
    def silly(coins,item,item2,item3):
        if not shop_invo:
            print("you left")
            exit()

    def silly_funny(coins,item,item2,item3):
        if coins<0:
            print("not enough money")
            coins+=10
            print(coins)
            mooney.buy(coins,Health_Potion,Flimsy_Wooden_Sword,Flimsy_Steel_Sword)
Health_Potion = mooney("Health Potion", 10)
Flimsy_Wooden_Sword = mooney("Flimsy Wooden Sword", 40)
Flimsy_Steel_Sword = mooney("Flimsy Steel Sword", 60)

shop_invo = [Health_Potion.name, Flimsy_Wooden_Sword.name, Flimsy_Steel_Sword.name]
funny_list = [Health_Potion]
player = []

mooney.buy(coins,Health_Potion,Flimsy_Wooden_Sword,Flimsy_Steel_Sword)
