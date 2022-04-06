"""Component 4 - game mechanics and looping v2
based on 06_rounds_v2
Removed hard-wiring so that all tokens can be generated
Gives user feedback about number of rounds and maintains balance
Test amount set to $5
"""

import random

# Main
TEST_AMOUNT = 5
balance = TEST_AMOUNT

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


# output
print(f"\nStarting balance: ${TEST_AMOUNT}.")
print(f"Final balance: ${balance:.2f}.")


