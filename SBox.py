import random

class PasCommon():
    def c(name, skill_health):
        return (skill_health)
Bleeding = PasCommon.c('Bleed', 0.3)
Regeneration = PasCommon.c('Regen', 0.2)

class Active():
    def BaseActive(name, skill_damage):
        return (skill_damage)
    
    def NumberedActive(name, sd, count):
        return (sd * (count))
Piercing_Slash = Active.BaseActive('Piercing Slash', 12)
count = random.randint(3, 7)
Rain = Active.NumberedActive('Rain', 3, count)
Right_Hook = Active.BaseActive('Right Hook', 12)