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

# Fighter
Right_Hook = Active.BaseActive('Right Hook', 12) #Bleed Chance 1/10
Bp = Active.BaseActive('Brass punch', 9) # Always Bleed
# Chain Skill
u = Active.BaseActive('Uppercut', 11) # 1/18 bleed | always chain
u2 = Active.BaseActive('Kick', 14) # 1/20 bleed | 1/3 chain
u3 = Active.BaseActive('Slammer', 7) # 1/8 bleed | 1/7 chain
uf = Active.NumberedActive('Repeated Kicks', 5, jcount)

# Assassin
Slash = Active.BaseActive('Slash', 3) #Bleed Chance 2/3 | Poison Chance 4/5
PStab = Active.BaseActive('Poison Stab', 4) # 1/3 Bleed Chance | Always Poison
Dt = Active.BaseActive('Dagger Throw', 12) # Always Bleed | 1/3 Poison
# Chain Skill
Ss = Active.BaseActive('Shadow Step', 4) # 1/2 Poison | Chain chance 1/3
Bd = Active.NumberedActive('Blow Darts', 2, count) # Always Poison | Final chain 1/15
Si = Active.adhominum('Silencer', 7, PasDam, count, jcount) # Always Poison | 1/8 Bleed

# Berserker 
Rage_Pound = Active.BaseActive('Pound', 13) # 1/2 Bleed Chance to enemies 
Baby_Rage = Active.BaseActive('Rage', 23) # 3/5 Bleed Chance to enemies, 1/5 Bleed Chance to self 
Slam = Active.BaseActive('Slammer', 17) # -4 damage to self, 1/2 chance
RepeatJab = Active.NumberedActive('Jabathon', 4, jcount) 


# Archer
Rain = Active.NumberedActive('Rain', 3, count) #Bleed Chance 1/4 
ak = Active.BaseActive('Arrow Kick', 7) # Bleed 1/2
Ak = Active.NumberedActive('Gun', 2, (PasDam/count)) # Side effects maybe?
# Special Chain move
Bt = Active.BaseActive('Bow Throw', 4) #Chance to activate chain skill (1/4)
btchain = Active.NumberedActive('Bow Chain', 4, count) #Final skill chance 1/12
btfinal = Active.NumberedActive("Hell's arrow", 8, count) #1/5 bleed, 1/8 poison


#Wizard



# Troll | Not Actually a thing (Yet) | Ignore this:
Shalababang = Active.adhominum('Rick Roll', 3, count, PasDam, (count * PasDam))

# Secret Skills?? | Classified as General |
Sh = Active.adhominum('Status Hell', 2, Burnt, Bled, Poison) # If R.S.N is 5 | Input [s3cret] to use
st = Active.NumberedActive('Stabathon', 6, count) # IF R.S.N is 82 | Input [s3cret] to use



