# Put Certified Tested Code THAT WORKS inside green text like this!



class PasCommon():
    def c(name, skill_health):
        return (skill_health)







class Active():
    def BaseActive(name, skill_damage):
        return (skill_damage)
    
    def NumberedActive(name, sd, count):
        return (sd * (count))

import random
passiverandom = random.randint(1, 50)
Piercing_Slash = Active.BaseActive('Piercing Slash', 12)
Regeneration = PasCommon.c('Regen', 0.2)
print(Regeneration)

Regained = (Regeneration * passiverandom)
print(Regained)



# Testing below here 😭 👇 |





# Note for future self because I WILL forget:
# I need to find a way to use get a passive move like bleed or regen to affect an entity
#Bruh