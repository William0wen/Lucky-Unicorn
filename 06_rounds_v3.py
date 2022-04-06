"""Component 4 - game mechanics and looping v2
Converting v2 into a function
"""

import random


# Function to generate token
def generate_token(balance):

    rounds_played = 0
    play_again = ""

    while play_again != "x" and balance != 0:
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


# Main
starting_balance = 5
closing_balance = generate_token(starting_balance)
print(f"\nStarting balance: ${starting_balance}.")
print(f"Final balance: ${closing_balance:.2f}.")


