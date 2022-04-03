"""Component 3 (random tokens) v2
Calculate user balance based on a random selection"""

import random

tokens = ["unicorn", "horse", "zebra", "donkey"]
balance = 100

# testing loop to generate 20 tokens
for item in range(20):
    token = random.choice(tokens)
    print(token, end="\t")  # Can wrap output, making it easier to screenshot

    # Adjust balance
    if token == "unicorn":
        balance += 4
    elif token == "donkey":
        balance -= 1
    else:
        balance -= .5

    # output
    print(f"Token: {token}, Balance: ${balance}")
