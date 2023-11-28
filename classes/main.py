from merchant import Merchant
from hero import Hero
# Creates a new instance of Merchant, instantiation?
Audry = Merchant('Audrey', ['Sea-Shell', 'Green Sweater', 'Jarvis', 'Soul'])
Audry.sell("Soul")
Merchant.greeting()
Hambergs = Hero("Amber", 500, ['Hamburger',])
item = Audry.sell('Jarvis')
print(item)
Hambergs.buy(item)