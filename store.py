from products import Product

class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_total_quantity(self):
        return sum(product.quantity for product in self.products if product.is_active())

    def get_all_products(self):
        print("------")
        for i, product in enumerate(self.products, 1):
            if product.is_active():
                print(f"{i}. {product.show()}")
        print("------")

    def order(self, shopping_list):
        total_cost = 0
        for product, quantity in shopping_list:
            total_cost += product.buy(quantity)
        return total_cost
