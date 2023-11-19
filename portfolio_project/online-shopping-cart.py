# Class ItemToPurchase to create objects for an online shopping cart
class ItemToPurchase:
    
    # Initialization method with default values of:
    # * item_name = "none"  (data type string)
    # * item_description = "none"  (data type string)
    # * item_price = 0.0  (data type float)
    # * item_quantity = 0  (data type integer)
    def __init__(self, item_name="none", item_description= "none", item_price=0.0, item_quantity=0):
        self.item_name = str(item_name)
        self.item_description = str(item_description)
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)

    # Method to print out subtotal costs per each item object, including formatting to reinforce preferred data types
    # Expects no parameters; other than print statements, no values returned
    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity:d} @ ${self.item_price:.2f} = ${(self.item_quantity * self.item_price):.2f}")

    # Method to print out descriptions per each item object
    # Expects no parameters; other than print statements, no values returned
    def print_item_cost(self):
        print(f"{self.item_name}: {self.item_description}")

# Class Shopping cart that has typical CRUD methods for a shopping cart and a few additional methods to sum & print
class ShoppingCart:

    # Initialization method with default values of:
    # * customer_name = "none"  (data type string)
    # * current_date = "January 1, 2020"  (data type string)
    # * cart_items as a local empty array
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = str(customer_name)
        self.current_date = str(current_date)
        self.cart_items = []

    # Method to add a new item to the cart
    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    # Method to remove an item from the cart, including error proofing if item is not already in the cart
    # Expects an item object as the only parameter; other than print statements, no values returned
    def remove_item(self, item_to_purchase):
        
        # Initialize Boolean sentinel value to False
        found_item = False

        # Loop over each item in cart to see if item name passed in matches the name of an existing item in the cart
        for item in self.cart_items:

            # If a match hasnt't been found and the item name does match, then set the sentinel to True, remove the
            # item from the cart 
            if (not(found_item) and (item_to_purchase.item_name == item.item_name)):
                found_item = True
                self.cart_items.remove(item_to_purchase)
        
        # If the item was never found in the cart, then print a message letting the user know
        if not(found_item):
            print("Item not found in cart. Nothing removed.")

    # Method to modify an existing item in the cart, including error proofing if item is not already in the cart
    # Expects an item object as the only parameter; other than print statements, no values returned  
    def modify_item(self, item_to_purchase):
        # Initialize Boolean sentinel value to False
        found_item = False

        # Loop over each item in cart to see if item name passed in matches the name of an existing item in the cart
        for item in self.cart_items:

            # If a match hasnt't been found and the item name does match, then set the sentinel to True, remove the
            # item from the cart 
            if (not(found_item) and (item_to_purchase.item_name == item.item_name)):
                found_item = True
                
                # If each of the other three object values aren't default values, then update them to match the
                # passed in item's values
                if (item_to_purchase.item_description != "none"):
                    item.item_description = item_to_purchase.item_description
                if (item_to_purchase.item_price != 0.0):
                    item.item_price = item_to_purchase.item_price
                if (item_to_purchase.item_quantity != 0):
                    item.item_quantity = item_to_purchase.item_quantity

        # If the item was never found in the cart, then print a message letting the user know
        if not(found_item):
            print("Item not found in cart. Nothing modified.")

    # Method to sum the number of items in the cart
    # Expects no parameters; returns the number of items in the cart
    def get_num_items_in_cart(self):

        # Loop over cart items using list comprehension to gather the sum of all items
        num_items_in_cart = sum(item.item_quantity for item in self.cart_items)
        
        # Return the total items
        return num_items_in_cart

    # Method to sum the cost of the items in the cart
    # Expects no parameters; returns the cost of the items in the cart
    def get_cost_of_cart(self):

        # Loop over cart items using list comprehension to gather the cost of all items 
        cost_of_cart = sum(item.item_price * item.item_quantity for item in self.cart_items)

        #Return the total cost
        return cost_of_cart

    # Method to print out a nicely formatted cost-based cart list, including the cart owner's name, the date, total
    # number of items, followed by the subtotals for each item and quantity and the total cost for everything
    def print_total(self):

        # As long as the cart isn't empty proceed with the print formatting -- if it is empty, let the user know
        if (self.cart_items):

            # Print the header values: list owner's name, the date, and the number of items in the cart
            print(f"\n{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            
            # Loop over each item in the cart and call print_item_cost() method to print out the subtotal values
            for item in self.cart_items:
                item.print_item_cost()
            
            # Print the total cost for the cart
            print(f"Total: ${self.get_cost_of_cart():.2f}")
        else:
            # If the cart is empty, let the user know
            print("SHOPPING CART IS EMPTY")

    # Method to print out nicely formatted decription-based cart list, including the cart owner's name, the date, a
    # descriptive header, followed by the name and description of each item
    def print_descriptions(self):
        
        # As long as the cart isn't empty proceed with the print formatting -- if it is empty, let the user know
        if (self.cart_items):

            # Print the header values: list owner's name, the date, and the descriptive header
            print(f"\n{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Item Descriptions")

            # Loop over each item in the cart and call print_item_description() method to print out the descriptions
            for item in self.cart_items:
                item.print_item_description()          
        else:
            # If the cart is empty, let the user know
            print("SHOPPING CART IS EMPTY")
    
# Method to print out the shopping cart menu 
def print_menu(shopping_cart):
    quit_selected = False

    while not(quit_selected):
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        print("Choose an option:")

        menu_choice = input()

        if (menu_choice == 'q'):
            quit_selected = True

    print(f"Menu choice: {menu_choice}")

# Main method containing entry point code
def main():
    cart = ShoppingCart("Barrett", "November 18, 2023")
    print_menu(cart)

    # Instantiate two ItemToPurchase objects
    item1 = ItemToPurchase()
    item2 = ItemToPurchase()

    # Get the first item's name, price, and quantity from the user
    print("Item 1")
    item1.item_name = input("Enter the item name: ")
    item1.item_price = float(input("Enter the item price: "))
    item1.item_quantity = int(input("Enter the item quantity: "))

    # Get the second item's name, price, and quantity from the user
    print("\nItem 2")
    item2.item_name = input("Enter the item name: ")
    item2.item_price = float(input("Enter the item price: "))
    item2.item_quantity = int(input("Enter the item quantity: "))

    # Testing block

    cart.add_item(item1)
    cart.add_item(item2)

    cart.print_total()

# Use special __name__ variable to allow for other methods contained in the file to be run directly from the command
# line if deisred
if __name__ == "__main__":
    main()