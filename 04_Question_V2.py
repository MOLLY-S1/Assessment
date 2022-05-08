""" Question generator V2 based on V1
questions can now be answered by either integer or string
"""
import random

# list of numbers
num_list = [['Tahi',"1", "one"],['Rua',"2", "two"],['Tora',"3", "three"],
            ['Whā',"4", "four" ],['Rima',"5", "five"],["Ono","6", "six"],
            ['Whitu','7',"seven"],['Waru',"8", "eight"],['Iwa',"9", "nine"],
            ["Tekau","10", "ten"]]

choice = input("Please press <enter> to begin")
while choice == "":
    if choice == "":
        choice = num_list

    random.shuffle(choice)

    for i in choice:
        answer = input("please enter the english word for {}: ".format(i[0])).lower()
        if answer == i[1] or answer == i[2]:
            print("correct")
            print()
        else:
            print('incorrect')
            print()


