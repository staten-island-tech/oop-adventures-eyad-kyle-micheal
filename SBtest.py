# Testing below here 😭 👇 |
class Entity():
    def c(self, health):
        self.health = health

class JD(Entity):
    def __init__(self, health, attack):
        super().c(health)
        self.attack = attack

class Dummy(Entity):
    def __init__(self, health):
        super().c(health)

TestDummy = Dummy(100)
print(TestDummy.__dict__)

TestPlayer = JD(100, 0.8)
print(TestPlayer.__dict__)


class PasCommon():
    def c(self, srandint, skill_health):
        import random
        srandint = random.randint(1, 50)
        self.srandint = srandint
        self.skill_health = skill_health


class Pas(PasCommon):
    def Regen(self, srandint, skill_health, regained):
        super().c(self, srandint, skill_health, )
        self.regained = regained
        skill_health = 0.2
        regained = (float(skill_health) * float(srandint))


    def Bleed(self, srandint, skill_health, lost):
        super().c(self, srandint, skill_health)
        self.lost = lost
        skill_health = 0.3
        lost = (float(skill_health) * float(srandint))
        return (TestPlayer.attack * lost)






#Do Later 👇
class ActCommon():
    def k(self,  skill_damage):
        self.skill_damage = skill_damage


class Act(ActCommon):
    def ss(self, skill_damage):
        super().k(self, skill_damage)
        skill_damage = 7
        return (skill_damage)
    
def SS():#
    import random
    change = random.randint(1, 10)
    print(change)
    if change < 8 or change == 8:
        (float(TestDummy.health) - float(Act.ss))
    elif change > 8:
        print('Failed')
    else:
        print('Broke lol | Its the code,not you 🤣')


while TestDummy.health != 0:
    ui = input("Test skill?\n Slash\n Otherwise put 'N' ")
    if ui.lower() == 'slash':
        SS()
        print(TestDummy.__dict__)
    elif ui.lower() == 'n':
        break
    else:
        pbaj = input('Y/N')
        ui = pbaj

#    def bb(self, srandint, skill_health, entity_health):
#
#
#    def usa(self, srandint, skill_health, entity_health):









# FROZEN FOR LATER USE

#def SB():#
#    import random
#    change = random.randint(1, 10)
#    print(change)
#    if change < 8 or change == 8:
#        (float(TestDummy.health) - float(Pas.Bleed))
#    elif change > 8:
#        print('Failed')
#    else:
#        print('Broke lol | Its the code,not you 🤣')
#SB()
#
#while TestDummy.health != 0:
#    ui = input("Test skill?\n Bleed\n Otherwise put 'N' ")
#    if ui.lower() == 'bleed':
#        SB()
#        print(TestDummy.__dict__)
#    elif ui.lower() == 'n':
        break
#    else:
#        pbaj = input('Y/N')
#        ui = pbaj



# Note for future self because I WILL forget:
# I need to find a way to use get a passive move like bleed or regen to affect an entity
#Bruh