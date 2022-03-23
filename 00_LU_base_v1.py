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
          "\n")


# number checking function
def num_check(question, low, high):
    error = "That was not valid input\n" \
            "Please enter a number between {} and {}\n".format(low, high)

    # Keep asking until valid amount (1-10) is entered
    while True:
        try:
            # Ask for input
            response = int(input(question))

            # Check for number within the required range
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main
played_before = yes_no("Have you played this game before? ")

if played_before == "No":
    instructions()

# ask user how much they want to play with
user_balance = num_check("How much would you like to play with $", 1, 10)
print(f"You are playing with ${user_balance}.")
