import random

class PasCommon():
    def c(name, skill_health):
        return (skill_health)
Bleeding = PasCommon.c('Bleed', 0.3)
Regeneration = PasCommon.c('Heal', 0.2)
Poisoned = PasCommon.c('Poison', 0.6)

class Active():
    def BaseActive(name, skill_damage):
        return (skill_damage)
    
    def NumberedActive(name, sd, count):
        return (sd * (count))
# GENERAL SKILLS
Stab = Active.BaseActive('Stab', 6 )
Jab = Active.BaseActive('Jab', 4)

#CLASS SKILLS:

# Warrior
Piercing_Slash = Active.BaseActive('Piercing Slash', 12) #Bleed Chance 1/7

# Fighter
Right_Hook = Active.BaseActive('Right Hook', 12) #Bleed Chance 1/10

# Assassin
Slash = Active.BaseActive('Slash', 3) #Bleed Chance 2/3 | Poison Chance 4/5

# Beserker | They dont get to choose skills#
Baby_Rage = Active.BaseActive('Rage', 23) # 3/5 Bleed Chance to enemies, 1/5 Bleed Chance to self
Rage_Pound = Active.BaseActive('Pound', 13) # 1/2 Bleed Chance to enemies, 1/4 to self



# Archer
count = random.randint(3, 7) # Arrow count
Rain = Active.NumberedActive('Rain', 3, count) #Bleed Chance 1/4