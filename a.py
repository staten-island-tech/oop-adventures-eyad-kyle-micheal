#code below works and can be imported
coins = 100
class mooney:
    def __init__(self, name, amount):
        self.amount = amount
        self.name = name

    def buy(coins,item,item2,item3):
        mooney.silly(coins,Health_Potion,Flimsy_Wooden_Sword,Flimsy_Steel_Sword)
        print("for sale: ")
        for shop_item in secret:
            print(f"{shop_item.name}: {shop_item.amount}")
        print(f"this is the amount of money you have: {coins}")
        begin = input("buy item (type exit if you want to leave): ")
        if begin in shop_invo:
            selected_item = next(item_obj for item_obj in [item, item2, item3] if item_obj.name == begin)
            if coins >= selected_item.amount:
                shop_invo.remove(begin)
                player.append(begin)
                secret.remove(selected_item)
                coins-=selected_item.amount
                print(f"this is your inventory: {player}")
            mooney.buy(coins,Health_Potion,Flimsy_Wooden_Sword,Flimsy_Steel_Sword)
        elif begin == "exit":
            print("you left the shop...")
        else:
            print("no")
            mooney.buy(coins,Health_Potion,Flimsy_Wooden_Sword,Flimsy_Steel_Sword)
        
    def silly(coins,item,item2,item3):
        if not shop_invo:
            print("you left")
            exit()
Health_Potion = mooney("Health Potion", 10)
Flimsy_Wooden_Sword = mooney("Flimsy Wooden Sword", 40)
Flimsy_Steel_Sword = mooney("Flimsy Steel Sword", 70)

shop_invo = [Health_Potion.name, Flimsy_Wooden_Sword.name, Flimsy_Steel_Sword.name]
secret = [Health_Potion, Flimsy_Wooden_Sword, Flimsy_Steel_Sword]
player = []

mooney.buy(coins,Health_Potion,Flimsy_Wooden_Sword,Flimsy_Steel_Sword)
