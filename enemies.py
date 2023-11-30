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

goblin = Enemies("Goblin","a little green thing;embarrising if you die to it",100,0.4,0.8,100)   
troll = Enemies("Troll","a slightly bigger thing;would be less embarrisiing", 200, 2, 1, 0.05)
giant = Enemies("Giant", "this is a big boy",1000, 10,1,0)
wolf = Enemies("Wolf","...its a wolf",75,0.5,0.5,100)
ogre = Enemies("ogre","this is a very very very big thing",210,1.9,1.2,0.1)
whalen = Whalen("Whalen","this is the final boss; you are most definity going to die; you will also fail his class",2000,300,500,100,9999999999999)
a_british_person =Enemies("a british person","horrible teeth",15,0.8,0.1,90)
a_french_person =Enemies("A french man","dont let it near you government",20,0.9,0.1,100)
slime = Enemies("slime","sliiiiime",10,5,0.1,100)
Dragon = Enemies("dragon","breathes fire and stuff",250,0.2,0.8,90)
kyle = Enemies("kyle","kyle","kyle","kyle","kyle","hyle")
print(kyle.health+"-0")