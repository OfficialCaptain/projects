"""
The coffee shop module contains functions and contains variables
important to implementing a coffee shop.
"""

# Set some variables
shop_name = "RuneScape Beans"
coffee_sizes = ["small", "medium", "large"]
coffee_roasts = ["hot chocolate", "light", "medium", "dark", "espresso"]
milk_type = ["dairy", "almond", "soy", "coconut"]

def order_coffee(size, roast):
    """
    Take an order from a user
    :param size: a string containing one of the coffee_sizes
    :param roast: a string containing one of the coffee_roasts
    :return: a message about the coffee order
    """
    return "Here's your {} coffee roasted {}".format(size, roast)

def add_milk(milk_type):
    return " with {}".format(milk_type)
