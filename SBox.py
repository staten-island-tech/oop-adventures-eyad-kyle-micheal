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
half = random.random()
third = random.random()
quarter = random.randint(1,2)
seventh = random.randint(1,7)
tenth = random.randint(1,10)

def bh():
    if half == 2:
        return Bled
    else:
        return 0
def bt():
    if third == 3:
        return Bled
    else:
        return 0
def bq():
    if quarter == 4:
        return Bled
    else:
        return 0
def bs():
    if seventh == 7:
        return Bled
    else:
        return 0
def bte():
    if tenth == 10:
        return Bled
    else:
        return 0

def ph():
    if half == 2:
        return Poison
    else:
        return 0
def pt():
    if third == 3:
        return Poison
    else:
        return 0
def pq():
    if quarter == 4:
        return Poison
    else:
        return 0
def ps():
    if seventh == 7:
        return Poison
    else:
        return 0
def pte():
    if tenth == 10:
        return Poison
    else:
        return 0
# test zone

# GENERAL SKILLS
Stab = Active.BaseActive('Stab', 6 )
Jab = Active.BaseActive('Jab', 4)

#CLASS SKILLS:
count = random.randint(3, 7) # Arrow count
jcount = random.randint(3, 6) # Berserker Jabs

# Warrior
Bleed4=0
Piercing_Slash = (Active.BaseActive('Piercing Slash', 12)) + Bleed4

impale = Active.BaseActive('Impale', 8) + Bled

Piercing_Slash = Active.BaseActive('Piercing Slash', 12) #Bleed Chance 1/7
impale = Active.BaseActive('Impale', 8) # Bleed Always
print(Piercing_Slash)
divider = Active.BaseActive('Divider', 17) #Bleed 1/7
slash = Active.BaseActive('Slash', 13) # Bleed 1/2


Piercing_Slash = Active.BaseActive('Piercing Slash', 12) + bs()
impale = Active.BaseActive('Impale', 8) + Bled
divider = Active.BaseActive('Divider', 17) + bs()
slash = Active.BaseActive('Slash', 13) + bh()


divider = Active.BaseActive('Divider', 17) + Bleed4
slash = Active.BaseActive('Slash', 13) + Bleed4

big_sword= Active.BaseActive('Big Sword', 25) + Bled

# Fighter
Right_Hook = Active.BaseActive('Right Hook', 12) + bte()
Brass_punch = Active.BaseActive('Brass punch', 9) + Bled
# Chain Skill
uppercut = Active.BaseActive('Uppercut', 11) + Bled + bh() #always chain
kick = Active.BaseActive('Kick', 14) # 1/3 chain
slammer = Active.BaseActive('Slammer', 7) #1/7 chain
repeated = Active.NumberedActive('Repeated Kicks', 5, jcount)
fighter_skill = [Right_Hook,Brass_punch,uppercut,kick,slammer,repeated]


# Assassin
Slash = Active.BaseActive('Slash', 3) + bt() + pq()
PStab = Active.BaseActive('Poison Stab', 4) + bt() + Poison
dagger_throw = Active.BaseActive('Dagger Throw', 12) + Bled + pt()
# Chain Skill
shadow_step = Active.BaseActive('Shadow Step', 4) # 1/2 Poison | Chain chance 1/3
blow_dart = Active.NumberedActive('Blow Darts', 2, count) # Always Poison | Final chain 1/15
silencer = Active.adhominum('Silencer', 7, PasDam, count, jcount)

# Berserker 
Rage_Pound = Active.BaseActive('Pound', 13) + bh()
Baby_Rage = Active.BaseActive('Rage', 23) + bh()
Slam = Active.BaseActive('Slammer', 17) 
RepeatJab = Active.NumberedActive('Jabathon', 4, jcount) 

# Archer
Rain = Active.NumberedActive('Rain', 3, count) + bq()
arrow_kick = Active.BaseActive('Arrow Kick', 7) + bh()
gun = Active.NumberedActive('Gun', 2, (PasDam/count))
# Special Chain move
bow_throw = Active.BaseActive('Bow Throw', 4) #Chance to activate chain skill (1/4)
bow_chain = Active.NumberedActive('Bow Chain', 4, count) #Final skill chance 1/12
hells_arrow = Active.NumberedActive("Hell's arrow", 8, count) #1/5 bleed, 1/8 poison 

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
            'Arrow Rain:Deals 3 damage to target',
            'Arrow Kick:Deals 7 damage to target. 1/2 Bleed chance',
            'Gun:Deals 2 damage to target (Random) times'}}


has_kills=list(attacks['Archerattacks'])
assasin_skill =[shadow_step,blow_dart,silencer,slash,PStab,dagger_throw]
archer_skill = [bow_throw,bow_chain,hells_arrow,arrow_kick ,gun]
b_skill = [Rage_Pound,Baby_Rage,Slam,RepeatJab]
warrior_skill = [Piercing_Slash,impale,divider,slash]
def printing_skills():
    for i,skill in enumerate(has_kills):
        print(f'{i+1}.{skill}')
printing_skills()
def choice():
    
    while True:
        try:
            x=(input(":::"))
            x = int(x)
            if x <=len(has_kills):
                print(f'You chose the skill \n{has_kills[x-1]}')
                return has_kills[x-1]
            else:
                print(":(")
        except ValueError:
            print("uh oh")
choice()
    


