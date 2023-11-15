class Enemies():
    def __init__(self,name,health,attack,defense, speed):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
    
goblin = Enemies("Goblin",100,1100,100,100)
print(goblin.__dict__)