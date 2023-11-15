class Player():
    def __init__(self,health,attack,defense,speed):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed

player_class = input("What class would you like to play?:")
if player_class == ("none"):
    no_class = Player(1,1,1,1)
    print("your class is" + str(no_class.__dict__))
