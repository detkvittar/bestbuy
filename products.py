class Product:
    def __init__(self, name, price, quantity):
        if not name:  # Name is empty
            raise ValueError("Product name cannot be empty")
        if price < 0:  # Price is negative
            raise ValueError("Product price cannot be negative")
        if quantity < 0:  # Quantity is negative
            raise ValueError("Product quantity cannot be negative")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def buy(self, quantity):
        if quantity > self.quantity:  # Trying to buy more than available
            raise ValueError("Insufficient quantity in stock")
        self.quantity -= quantity
        if self.quantity == 0:
            self.active = False
        return self.price * quantity

    def show(self):
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def is_active(self):
        return self.active


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 0)  # 0 quantity, never changes

    def buy(self, quantity):
        # Quantity always remains zero, so no need to subtract from it
        return self.price * quantity

    def show(self):
        # Overridden show method to indicate unlimited quantity
        return f"{self.name}, Price: ${self.price}, Quantity: Unlimited"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        if quantity > self.maximum:
            raise ValueError("Quantity exceeds the maximum limit for this product")
        return super().buy(quantity)

    def show(self):
        # Overridden show method to indicate limited quantity per order
        return f"{self.name}, Price: ${self.price}, Limited to {self.maximum} per order!"
