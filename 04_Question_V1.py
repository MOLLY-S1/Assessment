""" This is a code to generate a random question from a list and ask input
then check the answer
"""
import random

# list of numbers to quiz on
num_list = [['tahi','1'],['rua','2'],['tora','3'],
            ['whā','4'],['rima','5'],["ono","6"],
            ['whitu','7'],['waru','8'],['iwa','9'],
            ["tekau","10"]]

test = num_list
random.shuffle(test)

for i in test:
    answer = int(input(f"please enter the english word for {test}".format(i[0])))
    if answer == 1[i]:
        print("correct")
    else:

