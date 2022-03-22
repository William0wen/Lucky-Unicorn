"""LU yes/no checking function
based on 01_yes_no_v2
"""


# Functions

def yes_no(question_text):
    while True:

        # Ask if played before
        answer = input(question_text).lower().strip()

        # If yes, program continues
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If no, display instructions
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Else, show error
        else:
            print("\nPlease answer [yes] or [no].")


# Main

show_instructions = yes_no("Have you played this game before? ")
print(f"You entered {show_instructions}")

having_fun = yes_no("Are you having fun? ")
print(f"You entered {having_fun}")
