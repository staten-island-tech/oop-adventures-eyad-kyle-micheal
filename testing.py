from stuff import Player,Archer,Assasin,Warrior,Berserker,Fighter,Wizard,Enemies,Floors,TestAttack
import random
goblin = Enemies("Goblin","a little green thing;embarrising if you die to it",0,0.4,0.8,100)   
troll = Enemies("Troll","a slightly bigger thing;would be less embarrisiing", 200, 2, 1, 0.05)
giant = Enemies("Giant", "this is a big boy",1000, 10,1,0)
wolf = Enemies("Wolf","...its a wolf",75,0.5,0.5,100)
ogre = Enemies("ogre","this is a very very very big thing",210,1.9,1.2,0.1)
a_british_person =Enemies("a british person","horrible teeth",15,0.8,0.1,90)
a_french_person =Enemies("A french man","dont let it near you government",20,0.9,0.1,100)
slime = Enemies("slime","sliiiiime",10,5,0.1,100)
Dragon = Enemies("dragon","breathes fire and stuff",250,0.2,0.8,90)
Enemies.enemies_list=[goblin,troll,giant,wolf,ogre,a_british_person,a_french_person,slime,Dragon]
Player.classes_choice=[
        Archer("Archer",90,  .35,  1.3,  0.8,  95,  1.1,  15,"infinite"),
        Assasin("Assasin", 100, 90, 90, 150, 100, 25, 0,1000),
        Warrior("Warrior",150,125,75,100,100,75,0,1000),
        Berserker("Berserker",100,150,30,75,100,15,0,1000000),
        Fighter("Fighter",150,100,1,175,100,10,0,100000),
        Wizard("Wizard",150,10,100,100,150,300,0,10000000),
]
archer = Archer("Archer",90,  .35,  1.3,  0.8,  95,  1.1,  15,"infinite")
assasin=Assasin("assasin", 100, 90, 90, 150, 100, 25, 0,1000)
warrior=Warrior("warrior",150,125,75,100,100,75,0,1000)
b = Berserker("Berserker",100,150,30,75,100,15,0,1000000)
fighter = Fighter("fighter",150,100,1,175,100,10,0,100000)
wizard = Wizard("Wizard",150,10,100,100,150,300,0,10000000)

Player.print_classes()
chosen = Player.better_choose_class()
def tutorial():
    Player.has_skiils=[ 
        TestAttack("quick attack",20),
        TestAttack("heavy",50)
    ]
    print(chosen.__dict__)
    chosen_skill = Player.choose_skill()
    print(chosen_skill.__dict__)

tutorial()


