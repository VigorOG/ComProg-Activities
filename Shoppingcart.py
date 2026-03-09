class Cart:
    def __init__(self):
        self.cart_list = []

    def view(self):
        if self.cart_list == []:
            print("\nCart is empty")
        else:
            print("\nItems in cart:")
            i = 0
            for item in self.cart_list:
                print(i + 1, ".", item)
                i = i + 1

    def add(self):
        item = input("\nEnter item name: ")
        self.cart_list.append(item)
        print("Item added")

    def remove(self):
        if self.cart_list == []:
            print("\nNothing to remove")
        else:
            self.view()
            num = int(input("Enter number of item to remove: "))
            num = num - 1

            if num >= 0 and num < len(self.cart_list):
                removed = self.cart_list.pop(num)
                print(removed, "removed")
            else:
                print("Wrong number")

    def checkout(self):
        if self.cart_list == []:
            print("\nCart is empty")
        else:
            print("\nYou bought:")
            for x in self.cart_list:
                print("-", x)

            print("Thank you!")
            self.cart_list = []


mycart = Cart()

while True:
    print("\nShopping Cart")
    print("1 View cart")
    print("2 Add item")
    print("3 Remove item")
    print("4 Checkout")
    print("5 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        mycart.view()

    elif choice == "2":
        mycart.add()

    elif choice == "3":
        mycart.remove()

    elif choice == "4":
        mycart.checkout()

    elif choice == "5":
        print("Bye")
        break

    else:
        print("Invalid choice")