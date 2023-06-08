from products import Product
from store import Store
from menu import Menu


def main():
    # Create some products
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    pixel = Product("Google Pixel 7", price=500, quantity=250)

    # Create a store and add the products to it
    store = Store()
    store.add_product(bose)
    store.add_product(mac)
    store.add_product(pixel)

    # Start the menu, taking store as parameter
    menu = Menu(store)
    menu.start()

if __name__ == "__main__":
  main()