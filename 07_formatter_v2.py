"""Component 5 - statement formatter v2
Changes v1 into a function
"""


# function to format text output
def formatter(symbol, text):
    sides = symbol * 3

    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main
text1 = input("Enter statement: ")
symbol1 = input("Enter format: ")
print()
print(formatter(symbol1, text1))
