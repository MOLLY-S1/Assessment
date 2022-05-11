""" This is a code to generate a random question from a list and ask input
then check the answer
"""
import random


number = random.randint(0,100)

choice = input("Please press <enter> to begin")
while choice == "":
    if choice == "":

        number = random.randint(2,100)

        if 0 <= number <= 10:
            answer = input("what is English word for Tahi?")
            if answer == "1" or answer == "one":
                print("correct")
            else:
                print("Incorrect")

        elif 11 <= number <= 20:
            answer = input("what is English word for Rua?")
            if answer == "2" or answer == "two":
                print("correct")
            else:
                print("Incorrect")

        elif 21 <= number <= 30:
            answer = input("what is English word for Toru?")
            if answer == "3" or answer == "three":
                print("correct")
            else:
                print("Incorrect")

        elif 31 <= number <= 40:
            answer = input("what is English word for Whā?")
            if answer == "4" or answer == "four":
                print("correct")
            else:
                print("Incorrect")

        elif 41 <= number <= 50:
            answer = input("what is English word for Rima?")
            if answer == "5" or answer == "five":
                print("correct")
            else:
                print("Incorrect")

        elif 51 <= number <= 60:
            answer = input("what is English word for Ono?")
            if answer == "6" or answer == "six":
                print("correct")
            else:
                print("Incorrect")
