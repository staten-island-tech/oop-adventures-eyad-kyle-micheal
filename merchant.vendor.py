class Merchant:
    def __init__(self, name, product):
        self.name = name
        self.product = product
    def sell(self, item):
        self.product.remove(item)
        print(f"you have purchased" (item))
        print(self.products)