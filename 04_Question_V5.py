""" Question generator V5 based on V3
Now a function that can be recycled for other parts of the program
"""

import random


def generate_question():
    # list of numbers
    num_list = [['Tahi', "1", "one"], ['Rua', "2", "two"], ['Tora', "3", "three"],
                ['Whā', "4", "four"], ['Rima', "5", "five"], ["Ono", "6", "six"],
                ['Whitu', '7', "seven"], ['Waru', "8", "eight"], ['Iwa', "9", "nine"],
                ["Tekau", "10", "ten"]]

    # Score tracker
    score = 0

    # Enter to Begin
    choice = input("Please press <enter> to begin")
    while choice == "":
        if choice == "":
            choice = num_list

        # Shuffle the list
        random.shuffle(choice)
        # Ask question
        for i in choice:
            answer = input("please enter the english word for {}: ".format(i[0])).lower()
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

    # show the score
    return f"Your score was {score} out of ten"

# Main Routine
print(generate_question())

