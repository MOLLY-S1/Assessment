""" V3 Instructions based on V2 Instructions
converts code from V2 into a loop for ease of testing
"""

show_instructions = ""
while show_instructions != 'x':

    # Ask the user if they have played before
    show_instructions = input("Have you done this quiz before?: ").lower()

    # If they say yes launch the game
    if show_instructions == "yes" or show_instructions == "y":
        print("launch quiz")

    # If they say no show instructions
    elif show_instructions == "no" or show_instructions == "n":
        print("Show instructions")

    # If anything else is entered show error message
    else:
        print("please enter 'Yes' or 'No' ")

    # Show Output
    print(f"You entered '{show_instructions}'")
