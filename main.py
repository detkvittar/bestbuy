import products
from store import Store
from menu import Menu

def main():
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]

    store = Store(product_list)
    # Start the menu, taking store as parameter
    menu = Menu(store)
    menu.start()

if __name__ == "__main__":
  main()
