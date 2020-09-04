import coffee_shop
from coffee_shop import add_milk

print("Welcome to", coffee_shop.shop_name)
print("Available sizes: \n", "\n".join(coffee_shop.coffee_sizes))
print("Available roasts: \n", "\n ".join(coffee_shop.coffee_roasts))
print("Available milks: \n", "\n".join(coffee_shop.milk_type))
order_size = input("What size would you like? ")
order_roast = input("What kind of roast do you want? ")

shop_says = coffee_shop.order_coffee(order_size, order_roast, add_milk)
print(shop_says)


add_milk_response = input("Do you wanna add milk? y/n")
if "y" in add_milk_response.lower():
    print("Available milks: \n", "\n".join(coffee_shop.milk_type))
    milk_type = input('What type of milk? ')
    print(shop_says)
