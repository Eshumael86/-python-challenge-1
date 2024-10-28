# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered


# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number


            # 3. Check if the customer typed a number

                # Convert the menu selection to an integer


                # 4. Check if the menu selection is in the menu items

                    # Store the item name as a variable


                    # Ask the customer for the quantity of the menu item


                    # Check if the quantity is a number, default to 1 if not


                    # Add the item name, price, and quantity to the order list


                    # Tell the customer that their input isn't valid


                # Tell the customer they didn't select a menu option

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input

                # Keep ordering

                # Exit the keep ordering question loop

                # Complete the order

                # Since the customer decided to stop ordering, thank them for
                # their order

                # Exit the keep ordering question loop


                # Tell the customer to try again


# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order

    # 7. Store the dictionary items as variables


    # 8. Calculate the number of spaces for formatted printing


    # 9. Create space strings


    # 10. Print the item name, price, and quantity


# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.




# My project


# Initialize an empty list to store the customer's order
order = []

# Dictionary to store menu items for different categories
menu_items = {
    'food': {
        1: {"Item name": "Burger", "Price": 5.99},
        2: {"Item name": "Pizza", "Price": 8.99},
        3: {"Item name": "Hotdog", "Price": 3.99}
    },
    'drink': {
        1: {"Item name": "Soda", "Price": 1.99},
        2: {"Item name": "Water", "Price": 0.99},
        3: {"Item name": "Juice", "Price": 2.99}
    },
    'dessert': {
        1: {"Item name": "Ice Cream", "Price": 3.49},
        2: {"Item name": "Cake", "Price": 4.99},
        3: {"Item name": "Cookie", "Price": 1.49}
    }
}

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Set up a loop to continuously prompt the customer to place an order
place_order = True
while place_order:
    # Ask the customer which menu category they want to order from
    menu_category = input("Which category do you want to order from? Type 'food', 'drink', or 'dessert': ").lower()
    
    # Check if the chosen category is valid
    if menu_category not in menu_items:
        print("Invalid category. Please type 'food', 'drink', or 'dessert'.")
        continue

    # Display available items in the selected category
    print(f"\nHere is our {menu_category.capitalize()} menu:")
    for item_number, value in menu_items[menu_category].items():
        print(f"{item_number}: {value['Item name']} - ${value['Price']:.2f}")

    # Ask customer to input menu item number
    item_number = input("Type item number: ")

    # Check if the input is a valid number
    if item_number.isdigit():
        item_number = int(item_number)

        # Check if the selected item number exists in the menu
        if item_number in menu_items[menu_category]:
            # Store the item details
            item_name = menu_items[menu_category][item_number]["Item name"]
            item_price = menu_items[menu_category][item_number]["Price"]

            # Prompt for valid quantity
            while True:
                quantity = input(f"How many {item_name}s would you like to order? ")
                if quantity.isdigit() and int(quantity) > 0:
                    quantity = int(quantity)
                    break
                else:
                    print("Invalid quantity. Please enter a positive number.")

            # Add the item, price, and quantity to the order list
            order.append({
                "Item name": item_name,
                "Price": item_price,
                "Quantity": quantity
            })
            print(f"Added {quantity} x {item_name} to your order.")
        else:
            print("Invalid item number. Please try again.")
            continue
    else:
        print("Invalid input. Please enter a number.")
        continue

    # Ask the customer if they want to order more items
    keep_ordering = input("Would you like to order another item? (Y/N): ")

    # Check the response and update loop variable accordingly
    if keep_ordering.lower() == 'n':
        print("Thank you for your order!")
        place_order = False
    elif keep_ordering.lower() != 'y':
        print("Please type 'Y' for yes or 'N' for no.")

# Print out the complete order for the customer
print("\nThis is what we are preparing for you:\n")
print(f"{'Item name':<26}| {'Price':<6} | {'Quantity':<8}")
print("-" * 42)

# Loop through each item in the order and print it with formatted spacing
for item in order:
    item_name = item["Item name"]
    item_price = item["Price"]
    quantity = item["Quantity"]
    print(f"{item_name:<26}| ${item_price:>6.2f} | {quantity:<8}")

# Calculate and print the total cost of the order
total_cost = sum([item["Price"] * item["Quantity"] for item in order])
print(f"\nTotal cost: ${total_cost:.2f}")


