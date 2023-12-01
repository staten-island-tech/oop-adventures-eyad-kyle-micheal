class Enemies():
    def __init__(self,name,descripton,health,attack,defense, speed):
        self.name = name
        self.description = descripton
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
class Whalen(Enemies):
    def __init__(self,name,description,health,attack,defense, speed,Authority):
        super().__init__(name,description,health,attack,defense, speed)
        self.authority = Authority
whalen = Whalen("Whalen","this is the final boss; you are most definity going to die; you will also fail his class",2000,300,500,100,9999999999999)

print (whalen.__dict__)