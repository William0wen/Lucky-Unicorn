"""Component 2 (How Much) v1
Ask user how much they want to play with - check if interger is
between 1 and 10. If it is, amount is set as user_balance"""

user_balance = int(input("How much are you playing for? $"))

# Keep asking until valid amount is entered
while not 1 <= user_balance <= 10:
    print("\nPlease enter a whole number between 1 and 10.")
    # ask for input
    user_balance = int(input("\nHow much are you playing for? $"))

    print(f"You are playing with ${user_balance}.")

print(f"You are playing with ${user_balance}.")




