# Control flow
# Conditional statements control the flow of program

age = input("How old is the user?   ") # Ask age of the user

if int(age) >= 18:   # If true, will print statement
    print("This user can purchase any ticket")
elif int(age) >= 15:    # If true, will print statement
    print("This user can purchase tickets with a rating of U, PG, 12, or 15")
elif int(age) >= 12:
    print("This user can purchase tickets with a rating of U, PG, or 12")
else:
    print("This user can only watch films with a rating of U or PG")