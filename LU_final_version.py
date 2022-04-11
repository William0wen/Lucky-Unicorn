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
    print(formatter("*", "How to Play"))
    print("\nChoose a starting amount to play with - between $1 and $10")
    print("\nThen press <enter> to play. You will get a random token"
          "\nwhich might be a horse, a zebra, a donkey or a unicorn.")
    print("\nIt costs $1 to play each round but, depending on your prize, you "
          "\ncould win your money back. These are the payout amounts:"
          "\n\tUnicorn: $5 (balance increases by $4)"
          "\n\tHorse: $0.50 (balance decreases by $0.50)"
          "\n\tZebra: $0.50 (balance decreases by $0.50)"
          "\n\tDonkey: $0 (balance decreases by $1)")
    print("\nSee if you can get less donkeys, more unicorns, and finish with "
          "\nmore money than you started with.\n")

    print("*" * 50)
    print()


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


# function to generate token
def generate_token(balance):

    rounds_played = 0
    play_again = ""

    while play_again != "x":
        rounds_played += 1
        print(formatter(".", f"Round {rounds_played}"))
        print()
        number = random.randint(1, 100)

        # Adjust balance
        # If number is between 1 and 5
        # user gets unicorn
        if 1 <= number <= 5:
            balance += 4
            print(formatter("!", "Congratulations, you got a Unicorn"))
            print()

        elif 6 <= number <= 36:
            balance -= 1
            print(formatter("D", "Bad luck, you got a Donkey"))

        else:
            # if even number, zebra
            if number % 2 == 0:
                balance -= .5
                print(formatter("Z", "You got a Zebra"))

            else:
                balance -= .5
                print(formatter("H", "You got a Horse"))

        print(f"\nYour balance is now ${balance:.2f}.")
        if balance < 1:
            print("\nSorry, you have run out of money.")
            play_again = "x"
        else:
            play_again = input("\nDo you want to play another round?"
                               "\n<enter> to play again or [x] to exit\n").lower().strip()

    return balance


# function to format text output
def formatter(symbol, text):
    sides = symbol * 3

    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main
print(formatter("-", "Welcome to the Lucky Unicorn Game"))
print()

played_before = yes_no("Have you played this game before? ")

if played_before == "No":
    instructions()

# ask user how much they want to play with
starting_balance = num_check("How much would you like to play with $", 1, 10)
print(f"You are playing with ${starting_balance}.")

closing_balance = generate_token(starting_balance)
print(f"\nStarting balance: ${starting_balance}.")
print(f"Final balance: ${closing_balance:.2f}.\n")

print(formatter("*", "Goodbye"))
