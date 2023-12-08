from merchant import Merchant
from hero import Hero
#create a new instance of mwerchane, instantiation?
Audrey = Merchant("Audrey",['sea shell','green sweater','jarvis','Soul'])
Audrey.sell("Soul")
Merchant.greeting()
Hamburgs = Hero("Amber",500,['Hamburger'])
Audrey.sell("Soul")
Hamburgs.buy("Soul")
item = Audrey.sell("Jarvis")