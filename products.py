class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise Exception("Product name cannot be empty")
        if price < 0:
            raise Exception("Product price cannot be negative")
        if quantity < 0:
            raise Exception("Product quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def buy(self, quantity):
        if quantity <= self.quantity:
            self.quantity -= quantity
            if self.quantity == 0:
                self.active = False
            return self.price * quantity
        else:
            raise Exception("Insufficient quantity in stock")

    def show(self):
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def is_active(self):
        return self.active
