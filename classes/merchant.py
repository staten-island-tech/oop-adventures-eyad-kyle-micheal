class Merchant():
    def __init__(self,name,products):
        self.name = name
        self.products = products
    def sell(self,items):
        self.products.remove(items)
        print(f'you have perchase {items}')
        print(self.products)
        return items
    @staticmethod
    def greeting():
        print("welcome to my shop")
