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
        self.promotion = None

    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_promotion(self):
        return self.promotion

    def show(self):
        promo = f", Promotion: {self.promotion.name}" if self.promotion else ", Promotion: None"
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}{promo}"

    def buy(self, quantity):
        if quantity > self.quantity:
            raise ValueError("Requested quantity exceeds available stock")

        self.quantity -= quantity

        if self.quantity == 0:
            self.active = False

        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        else:
            return self.price * quantity

    def is_active(self):
        return self.active


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 0)  # 0 quantity, never changes

    def buy(self, quantity):
        # No need to modify quantity as these aren't stocked products
        # Just calculate price and return
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        else:
            return self.price * quantity

    def show(self):
        promo = f", Promotion: {self.promotion.name}" if self.promotion else ", Promotion: None"
        return f"{self.name}, Price: ${self.price}, Quantity: Unlimited{promo}"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        if quantity > self.maximum:
            raise ValueError("Quantity exceeds the maximum limit for this product")

        return super().buy(quantity)

    def show(self):
        promo = f", Promotion: {self.promotion.name}" if self.promotion else ", Promotion: None"
        return f"{self.name}, Price: ${self.price}, Limited to {self.maximum} per order!{promo}"
