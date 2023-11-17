

class PasCommon():
    def c(self, srandint, skill_health, entity_health):
        import random
        srandint = random.randint(1, 50)
        self.srandint = srandint
        self.skill_health = skill_health
        self.entity_health = entity_health

class Pas(PasCommon):
    def Regen(self, srandint, skill_health, entity_health, regained):
        super().c(self, srandint, skill_health, entity_health)
        self.regained = regained
        skill_health = 0.2
        regained = (float(skill_health) * float(srandint))
        entity_health = (float(entity_health) + float(regained))

    def Bleed(self, srandint, skill_health, entity_health, lost):
        super().c(self, srandint, skill_health, entity_health)
        self.lost = lost
        skill_health = 0.3
        lost = (float(skill_health) * float(srandint))
        entity_health = (float(entity_health) - float(lost))




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

bleed = Pas.Bleed
print(bleed.__dict__)


# Note for future self because I WILL forget:
# I need to find a way to use get a passive move like bleed or regen to affect an entity