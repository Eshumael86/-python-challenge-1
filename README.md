# -python-challenge-1


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
