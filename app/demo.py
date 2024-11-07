class ShoppingCart:
    """
    A class to represent a shopping cart.
    """
    def __init__(self):
        """
        Initialize the shopping cart with an empty item dictionary.
        """
        self.items = {}

    def add_item(self, item, quantity):
        """
        Add a specified quantity of an item to the cart.

        Args:
            item (str): The name of the item to add.
            quantity (int): The quantity of the item to add.
        """
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item, quantity):
        """
        Remove a specified quantity of an item from the cart.

        Args:
            item (str): The name of the item to remove.
            quantity (int): The quantity of the item to remove.
        """
        if quantity >= self.items[item]:
            del self.items[item]
        else:
            self.items[item] -= quantity

    def get_item_count(self, item):
        """
        Get the quantity of a specific item in the cart.

        Args:
            item (str): The name of the item to check.

        Returns:
            int: The quantity of the item in the cart, or 0 if not present.
        """
        if item in self.items:
            return self.items[item]
        else:
            return 0

    def get_total_items(self):
        """
        Get the total number of items in the cart.

        Returns:
            int: The total number of items in the cart.
        """
        return sum(self.items.values())

    def get_cart_items(self):
        """
        Get a list of all items in the cart.

        Returns:
            list: A list of item names in the cart.
        """
        return list(self.items.keys())

    def clear_cart(self):
        """
        Clear all items from the cart.
        """
        self.items = {}
