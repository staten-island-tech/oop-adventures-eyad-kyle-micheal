class Enemies():
    def __init__(self,name,health,attack,defense, speed):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed

enemies=  [ Enemies("Goblin",100,0.4,0.8,100),     Enemies("Troll", 200, 2, 1, 0.05),Enemies("Giant", 1000, 10,1,0), Enemies("Wolf",75,0.5,0.5,100),
 Enemies("ogre",210,1.9,1.2,0.1)]



