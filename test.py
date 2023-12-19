class PasCommon():
    def c(name, skill_health):
        return (skill_health)
Passive ={
    "Bleeding":PasCommon.c('Bleed', 0.3),
    "Regeneration":PasCommon.c('Heal', 0.2),
    "Poisoned":PasCommon.c('Poison', 0.6),
    "Burn":PasCommon.c('Burning', 0.4)
}
attacks = {
    'passive': {
        'name': 'Bleeding', 'damage':PasCommon.c('Bleed', 0.3),
    "Regeneration":PasCommon.c('Heal', 0.2),
    "Poisoned":PasCommon.c('Poison', 0.6),
    "Burn":PasCommon.c('Burning', 0.4)
}
}
print(attacks['passive']['name'])
print(attacks['passive']['Bleeding'])