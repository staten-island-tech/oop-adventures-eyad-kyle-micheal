

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
        return lost





# Do Later 👇
#class ActCommon():
#    def k(self, srandint, skill_health, entity_health):
#        import random
#        srandint = random.randint(1, 5)
#        self.srandint = srandint
#        self.skill_health = skill_health
#        self.entity_health = entity_health

#class Act(ActCommon):
#    def ss(self, srandint, skill_health, entity_health):
#        super().k
#
#    def bb(self, srandint, skill_health, entity_health):
#
#
#    def usa(self, srandint, skill_health, entity_health):







# Testing below here 😭 👇 |

class Dummy():
    def __init__(self, health):
        self.health = health

TestDummy = Dummy(100)
print(TestDummy.__dict__)


bleeddamage = Pas.Bleed()


def SB():
    import random
    change = random.randint(1, 10)
    print(change)
    if change < 8 or change == 8:
        TestDummy.health = TestDummy.health - bleeddamage
    elif change > 8:
        print('Failed')
    else:
        print('Broke lol | Its the code,not you 🤣')
SB()

while TestDummy.health != 0:
    ui = input('Test skill? Y/N ')
    if ui.lower() == 'y':
        SB()
        print(TestDummy.__dict__)
    elif ui.lower() == 'n':
        break
    else:
        pbaj = input('Y/N')
        ui = pbaj



# Note for future self because I WILL forget:
# I need to find a way to use get a passive move like bleed or regen to affect an entity
#Bruh