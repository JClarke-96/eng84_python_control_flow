# Loops

# Create a shopping list and print each item
shopping_list = ["bread", "eggs", "milk", "oranges"]
for item in shopping_list:
    print(item)
    if item == "milk":
        break   # Escape the loop at milk

for letter in "fruits":
    print(letter)

food_bill = {1: {"name": "James", "bill": "£1"},
             2: {"name": "Bond", "bill": "£2"},
             3: {"name": "Shah", "bill": "£3"}}

for customer in food_bill.values():
    print(f"{customer["name"]}'s total is: {customer["bill"]}")
    print(customer["name"])