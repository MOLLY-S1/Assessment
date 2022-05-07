""" This is a code to generate a random question from a list and ask input
then check the answer
"""
import random

# list of numbers
num_list = [['Tahi',1],['Rua',2],['Tora',3],
            ['Whā',4],['Rima',5],["Ono",6],
            ['Whitu',7],['Waru',8],['Iwa',9],
            ["Tekau",10]]

choice = input("Please press <enter> to begin")
while choice == "":
    if choice == "":
        choice = num_list

    random.shuffle(choice)

    for i in choice:
        answer = int(input("please enter the english word for {}: ".format(i[0])))
        if answer == i[1]:
            print("correct")
        else:
            print('incorrect')


