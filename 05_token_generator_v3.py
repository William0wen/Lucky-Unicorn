"""Component 3 (random tokens) v2
Calculate percentages to ensure the odds favour the house
5% unicorn, 30% donkey, and the remaining 65% horses/zebras"""

import random


STARTING_BALANCE = 100
balance = STARTING_BALANCE

# testing loop to generate 20 tokens
for item in range(10):
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

    print(f"Token: {token}, balance: ${balance:.2f}.")


# output
print(f"\nStarting balance: ${STARTING_BALANCE}.")
print(f"Final balance: ${balance:.2f}.")
