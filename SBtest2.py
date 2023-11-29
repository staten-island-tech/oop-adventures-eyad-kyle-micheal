from SBox import Pas




class Dummy():
    def __init__(self, health):
        self.health = health

TestDummy = Dummy(100)
print(TestDummy.__dict__)


bleeddamage = Pas.Bleed()


def SB():
    import random
    change = random.randint(1, 10)
    print(change)
    if change < 8 or change == 8:
        TestDummy.health = TestDummy.health - bleeddamage
    elif change > 8:
        print('Failed')
    else:
        print('Broke lol | Its the code,not you 🤣')
SB()

while TestDummy.health != 0:
    ui = input('Test skill? Y/N ')
    if ui.lower() == 'y':
        SB()
        print(TestDummy.__dict__)
    elif ui.lower() == 'n':
        break
    else:
        pbaj = input('Y/N')
        ui = pbaj