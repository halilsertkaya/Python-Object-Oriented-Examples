"""
Generated for example#3 writing OOB example in python 3
"""
class Dress:
    def __init__(self, color, size, price, stock):
        self.color = color
        self.size = size
        self.price = price
        self.stock = stock
    
    def sell(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            print(f"{quantity} adet {self.color} elbise satıldı.")
        else:
            print("Stokta yeterli elbise yok.")
    
    def update_stock(self, quantity):
        self.stock += quantity
        print(f"{quantity} adet {self.color} elbise stoklara eklendi.")
    
class DressStore:
    def __init__(self):
        self.dresses = []
    
    def add_dress(self, dress):
        self.dresses.append(dress)
        print(f"{dress.color} elbisesi sisteme eklendi.")
    
    def remove_dress(self, dress):
        if dress in self.dresses:
            self.dresses.remove(dress)
            print(f"{dress.color} elbisesi sistemden silindi.")
        else:
            print(f"{dress.color} elbisesi sistemde yok.")
    
    def search_dress(self, color):
        for dress in self.dresses:
            if dress.color == color:
                return dress
        return None
    
    def sell_dress(self, color, quantity):
        dress = self.search_dress(color)
        if dress:
            dress.sell(quantity)
        else:
            print(f"{color} elbisesi sistemde yok.")
    
    def update_stock(self, color, quantity):
        dress = self.search_dress(color)
        if dress:
            dress.update_stock(quantity)
        else:
            print(f"{color} elbisesi sistemde yok.")


store = DressStore()

dress1 = Dress("Kırmızı", "M", 99.99, 20)
dress2 = Dress("Siyah", "S", 149.99, 15)


store.add_dress(dress1)
# Kırmızı elbisesi sisteme eklendi.

store.add_dress(dress2)
# Siyah elbisesi sisteme eklendi.

store.remove_dress(dress2)
# Siyah elbisesi sistemden silindi.

store.sell_dress("Kırmızı", 5)
# 5 adet Kırmızı elbise satıldı.

store.update_stock("Kırmızı", 10)
# 10 adet Kırmızı elbise stoklara eklendi.