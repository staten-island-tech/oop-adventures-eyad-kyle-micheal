

class SkillCommon():
    def c(self, srandint, s_health):
        self.srandint = srandint
        self.s_health = s_health

class Pas(SkillCommon):
    def Regen(self, srandint, s_health, r):
        super().c(self, srandint, s_health)
        self.r = r
        s_health = 0.2

