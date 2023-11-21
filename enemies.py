class Enemies():
    def __init__(self,name,health,attack,defense, speed):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
goblin = Enemies("Goblin",100,0.4,0.8,100)    
troll = Enemies("Troll", 200, 2, 1, 0.05)
giant = Enemies("Giant", 1000, 10,1,0)
wolf = Enemies("Wolf",75,0.5,0.5,100)

ogre = Enemies("ogre",210,1.9,1.2,0.1)