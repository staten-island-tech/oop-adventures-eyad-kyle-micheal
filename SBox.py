import random

class PasCommon():
    def c(name, skill_health):
        return (skill_health)
PasDam = random.randint(3, 50)

# Passive Skills
Bleeding = PasCommon.c('Bleed', 0.3)
Regeneration = PasCommon.c('Heal', 0.2)
Poisoned = PasCommon.c('Poison', 0.6)

# Direct Damage from Passive Skills
Bled = (Bleeding * PasDam)
Regen = (Regeneration * PasDam)
Poison = (Poisoned * PasDam)

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

# Warrior
Piercing_Slash = Active.BaseActive('Piercing Slash', 12) #Bleed Chance 1/7

# Fighter
Right_Hook = Active.BaseActive('Right Hook', 12) #Bleed Chance 1/10

# Assassin
Slash = Active.BaseActive('Slash', 3) #Bleed Chance 2/3 | Poison Chance 4/5
PStab = Active.BaseActive('Poison Stab', 4) # 1/3 Bleed Chance | Always Poison


# Beserker |
Rage_Pound = Active.BaseActive('Pound', 13) # 1/2 Bleed Chance to enemies 
Baby_Rage = Active.BaseActive('Rage', 23) # 3/5 Bleed Chance to enemies, 1/5 Bleed Chance to self 
Slam = Active.BaseActive('Slammer', 17) # -4 damage to self, 1/2 chance
jcount = random.randint(3, 6)
RepeatJab = Active.NumberedActive('Jabathon', 4, jcount) 


# Archer
count = random.randint(3, 7) # Arrow count
Rain = Active.NumberedActive('Rain', 3, count) #Bleed Chance 1/4 
ak = Active.BaseActive('Arrow Kick', 7) # Bleed 1/2
Ak = Active.NumberedActive('Gun', 2, (PasDam/count)) # drains your mana based off skill damage
# Special Chain move
Bt = Active.BaseActive('Bow Throw', 4) #Chance to activate chain skill (1/4)
btchain = Active.NumberedActive('Bow Chain', 4, count) #Final skill chance 1/12
btfinal = Active.NumberedActive("Hell's arrow", 8, count) #1/5 bleed, 1/8 poison 


# Troll | Not Actually a thing (Yet)
Shalababang = Active.adhominum('Rick Roll', 3, count, PasDam, (count * PasDam))
