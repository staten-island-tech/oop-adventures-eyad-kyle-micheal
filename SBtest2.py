from SBox import PasCommon
from SBox import Active

import random
passiverandom = random.randint(1, 50)
Piercing_Slash = Active.BaseActive('Piercing Slash', 12)

Regeneration = PasCommon.c('Regen', 0.2)
Regained = (Regeneration * passiverandom)
Bleeding = PasCommon.c('Bleed', 0.3)
Bled = (Bleeding * passiverandom)
# Bled is Bleed damage, subtract it from health
# Regained is health healed, add it to health

class Dummy():
    def __init__(self, health):
        self.health = health

TestDummy = Dummy(100)
print(TestDummy.__dict__)




def SkillBleed():
    import random
    Chance = random.randint(1, 10)
    if Chance < 8 or Chance == 8:
        TestDummy.health = TestDummy.health - Bled
    elif Chance > 8:
        print('Failed')
    else:
        print('Broke lol | Its the code,not you 🤣')




def SkillHeal():
    import random
    Chance = random.randint(1, 10)
    if Chance < 8 or Chance == 8:
        TestDummy.health = TestDummy.health + Regained
    elif Chance > 8:
        print('Failed')
    else:
        print('Broke lol | Its the code,not you 🤣')

def SkillPierce():
    import random
    Chance = random.randint(1, 10)
    if Chance < 8 or Chance == 8:
        TestDummy.health = TestDummy.health - round(Piercing_Slash)
    elif Chance > 8:
        print('Failed')
    else:
        print('Broke lol | Its the code,not you 🤣')


while TestDummy.health > 0:
    ui = input('Test skill? Y/N ')
    if ui.lower() == 'y':
        print('Piercing...')
        SkillPierce()
        round(TestDummy.health)
        print(TestDummy.health)

        print('Bleeding...')
        SkillBleed()
        round(TestDummy.health)
        print(TestDummy.health)

        print('Healing...')
        SkillHeal()
        round(TestDummy.health)
        print(TestDummy.health)
    elif ui.lower() == 'n':
        break
    else:
        pbaj = input('Y/N')
        ui = pbaj