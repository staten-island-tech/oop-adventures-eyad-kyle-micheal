import random
random_thing = random.randint(1,2)
print(random_thing)

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

b = 1
while b == 1:
    if b == 1:
        number = int(input("For an item or weapon, please flip a coin, type in 1 or 2? "))
        if (number < 1 or number > 2):
            print("Incorrect Input, try again")

        if number == random_thing:
                print("You got Heads, you get a weapon")
                b = 2
                if b == 2:
                      exit()
        elif number + 1 == random_thing:
                print("You got Tails, you get a item")
                b = 2
                if b == 2:
                      exit()
        elif number - 1 == random_thing:
                print("You got Tails, you get a item")
                b = 2
                if b == 2:
                      exit()

b = 1
while b == 1:
    if b == 1:
        number = str(input("For an item or weapon, please flip a coin, type in heads or tails? "))
        if number == "heads":
              number = 1
        if number == "tails":
              number = 2

        if (number < 1 or number > 2):
            print("Incorrect Input, try again")

        if number == random_thing:
                print("You got Heads, you get a weapon")
                b = 2
                if b == 2:
                      exit()
        elif number + 1 == random_thing:
                print("You got Tails, you get a item")
                b = 2
                if b == 2:
                      exit()
        elif number - 1 == random_thing:
                print("You got Tails, you get a item")
                b = 2
                if b == 2:
                      exit()
