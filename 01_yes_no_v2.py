"""LU yes/no
same code as in v1
Prints result for test
Has a while True loop
"""

# Ask if played before

while True:
    show_instructions = input("Have you played this game before? ").lower().strip()

# If yes, program continues
    if show_instructions == "yes" or show_instructions == "y":
        print("\nprogram continues")

# If no, display instructions
    elif show_instructions == "no" or show_instructions == "n":
        print("\ndisplay instructions")

# Else, show error
    else:
        print("\nPlease answer [yes] or [no].")

print(f"You entered '{show_instructions}'")
