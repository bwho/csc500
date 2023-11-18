# New class ItemsToPurchase to create objects for an online shopping cart
class ItemsToPurchase:
    
    # Initialization method with default values of:
    # * item_name = "none"  (data type string)
    # * item_price = 0.0  (data type float)
    # * item_quantity = 0  (data type integer)
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = str(item_name)
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)

    # Method to print out subtotal costs per each item object, including formatting to reinforce preferred data types
    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity:d} @ ${self.item_price:.2f} = ${(self.item_quantity * self.item_price):.2f}")

# Instantiate two ItemsToPurchase objects
item1 = ItemsToPurchase()
item2 = ItemsToPurchase()

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

# Add additional new line to block the total costs together
print("\nTOTAL COST")

# Call print_item_cost function in ItemsToPurchase class to print out the subtotal costs for each of the two items
item1.print_item_cost()
item2.print_item_cost()

# Calculate the subtotal costs per each of the two items and add them together, then print out the total
total_cost = (item1.item_quantity * item1.item_price) + (item2.item_quantity * item2.item_price)
print(f"Total: ${total_cost:.2f}")