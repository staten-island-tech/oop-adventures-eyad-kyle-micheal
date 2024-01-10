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


# GENERAL SKILLS
Stab = Active.BaseActive('Stab', 6 )
Jab = Active.BaseActive('Jab', 4)

#CLASS SKILLS:
count = random.randint(3, 7) # Arrow count
jcount = random.randint(3, 6) # Berserker Jabs

# Warrior
Piercing_Slash = Active.BaseActive('Piercing Slash', 12) + Statis.calc(7, Bled)
impale = Active.BaseActive('Impale', 8) + Bled
divider = Active.BaseActive('Divider', 17) + Statis.calc(7, Bled)
slash = Active.BaseActive('Slash', 13) + Statis.calc(2, Bled)
big_sword= Active.BaseActive('Big Sword', 25) + Bled

# Fighter
Right_Hook = Active.BaseActive('Right Hook', 12) + Statis.calc(10, Bled)
Brass_punch = Active.BaseActive('Brass punch', 9) + Bled
# Chain Skill

def fighterchain():
    kick = Active.BaseActive('Kick', 14) + Statis.calc(20, Bled)
    slammer = Active.BaseActive('Slammer', 7) + Statis.calc(8, Bled)
    repeated = Active.NumberedActive('Repeated Kicks', 5, jcount)
    if third == 3:
        if seventh == 7:
            return repeated + slammer + kick
        else:
            return slammer + kick
    else:
        return kick
uppercut = Active.BaseActive('Uppercut', 11) + fighterchain()

# Assassin
Slash = Active.BaseActive('Slash', 3) + Statis.calc(3, Bled) + Statis.calc(4, Poison)
PStab = Active.BaseActive('Poison Stab', 4) + Statis.calc(3, Bled) + Poison
dagger_throw = Active.BaseActive('Dagger Throw', 12) + Bled + Statis.calc(3, Poison)
# Chain Skill
def assassinchain():
    blow_dart = Active.NumberedActive('Blow Darts', 2, count) + Poison # Final chain 1/15
    silencer = Active.adhominum('Silencer', 7, PasDam, count, jcount)
    if third == 3:
        if tenth == 10:
            return silencer + blow_dart
        else:
            return silencer
    else:
        return 0
shadow_step = Active.BaseActive('Shadow Step', 4) + Statis.calc(2, Poison) + assassinchain()

# Berserker 
Rage_Pound = Active.BaseActive('Pound', 13) + Statis.calc(2, Bled)
Baby_Rage = Active.BaseActive('Rage', 23) + Statis.calc(2, Bled)
Slam = Active.BaseActive('Slammer', 17) 
RepeatJab = Active.NumberedActive('Jabathon', 4, jcount) 

# Archer
Rain = Active.NumberedActive('Rain', 3, count) + Statis.calc(4, Bled)
arrow_kick = Active.BaseActive('Arrow Kick', 7) + Statis.calc(2, Bled)
gun = Active.NumberedActive('Gun', 2, (PasDam/count))
# Chain Skill
def archerchain():
    bow_chain = Active.NumberedActive('Bow Chain', 4, count)
    hells_arrow = Active.NumberedActive("Hell's arrow", 8, count) + Statis.calc(4, Bled) + Statis.calc(7, Poison)
    if quarter == 4:
        if tenth == 10:
            return hells_arrow
        else: return bow_chain
    else:
        return 0
bow_throw = Active.BaseActive('Bow Throw', 4) + archerchain()




lists=[Rain]
print(lists[0])


#used literally once
Burn = PasCommon.c('Burning', 0.4)
Burnt = (Burn * PasDam)

# Wizard
# Secret skills
Torosion = Active.adhominum('TT', 7, PasDam, PasDam, PasDam)
# Normal Skills
Fireball = Active.NumberedActive('Fireball', 7, Burnt)
Poison_Mist = Active.NumberedActive('Poison Fog', 7, Poisoned)
Staff_Yeet = Active.BaseActive('Staff_Throw', 7)











attacks = {



        'Warrior':{

                'Pierce:Deals 12 damage to target | 1/7 Bleed Chance',

                'Impale:Deals 8 damage to target + Bleed Damage',

                'Divide:Deals 17 damage to target | 1/7 Bleed Chance',

                'Slash:Deals 13 damage to target | 1/2 Bleed Chance'},

        'Wizard':{

                'Fireball:Deals 7 damage + burn damage to target',
                'Poison Mist: Surrounds the enemy in a poison fog, dealing 7 damage + Poison to target',
                'Staff Yeet:Throws staff at target at Mach 7, dealing 7 damage'},
    
        'Fighter':{

            'Uppercut:Deals 11 damage to target | 1/18 Bleed chance',
            'Kick:Deals 14 damage to target | 1/20 Bleed chance, 1/3 continuation chance',
            'Slam:Deals 7 damage to target | 1/8 Bleed chance, 1/7 continuation chance',
            'Combo:Deals base 5 damage to target 3-6 times',
            'Right Hook:Deals 12 damage to target | 1/10 Bleed Chance',
            'Brass Punch:Deals 9 damage to target + Bleed'},
            
        'Assassin':{

            'Shadow Step:Deals 4 damage to target. 1/2 Poison chance',
            'Blow DartDeals 2 damage 3-7 times. Always Poisons',
            'Silencer:Deals 7 damage a minimum of 27 times',
            'Slash:Deals 3 damage to target, with High Bleed & Poison chance',
            'Poison Stab 4 damage to target. 1/3 Bleed chance, Always Poisons',
            'Dagger Throw:Deals 12 damage to target. Always Bleed, 1/3 Poison'},

        "Berserker":{
            'Rage Pound:Deals 13 damage to target. 1/2 Bleed chance',
            'Baby Rage:Deals 23 damage to target. High Bleed chance',
            'Slam:Deals 17 damage to target',
            'Jabs:Deals 4 damage to target 3-6 times'},

        "Archerattacks" :{

            'Bow Throw:Deals 4 damage to target',
            'Bow Chain:Deals 4 damage to target 3-7 times',
            'Hells Arrow:Deals 8 damage to target 3-7 times. Low Poison & Bleed chance',
            'Arrow Rain:Deals 3 damage to target'
            'Arrow Kick:Deals 7 damage to target. 1/2 Bleed chance',
            'Gun:Deals 2 damage to target (Random) times'}}


has_kills=list(attacks['Archerattacks'])
assasin_skill =[shadow_step,slash,PStab,dagger_throw]
archer_skill = [bow_throw, arrow_kick ,gun, Rain]
b_skill = [Rage_Pound,Baby_Rage,Slam,RepeatJab]
warrior_skill = [Piercing_Slash,impale,divider,slash]
fighter_skill = [Right_Hook,Brass_punch,uppercut]
