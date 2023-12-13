#cost_1 = 10
#cost_2 = 10
#cost_3 = 10
#amount = 20

#def user_warning_1(amount):
    #if amount < 0:
        #print("You do not have enough money to afford this")
        #amount+=cost_1
        #sell_1(amount)

#def user_warning_2(amount):
    #if amount < 0:
        #print("You do not have enough money to afford this")
        #amount+=cost_2
        #sell_1(amount)

#def user_warning_3(amount):
    #if amount < 0:
        #print("You do not have enough money to afford this")
        #amount+=cost_3
        #sell_1(amount)

#shop_inventory = ["Health Potion", "Flimsy Wooden Sword", "Flimsy Steel Sword"]
#inventory = []
#class mooney():
    #def __init__(self, amount):
        #self.amount = amount

#stage_1 = 1
#stage_2 = 2
#def sell_2(amount):
    #if not shop_inventory:
      #  print("There is nothing to buy")
     #   exit()
    #while stage_2 == 2:
      #  print(shop_inventory)
     #   redo = input("Do you want to buy anything else? (Yes or No): ")
    #    if redo == "Yes":
   #         sell_1(amount)
  #      if redo == "No":
 #           exit()
#
#def sell_1(amount):
  #  print(shop_inventory)
 #   while stage_1 == 1:
#        user_purchase = input("What would you like to buy?(Type exit if you want to leave.): ")
       # if not shop_inventory:
      #      print("There is nothing to buy")
     #       exit()
    #    if user_purchase == "Exit":
   #         print("You left the shop...")
  #          exit()
 #       if user_purchase == "Health Potion":
#            if amount == 0:
      #          print("You ran out of money")
     #           print(inventory)
    #            exit()
   #         amount-=cost_1
  #          user_warning_1(amount)
 #           print("You have purchased a Heath Potion")
#            shop_inventory.remove("Health Potion")
      #      inventory.append("Health Potion")
     #       print(inventory)
    #        print(amount)
   #         sell_2(amount)
  #      if user_purchase == "Flimsy Wooden Sword":
 #           if amount == 0:
#                print("You ran out of money")
     #           exit()
    #        amount-=cost_2
   #         user_warning_2(amount)
  #          print("You have purchased a Flimsy Wooden Sword")
 #           shop_inventory.remove("Flimsy Wooden Sword")
#            inventory.append("Flimsy Wooden Sword")
      #      print(inventory)
     #       print(amount)
    #        sell_2(amount)
   #     if user_purchase == "Flimsy Steel Sword":
  #          if amount == 0:
 #               print("You ran out of money")
#                exit()
     #       amount-=cost_3
    #        user_warning_3(amount)
   #         print("You have purhcased a Flimsy Steel Sword")
  #          shop_inventory.remove("Flimsy Steel Sword")
 #           inventory.append("Flimsy Steel Sword")
#            print(inventory)
    #        print(amount)
   #         sell_2(amount)
  #      else:
 #           print("Incorrect Input, Item is not in shop")
#           sell_1(amount)
#sell_1(amount)


cost_1 = 10
cost_2 = 40
cost_3 = 60
amount = 20

def user_warning_1(amount):
    if amount < 0:
        print("You do not have enough money to afford this")
        amount+=cost_1
        sell_1(amount)

def user_warning_2(amount):
    if amount < 0:
        print("You do not have enough money to afford this")
        amount+=cost_2
        sell_1(amount)

def user_warning_3(amount):
    if amount < 0:
        print("You do not have enough money to afford this")
        amount+=cost_3
        sell_1(amount)

shop_inventory = ["Health Potion", "Flimsy Wooden Sword", "Flimsy Steel Sword"]
inventory = []
class mooney():
    def __init__(self, name, amount):
        self.amount = amount
        self.name = name
    Health_Potion = ("Health Potion", 10)
    Flimsy_Wooden_Sword = ("Flimsy Wooden Sword", 40)
    Flimsy_Steel_Sword = ("Flimsy Steel Sword", 60)

stage_1 = 1

def sell_1(amount):
    print("Items for sale:")
    if "Health Potion" in shop_inventory:
        print("Health Potion Cost: 10")
    if "Flimsy Wooden Sword" in shop_inventory:
        print("Flimsy Wooden Sword Cost: 40")
    if "Flimsy Steel Sword" in shop_inventory:
        print("Flimsy Steel Sword Cost: 60")
    while stage_1 == 1:
        user_purchase = input("What would you like to buy?(Type Exit if you want to leave.): ")
        if not shop_inventory:
            print("There is nothing to buy")
            exit()
        if user_purchase == "Exit":
            print("You left the shop...")
            exit()
        if user_purchase == "Health Potion":
            if amount == 0:
                print("You ran out of money")
                print(inventory)
                exit()
            amount-=cost_1
            user_warning_1(amount)
            print("You have purchased a Heath Potion")
            shop_inventory.remove("Health Potion")
            inventory.append("Health Potion")
            print("This is your inventory:")
            print(inventory)
            print("This is the amount of money you have:")
            print(amount)
            if amount == 0:
                print("You ran out of money")
                print("You left the shop...")
                exit()
            sell_1(amount)
        if user_purchase == "Flimsy Wooden Sword":
            amount-=cost_2
            user_warning_2(amount)
            print("You have purchased a Flimsy Wooden Sword")
            shop_inventory.remove("Flimsy Wooden Sword")
            inventory.append("Flimsy Wooden Sword")
            print("This is your inventory:")
            print(inventory)
            print("This is the amount of money you have:")
            print(amount)
            if amount == 0:
                print("You ran out of money")
                exit()
            sell_1(amount)
        if user_purchase == "Flimsy Steel Sword":
            amount-=cost_3
            user_warning_3(amount)
            print("You have purhcased a Flimsy Steel Sword")
            shop_inventory.remove("Flimsy Steel Sword")
            inventory.append("Flimsy Steel Sword")
            print("This is your inventory:")
            print(inventory)
            print("This is the amount of money you have:")
            print(amount)
            if amount == 0:
                print("You ran out of money")
                exit()
            sell_1(amount)
        else:
            print("Incorrect Input, Item is not in shop")
            sell_1(amount)
sell_1(amount)