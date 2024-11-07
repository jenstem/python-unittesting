import pytest
from app.demo import ShoppingCart

def test_add_item():
    """
    Test the functionality of adding an item to the shopping cart.
    """
    cart = ShoppingCart()
    cart.add_item("apple", 2)
    assert cart.get_item_count("apple") == 2
    assert cart.get_total_items() == 2
