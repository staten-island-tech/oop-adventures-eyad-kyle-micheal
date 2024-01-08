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
half = random.random(1,2)
third = random.random(1,3)
quarter = random.randint(1,4)
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
Piercing_Slash = Active.BaseActive('Piercing Slash', 12) + bs()
impale = Active.BaseActive('Impale', 8) + Bled
divider = Active.BaseActive('Divider', 17) + bs()
slash = Active.BaseActive('Slash', 13) + bh


#Secret Skill | Warrior | Must input specific number to activate
big_sword= Active.BaseActive('Big Sword', 25)

# Fighter
Right_Hook = Active.BaseActive('Right Hook', 12) + bte()
Brass_punch = Active.BaseActive('Brass punch', 9) + Bled
# Chain Skill
uppercut = Active.BaseActive('Uppercut', 11) # 1/18 bleed | always chain
kick = Active.BaseActive('Kick', 14) # 1/20 bleed | 1/3 chain
slammer = Active.BaseActive('Slammer', 7) # 1/8 bleed | 1/7 chain
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

    'passive': {

        'Bleed': {
        "Bleeding":PasCommon.c('Bleed', 0.3),'Description':'Deals 0.3 bleed damage to target'},

        'Regen':{
        "Regeneration":PasCommon.c('Heal', 0.2),'Description':'Heals 0.2 health to target'},

        'Poison':{
        "Poisoned":PasCommon.c('Poison', 0.6),'Description':'Deals 0.6 poison damage to target'},

        'Burn':{
        "Burnt":PasCommon.c('Burning', 0.4),'Description':'Deals 0.4 burn damage to target'}},


    'active':{

        'General':{
            'Secret':{
                'Stabathon':{
                "Damage":Active.NumberedActive('Stabathon', 6, count), 'Description':'Call me London, deals 6 damage per stab'},

                'Status Hell':{
                "Damage":Active.adhominum('Status Hell', 2, Burnt, Bled, Poison), 'Description':'Shadow Wizard Money Gang | We love casting spells'}},


            'Normal':{
                'Stab':{
                "Damage":Active.BaseActive('Stab', 6), "Description":'Deals 6 damage to the opps'},

                'Jab':{
                "Damage":Active.BaseActive('Jab', 4), "Description":'Deals 4 damage to the opps'},
            
                'Stomp':{
                "Damage":Active.BaseActive('Stomp', 5), "Description":'Deals 5 damage to the opps'}}},


        'Warrior':{

            'Secret':{
                'Divine Slash':{
                "Damage":Active.BaseActive('big_sword', 25), 'Description':'Deals 15 damage to target'}},


            'Normal':{
                'Pierce':{
                "Damage":Active.BaseActive('Piercing Slash', 12), 'Description': 'Deals 12 damage to target | 1/7 Bleed Chance'},

                'Impale':{
                "Damage":Active.BaseActive('Impale', 8), 'Description': 'Deals 8 damage to target + Bleed Damage'},

                'Divide':{
                "Damage":Active.BaseActive('Divider', 17), 'Description': 'Deals 17 damage to target | 1/7 Bleed Chance'},

                'Slash':{
                "Damage":Active.BaseActive('Slash', 13), 'Description': 'Deals 13 damage to target | 1/2 Bleed Chance'}}},

        'Wizard':{
            'Secret':{
                'Torosion':{
                "Damage":Active.adhominum('TT', 7, PasDam, PasDam, PasDam), 'Description': 'Deals massive damage multiplied by 7'}},
            
            'Normal':{
                'Fireball':{
                "Damage":Active.NumberedActive('Fireball', 7, Burnt), 'Description': 'Deals 7 damage + burn damage to target'},
                'Poison Mist':{
                "Damage":Active.NumberedActive('Poison Fog', 7, Poisoned), 'Description': 'Surrounds the enemy in a poison fog, dealing 7 damage + Poison to target'},
                'Staff Yeet':{
                "Damage":Active.BaseActive('Staff_Throw', 7), 'Description': 'Throws staff at target at Mach 7, dealing 7 damage'}}},
    
        'Fighter':{
            'Chain':{
            'Uppercut':{
            "Damage":Active.BaseActive('Uppercut', 11), 'Description':'Deals 11 damage to target | 1/18 Bleed chance'},
            'Kick':{
            "Damage":Active.BaseActive('Kick', 14), 'Description':'Deals 14 damage to target | 1/20 Bleed chance, 1/3 continuation chance'},
            'Slam':{
            "Damage":Active.BaseActive('Slammer', 7), 'Description':'Deals 7 damage to target | 1/8 Bleed chance, 1/7 continuation chance'},
            'Combo':{
            "Damage":Active.NumberedActive('Combo Kicks', 5, jcount), 'Description':'Deals base 5 damage to target 3-6 times'}},

            'Normal':{
            'Right Hook':{
            "Damage":Active.BaseActive('Right Hook', 12), 'Description':'Deals 12 damage to target | 1/10 Bleed Chance'},
            'Brass Punch':{
            "Damage":Active.BaseActive('Brass Punch', 9), 'Description':'Deals 9 damage to target + Bleed'}}},
            
        'Assassin':{
            'Chain':{
            'Shadow Step':{
            "Damage":Active.BaseActive('Shadow Step', 4), 'Description':'Deals 4 damage to target. 1/2 Poison chance'},
            'Blow Dart':{
            "Damage":Active.NumberedActive('Blow Darts', 2, count), 'Description':'Deals 2 damage 3-7 times. Always Poisons'},
            'Silencer':{
            "Damage":Active.adhominum('Silencer', 7, PasDam, count, jcount), 'Description':'Deals 7 damage a minimum of 27 times'}},

            'Normal':{
            'Slash':{
            "Damage":Active.BaseActive('Slash', 3), 'Description':'Deals 3 damage to target, with High Bleed & Poison chance'},
            'Poison Stab':{
            "Damage":Active.BaseActive('Poison Stab', 4), 'Description':'Deals 4 damage to target. 1/3 Bleed chance, Always Poisons'},
            'Dagger Throw':{
            "Damage":Active.BaseActive('Dagger Throw', 12), 'Description':'Deals 12 damage to target. Always Bleed, 1/3 Poison'}}},

        "Berserker":{
            'Normal':{
            'Rage Pound':{
            "Damage":Active.BaseActive('Pound', 13), 'Description':"Deals 13 damage to target. 1/2 Bleed chance"},
            'Baby Rage':{
            "Damage":Active.BaseActive('Rage', 23), 'Description':"Deals 23 damage to target. High Bleed chance"},
            'Slam':{
            "Damage":Active.BaseActive('Slammer', 17), 'Description':"Deals 17 damage to target"},
            'Jabs':{
            "Damage":Active.NumberedActive('Jabathon', 4, jcount), 'Description':"Deals 4 damage to target 3-6 times"}}},

        "Archerattacks" :{
            'Chain':{
            'Bow Throw':{
            "Damage":Active.BaseActive('Bow Throw', 4), 'Description':'Deals 4 damage to target'},
            'Bow Chain':{
            "Damage":Active.NumberedActive('Bow Chain', 4, count), 'Description':'Deals 4 damage to target 3-7 times'},
            'Hells Arrow':{
            "Damage":Active.NumberedActive("Hell's arrow", 8, count), 'Description':'Deals 8 damage to target 3-7 times. Low Poison & Bleed chance'}},

            'Normal':{
            'Arrow Rain':{
            "Damage":Active.NumberedActive('Rain', 3, count), 'Description':'Deals 3 damage to target'},
            'Arrow Kick':{
            "Damage":Active.BaseActive('Arrow Kick', 7), 'Description':'Deals 7 damage to target. 1/2 Bleed chance'},
            'Gun':{
            "Damage":Active.NumberedActive('Gun', 2, (PasDam/count)), 'Description':'Deals 2 damage to target (Random) times'}}}}}

has_kills={}
has_kills=attacks['active']['Warrior']['Normal']
assasin_skill =[shadow_step,blow_dart,silencer,slash,PStab,dagger_throw]
archer_skill = [bow_throw,bow_chain,hells_arrow,arrow_kick ,gun]
b_skill = [Rage_Pound,Baby_Rage,Slam,RepeatJab]
warrior_skill = [Piercing_Slash,impale,divider,slash]


