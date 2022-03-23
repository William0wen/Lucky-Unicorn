"""LU base component
Components after they have been created and tested."""


# yes/no checking function
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


# display instructions function
def instructions():
    print("\n\t**** How to Play ****"
          "\n\tThe rules of the game go here"
          "\n\nProgram continues\n")


# Main

played_before = yes_no("Have you played this game before? ")

if played_before == "No":
    instructions()
else:
    print("Program continues")
