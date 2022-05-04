""" Function taken from 02V1 as the basis for this function
It incorperates both the yes no function and the ability to show instructions
"""

# Functions goes here
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say yes launch the game
        if answer == "yes" or "y":
            answer = "Yes"
            return answer

        # If they say no show instructions
        elif answer == "no" or "n":
            answer = "No"
            return answer

        # If anything else is entered show error message
        else:
            print("that was not a valid input please enter 'Yes' or 'No' ")

# Function 




# Main routine
show_instructions = yes_no("have you done this quiz before? :")
print(f"You entered '{show_instructions}'")

