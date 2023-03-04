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
            print(f"{quantity} piece of {self.color} cloth has been sold.")
        else:
            print("Not enough quantity for sell.")
    
    def update_stock(self, quantity):
        self.stock += quantity
        print(f"{quantity} piece of {self.color} cloth has been sold.")
    
class DressStore:
    def __init__(self):
        self.dresses = []
    
    def add_dress(self, dress):
        self.dresses.append(dress)
        print(f"{dress.color} cloth has been added to system.")
    
    def remove_dress(self, dress):
        if dress in self.dresses:
            self.dresses.remove(dress)
            print(f"{dress.color} cloth successfully deleted in system.")
        else:
            print(f"{dress.color} cloth not found in system.")
    
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
            print(f"{color} cloth is not found in system.")
    
    def update_stock(self, color, quantity):
        dress = self.search_dress(color)
        if dress:
            dress.update_stock(quantity)
        else:
            print(f"{color} cloth is not found in system.")


store = DressStore()

dress1 = Dress("Kırmızı", "M", 99.99, 20)
dress2 = Dress("Siyah", "S", 149.99, 15)


store.add_dress(dress1)
# Add

store.add_dress(dress2)
# Add

store.remove_dress(dress2)
# Remove

store.sell_dress("Kırmızı", 5)
# Sell Piece

store.update_stock("Kırmızı", 10)
# Update Stock-Colot