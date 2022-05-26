""" Component 8 Aim V3
Makes the code more efficient - includes the valid range as a basis for
while loops
"""

error = "That was not a valid input\n"
aim = 0

# Continue asking until a valid amount is entered
while not 1 <= aim <= 10:
     try:
          # Ask for amount
          aim = int(input("Please enter a whole number between "
                                   "1 and 10\n What do you aim to get on this "
                                   "quiz? :"))
          print()

     except ValueError:
          print(error)




