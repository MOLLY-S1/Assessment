
import random

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
            if 4 >= score:
                print("You should probably do some more studying!")
            elif 4 < score <= 6:
                print("Well done, you got half(ish) right!")
            elif 6 < score <= 9:
                print("WOW, you got more than half, that's a great score!")
            else:
                print("10/10 THAT'S AMAZING!!!")

            play_again = input("\n Do you want to play again?\n "
                               "<enter> to play again or 'X' to exit").lower()

            score = 0

        if question > 10:
            question = 1
