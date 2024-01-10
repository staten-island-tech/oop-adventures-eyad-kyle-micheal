import random


class PasCommon():
    def c(name, skill_health):
        return (skill_health)
    
PasDam = random.randint(3, 50)

# Passive things
Bleeding = PasCommon.c('Bleed', 0.3)
Poisoned = PasCommon.c('Poison', 0.6)
Bled = (Bleeding * PasDam)
Poison = (Poisoned * PasDam)

class Active():
    def BaseActive(name, sd):
        return (sd)
    
    def NumberedActive(name, sd, count):
        return (sd * (count))
    
    def adhominum(name, sd, count, count2, count3):
        return (sd * count * count2 * count3)

# test zone
half = random.randint(1,2)
third = random.randint(1,3)
quarter = random.randint(1,4)
seventh = random.randint(1,7)
tenth = random.randint(1,10)

class Statis():
    def calc(percentage, name):
        x = random.randint(1, percentage)
        if x == percentage:
            return name
        else:
            return 0
        
Piercing_Slash = Active.BaseActive('Piercing Slash', 12) + Statis.calc(100, Bled)
print(Piercing_Slash)