equiped_armor=None
equiped_weapon=None

class Shop():

    displayed_shop_inventory = []
    default_inventory =[]
    prices=[]

    def __init__(self,description,price):
        self.description = description
        self.price = price
<<<<<<< Updated upstream
    def buying():
=======
        
        


    def __str__(self):
         return f'Description:{self.description},Price:{self.price}'
    def print_inventory():
        for i,inevntory in enumerate(Shop.displayed_shop_inventory):
             print(f'{i+1}.{inevntory}\n')

    
    def buying(player):
>>>>>>> Stashed changes
        while Shop.displayed_shop_inventory: 
            global equiped_weapon
            global equiped_armor
            if player.health >0 or player.mana > 0 :
                

                Shop.print_inventory()
                x = input("Hello! What item would you like to purchase:(type the correspodning number; type exit if you'd like to exit the shop.)")
                try:  
                    if x.lower() == 'exit':
                         print(f'ok bye')
                         break
                    chosen_item=int(x)    
                    if 1<=chosen_item<=len(Shop.displayed_shop_inventory):
                        item_price = Shop.default_inventory[chosen_item-1].price
                        item = Shop.default_inventory[chosen_item-1]
                        if player.money>= item_price:
                            print(f'You have purchased {Shop.displayed_shop_inventory[chosen_item-1]}')
                            Shop.displayed_shop_inventory.pop(chosen_item-1)
                            player.money-=item_price
                            Shop.armour_check(item,player)
                            Shop.weapon_check(item,player)
                            Shop.recoil_check(player)
                            player.health=round(player.health)
                            player.defense=round(player.defense,1)
                            player.attack=round(player.attack,1)
                            print(player.__dict__)
                        else: 
                            print(f"You don't have enough money for this.")
                    else:
                        print("Please print a valid integer")

                except ValueError:
                    print("Please type an integer")
            else:
                break
        else:
<<<<<<< Updated upstream
             print(f'There are no more items in the shop at htis time. Come back next floor!')
Shop.buying()

=======
            print(f'There are no more items in the shop at htis time. Come back next floor!')
    def recoil_check(player):
        global equiped_weapon
        global equiped_armor
        if equiped_armor == recoil_armor:
            player.health+=recoil_armor.health_increase
            player.defense+=recoil_armor.defense_increase
            player.attack-=0.9
        if equiped_weapon == recoil_ssword:
             player.health-=80
             player.defense-=0.4
             player.attack+=recoil_ssword.buff_increase  
        
    def armour_check(item,player):
        global equiped_armor
        if isinstance(item,Armor):
            player.health+=item.health_increase
            player.defense+=item.defense_increase
            
            if equiped_armor != None:
                player.health-= equiped_armor.health_increase
                player.defense-=equiped_armor.defense_increase
            player.health = round(player.health)
            equiped_armor = item
    def weapon_check(item,player):
         global equiped_weapon
         if isinstance(item,Sword):
            player.attack+=item.buff_increase
            if equiped_weapon != None:
                player.attack-=equiped_weapon.buff_increase
            player.attack=round(player.attack,1)
            equiped_weapon= item


class Sword(Shop):

    def __init__(self,description,price,buff_increase):
          super().__init__(description,price)
          self.buff_increase = buff_increase

        
                
class Armor(Shop):
    def __init__(self,description,price,health_increase,defense_increase):
        super().__init__(description,price)
        self.health_increase = health_increase
        self.defense_increase = defense_increase 



#weapons
flimsy_sword=Sword("Flimsy Sword: Gives 0.1 atatck for 20 coins",20,0.1)
reinforced_sword=Sword("Reinforced Sword:Gives .15 attack for 20 coins",20,.15)
sturdy_sword=Sword("Sturdy Sword: Gives an extra 0.2 attack for 30 coins",30,0.2)
crystal_sword=Sword("Crystal sword: gives an extra 0.5 attack for 70 coins",70,0.5)
recoil_ssword=Sword("Recoil Sword: Gives an extra 0.8 attack but lowers hp by 40 and defense by 0.4 for 70 coins",70,0.8)
for_me=Sword(":::",0,100000)
                



#armor
flimsy_armor=Armor("Flimsy_armor: Gives an extra 10 hp for 10 coins",10,10,0)
sturdy_chestplate=Armor("Sturdy chestplate:Gives an extra 40 hp and 0.3 defense for 60 coins",60,40,0.3)
chainmail=Armor("Chainmail:Gives an extra 15 hp and 0.1 attack for 20 coins",20,15,0.1)
crystal_armor=Armor("Crystal armos:gives an extra 50 hp and 0.4 defense for 80 coins",80,50,0.4)
recoil_armor= Armor("Recoil Armor: Gives an extra 75 hp and 0.5 defense and lowers attack by 0.9 for 80 coins",80,75,0.5)
for_me=Armor("wgu",0,10000,10000)

Shop.default_inventory=[flimsy_sword,reinforced_sword,sturdy_sword,crystal_sword,recoil_ssword,flimsy_armor,sturdy_chestplate,chainmail,crystal_armor,recoil_armor]
Shop.displayed_shop_inventory=[flimsy_sword.description,reinforced_sword.description,sturdy_sword.description,crystal_sword.description,recoil_ssword.description,flimsy_armor.description,sturdy_chestplate.description,chainmail.description,crystal_armor.description,recoil_armor.description]





         
        
>>>>>>> Stashed changes
        

            



