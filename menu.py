class Menu:
    def __init__(self, store):
        self.store = store

    def start(self):
        while True:
            print("""
Store Menu
----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
            """)

            choice = input("Please choose a number: ")
            if choice == '1':
                self.store.get_all_products()

            elif choice == '2':
                print(f"Total of {self.store.get_total_quantity()} items in store")

            elif choice == '3':
                print("(Press enter when finished.)")
                shopping_list = []

                while True:
                    try:
                        product_number = input("Which product # do you want? ")
                        if product_number == '':
                            break

                        product_number = int(product_number)
                        quantity = int(input("What amount do you want? "))
                        product = self.store.products[product_number - 1]
                        # - 1 because the indexes of the lists start from 0
                        # in the system but from 1 in the menu
                        shopping_list.append((product, quantity))
                    except ValueError:
                        print("Invalid input. Please enter a valid product number and quantity.")
                    except IndexError:
                        print("Product number does not exist. Please enter a valid product number.")

                if not shopping_list:
                    print("No items were added to the order. Order cancelled.")
                else:
                    try:
                        total_price = self.store.order(shopping_list)
                        print(f"Order made! Total payment: ${total_price}")
                    except Exception as e:
                        print(f"Order could not be completed: {str(e)}")

            elif choice == '4':
                break
            else:
                print("Invalid choice, try again")
