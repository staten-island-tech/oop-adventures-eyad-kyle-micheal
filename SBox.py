import random

class PasCommon():
    def c(name, skill_health):
        return (skill_health)
    
PasDam = random.randint(3, 50)
class Statis():
    def calc(percentage, name):
        x = random.randint(1, percentage)
        if x == percentage:
            return name
        else:
            return 0
# Passive things
Bleeding = PasCommon.c('Bleed', 0.3)
Poisoned = PasCommon.c('Poison', 0.6)
Bled = (Bleeding * PasDam)
Poison = (Poisoned * PasDam)
def chance(chance):
    x = random.randint(1, chance)
    return x

class Active():
    def BaseActive(name, sd):
        return (sd)
    
    def NumberedActive(name, sd, count):
        return (sd * (count))
    
    def adhominum(name, sd, count, count2, count3):
        return (sd * count * count2 * count3)
    
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
    def assassinchain():
        blow_dart = Active.NumberedActive('Blow Darts', 2, count) + Poison # Final chain 1/15
        silencer = Active.adhominum('Silencer', 7, PasDam, count, jcount)
        if third == 3:
            if twth == 20:
                return silencer + blow_dart
            else:
                return blow_dart
        else:
            return 0
    def archerchain():
        bow_chain = Active.NumberedActive('Bow Chain', 4, count)
        hells_arrow = Active.NumberedActive("Hell's arrow", 8, count) + Statis.calc(4, Bled) + Statis.calc(7, Poison)
        if quarter == 4:
            if tenth == 10:
                return hells_arrow
            else: 
                return bow_chain
        else:
            return 0
    def whaledown():
        damage = 0.1
        time = random.randint(1,100)
        while time < 90:
            damage += 0.4
            time = random.randint(1, 100)
        return round(damage)

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
uppercut = Active.BaseActive('Uppercut', 11) + Active.fighterchain()

# Assassin
Slash = Active.BaseActive('Slash', 3) + Statis.calc(3, Bled) + Statis.calc(4, Poison)
PStab = Active.BaseActive('Poison Stab', 4) + Statis.calc(3, Bled) + Poison
dagger_throw = Active.BaseActive('Dagger Throw', 12) + Bled + Statis.calc(3, Poison)
shadow_step = Active.BaseActive('Shadow Step', 4) + Statis.calc(2, Poison) + Active.assassinchain()

# Berserker 
Rage_Pound = Active.BaseActive('Pound', 13) + Statis.calc(2, Bled)
Baby_Rage = Active.BaseActive('Rage', 23) + Statis.calc(2, Bled)
Slam = Active.BaseActive('Slammer', 17) 
RepeatJab = Active.NumberedActive('Jabathon', 4, jcount) 

# Archer
Rain = Active.NumberedActive('Rain', 3, count) + Statis.calc(4, Bled)
arrow_kick = Active.BaseActive('Arrow Kick', 7) + Statis.calc(2, Bled)
gun = Active.NumberedActive('Gun', 2, (PasDam/count))
bow_throw = Active.BaseActive('Bow Throw', 4) + Active.archerchain()




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





# Whalen Skills
Hands = Active.BaseActive('Dem Hands', 17) + Statis.calc(3, Bled)
Fault = Active.BaseActive('Faulty Code', PasDam) + Statis.calc(66, Bled) + Statis.calc(66, Poison) + Statis.calc(66, Burn)
slap = Active.BaseActive('Beatdown', 0) + Active.whaledown()
# Insta Kill
Fail = Active.adhominum('Failure!', 666, PasDam, PasDam, PasDam)
whalen_skill =[Hands, Fault, slap, Fail]




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
            'Blow Dart:Deals 2 damage 3-7 times. Always Poisons',
            'Silencer:Deals 7 damage a minimum of 27 times',
            'Slash:Deals 3 damage to target, with High Bleed & Poison chance',
            'Poison Stab 4 damage to target. 1/3 Bleed chance, Always Poisons',
            'Dagger Throw:Deals 12 damage to target. Always Bleed, 1/3 Poison'},

        'Berserker':{
            'Rage Pound:Deals 13 damage to target. 1/2 Bleed chance',
            'Baby Rage:Deals 23 damage to target. High Bleed chance',
            'Slam:Deals 17 damage to target',
            'Jabs:Deals 4 damage to target 3-6 times'},

        'Archerattacks' :{

            'Bow Throw:Deals 4 damage to target',
            'Bow Chain:Deals 4 damage to target 3-7 times',
            'Hells Arrow:Deals 8 damage to target 3-7 times. Low Poison & Bleed chance',
            'Arrow Rain:Deals 3 damage to target'
            'Arrow Kick:Deals 7 damage to target. 1/2 Bleed chance',
            'Gun:Deals 2 damage to target (Random) times'}}


