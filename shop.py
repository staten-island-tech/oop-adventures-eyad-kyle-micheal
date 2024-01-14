


class Shop():
    inventory=[]
    displayed_shop_inventory = []
    player_inventory=[]
    prices=[]

    def __init__(self,price):
        self.price = price
    def buying(player):
        while Shop.displayed_shop_inventory: 
            for i, items in enumerate(Shop.displayed_shop_inventory):
                        print(f'{i+1}.{items}\n')
            x = input("Hello! What item would you like to purchase:(type the correspodning number; type exit if you'd like to exit the shop.)")
            try:  
                if x.lower() == 'exit':
                     print(f'ok bye')
                     break
                chosen_item=int(x)    
                if 1<=chosen_item<=len(Shop.displayed_shop_inventory):
                    item = Shop.prices[x-1]
                    if player.money>= item:
                        print(f'You have purchased {Shop.displayed_shop_inventory[x-1]}')
                        Shop.displayed_shop_inventory.pop(x-1)
                    else: 
                        print(f"You don't have enough money for this.")
                
            except ValueError:
                print("no")
        else:
             print(f'There are no more items in the shop at htis time. Come back next floor!')

            


class TestPlayer():
    def __init__(self,money):
         self.money = money
test=TestPlayer(0)
def testing():
    Shop.displayed_shop_inventory=['Health Potion']
    Shop.buying(test)
testing()
