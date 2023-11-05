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