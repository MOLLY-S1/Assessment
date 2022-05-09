""" Base Component
Functions added when they have been tested and completed
"""

import random

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


# Function to generate questions and score
def generate_question():
    # list of numbers
    num_list = [['Tahi', "1", "one"], ['Rua', "2", "two"], ['Toru', "3", "three"],
                ['Whā', "4", "four"], ['Rima', "5", "five"], ["Ono", "6", "six"],
                ['Whitu', '7', "seven"], ['Waru', "8", "eight"], ['Iwa', "9", "nine"],
                ["Tekau", "10", "ten"]]

    # Score tracker
    score = 0

    # Question tracker
    question = 1

    # Enter to Begin
    choice = input("Please press <enter> to begin")
    while choice != "":
        choice = input("Please press <enter> to begin")
        print()
    while choice == "":
        if choice == "":
            choice = num_list

        # Shuffle the list
        random.shuffle(choice)
        # Ask question
        for i in choice:
            print()
            print(f"Question {question}")
            answer = input("Please enter the english word for {}: ".format(i[0])).lower()
            # If it is right show correct and add one to the score
            if answer == i[1] or answer == i[2]:
                print("Correct")
                print()
                score += 1


            # If incorrect give feedback
            else:
                print('Incorrect')
                print(f"The answer was {i[1]}")
                print()
            question += 1
    # show the score
    return f"Your score was {score} out of ten"


# Main routine
played_before = yes_no("have you done this quiz before? :")
if played_before == "No":
    instructions()
    print(generate_question())
else:
    print(generate_question())

