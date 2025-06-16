# Define the menu of the restaurant
menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80
}

# Greet the customer
print("Welcome to KEERTHANA Restaurant")
print("Menu:")
print("Pizza: Rs40\nPasta: Rs50\nBurger: Rs60\nSalad: Rs70\nCoffee: Rs80")

# Initialize total amount
order_total = 0

# First item order
item_1 = input("Enter the name of the item you want to order: ").title()

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item '{item_1}' has been added to your order.")
else:
    print(f"Ordered item '{item_1}' is not available!")

# Ask if user wants another item
another_order = input("Do you want to add another item? (Yes/No): ").strip().lower()

if another_order == "yes":
    item_2 = input("Enter the name of the second item: ").title()

    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item '{item_2}' has been added to your order.")
    else:
        print(f"Ordered item '{item_2}' is not available!")

# Display total
print(f"\nThe total amount to pay is Rs{order_total}.")
