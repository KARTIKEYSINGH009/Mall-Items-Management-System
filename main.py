class Items:
    def __init__(self):
        self.items_list = {}  

    def add_items(self, name, price):
        self.items_list[name] = float(price)

    def view_items(self):
        if not self.items_list:
            print("No items available.")
            return
        print("\nAvailable Items:")
        for name, price in self.items_list.items():
            print(f"- {name}: Rs.{price:.2f}")
        print()


class Cart(Items):
    def __init__(self):
        super().__init__()
        self.cart = {}  

    def add_item(self, name):
        key = name.strip()
        if key not in self.items_list:
            print("Item not available.")
            return
        self.cart[key] = self.items_list[key]
        print(f"Added '{key}' to cart.")

    def remove_item(self, name):
        key = name.strip()
        if key not in self.cart:
            print("You have not selected that item.")
            return
        del self.cart[key]
        print(f"Removed '{key}' from cart.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
            return
        print("\nYour Cart:")
        for name, price in self.cart.items():
            print(f"- {name}: Rs.{price:.2f}")
        print()

    def view_total(self):
        total = sum(self.cart.values())
        print(f"Total is Rs.{total:.2f}")


def run_shopping_mall():
    mall = Cart()
    mall.add_items("Iphone 15", 150000)
    mall.add_items("Iphone 14", 130000)
    mall.add_items("Iphone 13", 110000)
    mall.add_items("Iphone 12", 100000)
    mall.add_items("Iphone 11", 90000)
    mall.add_items("Iphone 10", 80000)
    mall.add_items("Iphone 9", 70000)
    mall.add_items("Iphone 8", 60000)
    

    while True:
        print("\n1 --> View Items")
        print("2 --> Add to cart")
        print("3 --> View Cart")
        print("4 --> View Total")
        print("5 --> Remove item")
        print("6 --> Quit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            mall.view_items()
        elif choice == "2":
            mall.view_items()
            item = input("Which item do you want? ").strip()
            mall.add_item(item)
        elif choice == "3":
            mall.view_cart()
        elif choice == "4":
            mall.view_total()
        elif choice == "5":
            item = input("Enter the item you want to remove: ").strip()
            mall.remove_item(item)
        elif choice == "6":
            print("Visit again!")
            break
        else:
            print("Enter a valid input (1-6).")


if __name__ == "__main__":
    run_shopping_mall()
