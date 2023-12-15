import random
random_thing = random.randint(1,2)


class weapon():
    def __init__(self, name, damage, durability):
        self.damage = damage
        self.durability = durability

flimsy_wooden_sword = weapon("Flimsy Wooden Sword", 30, 2)

flimsy_steel_sword = weapon("Flimsy Steel Sword", 50, 2)

sturdy_wooden_sword = weapon("Sturdy Wooden Sword", 35, 3)

sturdy_steel_sword = weapon("Flimsy Steel Sword", 60, 5)

flimsy_wooden_staff = weapon("Flimsy Wooden Staff", 30 , 2)

flimsy_steel_staff = weapon("Flimsy Wooden Staff", 50 , 2)

sturdy_wooden_staff = weapon("Sturdy Wooden Staff", 35 , 3)

sturdy_steel_staff = weapon("Sturdy Steel Staff", 60 , 5)

flimsy_wooden_bow = weapon("Flimsy Wooden Bow", 30, 2)

flimsy_steel_bow = weapon("Flimsy Steel Bow", 50, 2)

sturdy_wooden_bow = weapon("Sturdy Wooden Bow", 35, 3)

sturdy_steel_bow = weapon("Sturdy Steel Bow", 60, 5)

durability_decrease = 1

choice = 1




#all inactive code below works, but tweeks can be made. subject to change

#def breaking():
    #while flimsy_wooden_sword.durability > 0:
        #move = (input("What would you like to do: "))
        #if move == ("attack"):
            #print("hit")
            #flimsy_wooden_sword.durability = (flimsy_wooden_sword.durability - durability_decrease)
            #print(flimsy_wooden_sword.durability)
        #else:
            #print("Incorrect Input, Please try again: ")
        #if flimsy_wooden_sword.durability == 0:
            #print("Your Weapon Broke!")
#breaking()
#b = 1
#while b == 1:
#    if b == 1:
#        number = int(input("For an item or weapon, please flip a coin, type in 1 or 2? "))
#        if (number < 1 or number > 2):
#            print("Incorrect Input, try again")
#
#      if number == random_thing:
#               print("You got Heads, you get a weapon")
#          b = 2
#              if b == 2:
#                     exit()
#      elif number + 1 == random_thing:
#             print("You got Tails, you get a item")
#             b = 2
#          if b == 2:
#                  exit()
#        elif number - 1 == random_thing:
#               print("You got Tails, you get a item")
#          b = 2
#        if b == 2:
#              exit()

def breaking_flimsy_wooden_sword():
    while flimsy_wooden_sword.durability > 0:
        move = (input("What would you like to do: "))
        if move == ("attack"):
            print("hit")
            flimsy_wooden_sword.durability = (flimsy_wooden_sword.durability - durability_decrease)
            print(flimsy_wooden_sword.durability)
        else:
            print("Incorrect Input, Please try again: ")
        if flimsy_wooden_sword.durability == 0:
            print("Your Weapon Broke!")
            exit()

def breaking_flimsy_wooden_bow():
    while flimsy_wooden_bow.durability > 0:
        move = (input("What would you like to do: "))
        if move == ("attack"):
            print("hit")
            flimsy_wooden_bow.durability = (flimsy_wooden_bow.durability - durability_decrease)
            print(flimsy_wooden_bow.durability)
        else:
            print("Incorrect Input, Please try again: ")
        if flimsy_wooden_bow.durability == 0:
            print("Your Weapon Broke!")
            exit()
            
def breaking_flimsy_wooden_staff():
    while flimsy_wooden_staff.durability > 0:
        move = (input("What would you like to do: "))
        if move == ("attack"):
            print("hit")
            flimsy_wooden_staff.durability = (flimsy_wooden_staff.durability - durability_decrease)
            print(flimsy_wooden_staff.durability)
        else:
            print("Incorrect Input, Please try again: ")
        if flimsy_wooden_staff.durability == 0:
            print("Your Weapon Broke!")
            exit()

def weapon_thing():
    while 1:
        weapon_choice = input("What weapon will you choose?: ")
        if weapon_choice == ("Flimsy Wooden Sword"):
            breaking_flimsy_wooden_sword()
        if weapon_choice == ("Flimsy Wooden Bow"):
            breaking_flimsy_wooden_bow()
        if weapon_choice == ("Flimsy Wooden Staff"):
            breaking_flimsy_wooden_staff()
        else:
            print("Incorrect Input, Please try again")
weapon_thing()
