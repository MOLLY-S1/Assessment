""" Component to loop rounds and play again"""

import random
score = 0

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

    # Rounds
    play_again = ""
    while play_again != 'x':

        # Enter to Begin

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
                print(".",f"Question {question}")
                print()
                answer = input("Please enter the english word for {}: ".format(i[0])).lower()
                # If it is right show correct and add one to the score
                if answer == i[1] or answer == i[2]:
                    print("!","Correct")
                    print()
                    score += 1


                # If incorrect give feedback
                else:
                    print("*",'Incorrect')
                    print(f"The answer was {i[1]}")
                    print()
                question += 1

            play_again = input("\n Do you want to play again?\n "
            "<enter> to play again or 'X' to exit").lower()

            if question > 10:
                question = 1


# Main Routine
generate_question()
