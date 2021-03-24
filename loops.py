# Loops

# For Loops
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
    print(f'{customer["name"]}\'s total is: {customer["bill"]}')

# While Loops
num = 0
while num <= 10:
    print(f"It's working -> {num}")
    num += 1

user_prompt = True
while user_prompt:
    age = input("Please enter your age:  ")
    if age.isdigit():       # Checks input for age was a number
        user_prompt = False
    else:
        print("Invalid input, please enter a number.")
print(f"Your age is {age}") # Only runs if the user enters their age as a number