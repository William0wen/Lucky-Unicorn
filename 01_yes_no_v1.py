"""LU yes/no
Simplifies input using .lower()
Also accepts 'y' or 'n'
"""


# Ask if played before
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
