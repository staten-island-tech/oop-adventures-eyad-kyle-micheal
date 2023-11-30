from SBox import PasCommon
from SBox import Active

import random
passiverandom = random.randint(1, 50)
Piercing_Slash = Active.BaseActive('Piercing Slash', 12)

Regeneration = PasCommon.c('Regen', 0.2)
Regained = (Regeneration * passiverandom)
Bleeding = PasCommon.c('Bleed', 0.3)
Bled = (Bleeding * passiverandom)


class Dummy():
    def __init__(self, health):
        self.health = health

TestDummy = Dummy(100)
print(TestDummy.__dict__)




def SB():
    import random
    Chance = random.randint(1, 10)
    print(Chance)
    if Chance < 8 or Chance == 8:
        TestDummy.health = TestDummy.health - Bled
    elif Chance > 8:
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