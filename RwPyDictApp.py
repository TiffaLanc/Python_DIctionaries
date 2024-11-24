
# Task 1: Restaurant Menu Update You are given an initial structure of a restaurant menu stored in a nested dictionary. 
# Your task is to update this menu based on given instructions - Add a new category called "Beverages" with at least two items.

# - Update the price of "Steak" to 17.99.

# - Remove "Bruschetta" from "Starters". 

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu["Beverages"] = {"Lemonade" : 2.49 , "Hot Tea" : 1.49}
restaurant_menu["Main Course"]["Steak"] = 17.99
restaurant_menu["Starters"].pop("Bruschetta")

print(restaurant_menu)