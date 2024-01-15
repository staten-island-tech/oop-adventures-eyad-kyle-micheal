


class Shop():
    inventory=["put variables here;eg actual values"]
    displayed_shop_inventory = ["Healht potion"]
    player_inventory=["put players' values here"]
    display_player = ["put player "]
    prices=[]

    def __init__(self,price):
        self.price = price
    def buying():
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
                    item = Shop.prices[chosen_item-1]
                    if player.money>= item:
                        print(f'You have purchased {Shop.displayed_shop_inventory[chosen_item-1]}')
                        Shop.displayed_shop_inventory.pop(chosen_item-1)
                        Shop.player_inventory()
                    else: 
                        print(f"You don't have enough money for this.")
                
            except ValueError:
                print("no")
        else:
             print(f'There are no more items in the shop at htis time. Come back next floor!')
Shop.buying()

        

            



