""" Base Component
Functions added when they have been tested and completed
"""


# Yes/No checking function
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say yes launch the game
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no show instructions
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # If anything else is entered show error message
        else:
            print("Please enter 'Yes' or 'No' ")


# Function to display instructions
def instructions():
    print("*** How To Play ***")
    print()
    print("The Rules of the Quiz Will Go Here")
    print()
    print("Program Continues")
    print()


# Main routine
played_before = yes_no("have you done this quiz before? :")
if played_before == "No":
    instructions()
else:
    print("program continues")

