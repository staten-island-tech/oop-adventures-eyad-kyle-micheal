import random

class PasCommon():
    def c(name, skill_health):
        return (skill_health)
PasDam = random.randint(3, 50)

# Passive Skills | More can be added when documents are merged
Bleeding = PasCommon.c('Bleed', 0.3)
Regeneration = PasCommon.c('Heal', 0.2)
Poisoned = PasCommon.c('Poison', 0.6)
Burn = PasCommon.c('Burning', 0.4)

# Direct Damage from Passive Skills
Bled = (Bleeding * PasDam)
Regen = (Regeneration * PasDam)
Poison = (Poisoned * PasDam)
Burnt = (Burn * PasDam)

class Active():
    def BaseActive(name, skill_damage):
        return (skill_damage)
    
    def NumberedActive(name, sd, count):
        return (sd * (count))
    
    def adhominum(name, sd, count, count2, count3):
        return (sd * count * count2 * count3)

# GENERAL SKILLS
Stab = Active.BaseActive('Stab', 6 )
Jab = Active.BaseActive('Jab', 4)

#CLASS SKILLS:

count = random.randint(3, 7) # Arrow count
jcount = random.randint(3, 6) # Berserker Jabs

# Warrior
Piercing_Slash = Active.BaseActive('Piercing Slash', 12) #Bleed Chance 1/7
i = Active.BaseActive('Impale', 8) # Bleed Always
di = Active.BaseActive('Divider', 17) #Bleed 1/7
sl = Active.BaseActive('Slash', 13) # Bleed 1/2
#Secret Skill | Warrior | Must input specific number to activate
sa = Active.BaseActive('Self Sacrafice', 0) # Halfs health of opponent and subtracts 1/4 of your health

class Dummy():
    def __init__(self, health):
        self.health = health

TestDummy = Dummy(100)
print(TestDummy.__dict__)

bas1 = 
bas2
sk1
sk2
sk3
sk4
ss

def act():
    x = input('')
    print(x)
    if x.lower() == '':
        print('')
        print(round(TestDummy.health))
# TEST
    else: 
        print('Skill not valid')
# List of Skill Options


warn = 0
while TestDummy.health > 0:
    ui = input('Test skill? Y/N ')
    if ui.lower() == 'y':
        act()
    elif ui.lower() == 'n':
        break
    else:
        print('Bro stop breaking the code and follow the instructions')
        warn += 1
        print(f"You now have {warn} warnings")
        if warn >=5:
            break


