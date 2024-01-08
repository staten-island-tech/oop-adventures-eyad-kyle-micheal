attacking={
    "Archerattacks" :{

            'Bow Throw:Deals 4 damage to target',
            'Bow Chain:Deals 4 damage to target 3-7 times',
            'Hells Arrow:Deals 8 damage to target 3-7 times. Low Poison & Bleed chance',
            'Arrow Rain:Deals 3 damage to target',
            'Arrow Kick:Deals 7 damage to target. 1/2 Bleed chance',
            'Gun:Deals 2 damage to target (Random) times'}}
skills = list(attacking['Archerattacks'])
for i,skill in enumerate(skills):
    print(f'{i+1}.{skill}')
