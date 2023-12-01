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
mana = 100
# WHALEN BOSS EXCLUSIVE
# Boss will activate after 15 - 20 turns or in a 1/100 chance
def Whailord():
    Chance = random.randint(1, 20)
    if Chance == 20:
        print('Failing your class!')
        TestDummy.health = TestDummy.health - TestDummy.health
# Damage is pending review
# WHALEN BOSS EXCLUSIVE

def SkillBleed():
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
        mana - 10
    elif Chance > 8:
        print('Failed')
    else:
        print('Broke lol | Its the code,not you 🤣')

def act():
    x = input('Pierce, Bleed, or Heal: ')
    print(x)
    if x.lower() == 'pierce':
        print('Piercing...')
        SkillPierce()
        print(round(TestDummy.health))
    elif x.lower() == 'bleed':
        print('Bleeding...')
        SkillBleed()
        print(round(TestDummy.health))
    elif x.lower() =='heal':
        print('Healing...')
        SkillHeal()
        print(round(TestDummy.health)) 
# BOSS EXCLUSIVE TEST
    elif x.lower() == 'lol':
        Whailord()
        print(round(TestDummy.health))
# TEST
    else: 
        print('Skill not valid')

while TestDummy.health > 0:
    ui = input('Test skill? Y/N ')
    if ui.lower() == 'y':
        act()
    elif ui.lower() == 'n':
        break
    else:
        print('Bro stop breaking the code and follow the instructions')