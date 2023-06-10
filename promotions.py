from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        discount = self.percent / 100
        total = product.price * quantity * (1 - discount)
        return total


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        full_price_items = (quantity + 1) // 2
        half_price_items = quantity // 2
        total = full_price_items * product.price + half_price_items * product.price * 0.5
        return total


class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        full_price_items = (quantity // 3) * 2 + (quantity % 3)
        total = full_price_items * product.price
        return total
