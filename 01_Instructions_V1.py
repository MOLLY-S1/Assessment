"""Code to ask user if they have played before
if not show the instructions
"""

# Ask the user if they have played before
show_instructions = input("Have you done this quiz before?: ")

# If they say yes launch the game
if show_instructions == "yes":
    print("launch quiz")

# If they say no show instructions
elif show_instructions == "no":
    print("Show instructions")

# If anything else is entered show error message
else:
    print("that was not a valid input please enter 'Yes' or 'No' ")
