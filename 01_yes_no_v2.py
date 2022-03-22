"""LU yes/no
Simplifies input using .lower()
Also accepts 'y' or 'n'
Prints result for test
Has a while True loop
"""

# Ask if played before

while True:
    show_instructions = input("Have you played this game before? ").lower().strip()

# If yes, program continues
    if show_instructions == "yes" or show_instructions == "y":
        print("\nprogram continues")
        break

# If no, display instructions
    elif show_instructions == "no" or show_instructions == "n":
        print("\ndisplay instructions")
        break

# Else, show error
    else:
        print("\nPlease answer [yes] or [no].")

print(f"You entered '{show_instructions}'")
