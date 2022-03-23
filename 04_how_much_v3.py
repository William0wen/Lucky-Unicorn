"""Component 2 (How Much) v3
More efficient method - includes valid range as the basis of the
while loop which eliminates the need to use the 'valid' variable
Also puts code into a function"""


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
user_balance = num_check("How much would you like to play with $", 1, 10)
print(f"You are playing with ${user_balance}.")




