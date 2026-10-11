# Simple Bill Calculator — Week 2 Python Assignment
# Asks the user for an item price and quantity,
# then calculates and prints the total using an f-string.

# Ask the user for input (input() returns a string)
item_name = input("What is the item name? ")
price_input = input("What is the price of one item? ")
quantity_input = input("How many items do you want? ")

# Convert strings to numbers
price = float(price_input)
quantity = int(quantity_input)

# Calculate the total
total = price * quantity

# Print a friendly summary using an f-string
print(f"\nYou are buying {quantity} x {item_name}.")
print(f"{quantity} items at {price:.2f} each = {total:.2f}")
