# Control flow
# Conditional statements control the flow of program

age = input("How old is the user?   ") # Ask age of the user

# Code to tell user which rating of tickets they can purchase
if int(age) >= 18:      # User is older than 18 and can buy any ticket
    print("This user can purchase any ticket")
elif int(age) >= 15:    # User is older than 15, but younger than 18
    print("This user can purchase tickets with a rating of U, PG, 12, or 15")
elif int(age) >= 12:    # User is older than 12, but younger than 15
    print("This user can purchase tickets with a rating of U, PG, or 12")
else:                   # User is below the age of 12
    print("This user can only watch films with a rating of U or PG")