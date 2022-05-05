""" V2 instructions based on V1 Instructions
now user can input single letters and all input is formatted to lowercase.
prints the user input for ease of trialling
"""

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
    print("that was not a valid input please enter 'Yes' or 'No' ")


# Show Output
print(f"You entered '{show_instructions}'")
