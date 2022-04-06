"""LU base component - based on base_component_v1
Components after they have been created and tested.
"""

import random


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


# Function to generate token
def generate_token(balance):

    rounds_played = 0
    play_again = ""

    while play_again != "x":
        while balance >= 0:
            rounds_played += 1
            number = random.randint(1, 100)

            # Adjust balance
            # If number is between 1 and 5
            # user gets unicorn
            if 1 <= number <= 5:
                token = "unicorn"
                balance += 4

            elif 6 <= number <= 36:
                token = "donkey"
                balance -= 1

            else:
                # if even number, zebra
                if number % 2 == 0:
                    token = "zebra"
                    balance -= .5

                else:
                    token = "horse"
                    balance -= .5

            print(f"Round {rounds_played}: Token: {token}, balance: ${balance:.2f}.")
            play_again = input("\nDo you want to play another round?\n<enter> to play again or [x] to exit\n").lower().strip()
        return balance
    return balance


# Main
played_before = yes_no("Have you played this game before? ")

if played_before == "No":
    instructions()

# ask user how much they want to play with
starting_balance = num_check("How much would you like to play with $", 1, 10)
print(f"You are playing with ${starting_balance}.")

closing_balance = generate_token(starting_balance)
print(f"\nStarting balance: ${starting_balance}.")
print(f"Final balance: ${closing_balance:.2f}.")
