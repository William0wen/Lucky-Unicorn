"""Component 2 (How Much) v1
use try/except and pull error message out of loop"""

error = "Please enter a whole number between 1 and 10\n"
valid = False

# Keep asking until valid amount (1-10) is entered
while not valid:
    try:
        # Ask for input
        user_balance = int(input("How much are you playing with? $"))

        # Check if the amount is too high-low
        if 0 < user_balance <= 10:
            print(f"You are playing with ${user_balance}.")
            valid = True
        else:
            print(error)

    except ValueError:
        print(error)




