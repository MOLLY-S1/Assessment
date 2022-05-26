""" Base Component Final Version
Based off V3
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
            print()


# Function to display instructions
def instructions():
    print("*** How To Play ***")
    print()
    print("There will be 10 questions to test you knowledge of Māori numbers\n"
          "Each question can be answered as a integer or a word for that"
          " number\n"
          "At the end of the 10 questions you will be given your score out of"
          " ten\n"
          "You can then press <enter> to play again or 'x' to quit\n"
          "Have fun and good luck! ")
    print()


# Function to ask aim for quiz
def num_check(question, low, high):
    error = "That was not a valid input\n" \
             "Please enter a whole number between {} and {}\n".\
            format(low, high)

    while True:
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Function to generate questions, score and rounds
def generate_question():

    # list of numbers
    num_list = [['Tahi', "1", "one"], ['Rua', "2", "two"],
                ['Toru', "3", "three"], ['Whā', "4", "four"],
                ['Rima', "5", "five"], ["Ono", "6", "six"],
                ['Whitu', '7', "seven"], ['Waru', "8", "eight"],
                ['Iwa', "9", "nine"], ["Tekau", "10", "ten"]]

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
                print(formatter(".", f"Question {question}"))
                print()
                answer = input("Enter the english word for {}: ".
                               format(i[0])).lower()
                # If it is right show correct and add one to the score
                if answer == i[1] or answer == i[2]:
                    print(formatter("!", "Correct"))
                    print()
                    score += 1

                # If incorrect give feedback
                else:
                    print(formatter("*", 'Incorrect'))
                    print(f"The answer was {i[1]}")
                    print()
                question += 1
                # show the score
            print(formatter
                  ("/", f"Your score was {score} out of 10 questions"))

            # Give user feedback on score
            if 4 >= score:
                print("You should probably do some more studying!")
            elif 4 < score <= 6:
                print("Well done, you got half(ish) right!")
            elif 6 < score <= 9:
                print("WOW, you got more than half, that's a great score!")
            else:
                print("10/10 THAT'S AMAZING!!!")

            # Play again
            play_again = input("\n Do you want to play again?\n "
                               "press ANY BUTTON to play again or 'X' "
                               "to exit").lower()
            # Reset score to zero
            score = 0

        # Reset question number to zero
        if question > 10:
            question = 1


# Function to format statements
def formatter(symbol, text):
    sides = symbol * 5
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main routine
# Welcome Screen
print(formatter("-", " Welcome to the Māori Quiz! "))
print()

# Played before
played_before = yes_no("Have you done this quiz before? :")
if played_before == "No":
    instructions()

# Aim to get on quiz
aim = num_check("What score do you aim to get on this quiz? :", 1, 10)

# Question Generator
generate_question()

# Farewell Screen
print()
print("Thankyou for playing")
print(formatter("=", "Goodbye"))
