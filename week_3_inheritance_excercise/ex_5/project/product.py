class Product:
    def __init__(self, name: str, quantity: int):
        self.quantity = quantity
        self.name = name

    def decrease(self, quantity: int):
        if self.quantity - quantity >= 0:
            self.quantity -= quantity

    def increase(self, quantity: int):
        self.quantity += quantity

    def __repr__(self):
        return self.name
