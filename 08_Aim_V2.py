""" Component 8 Aim V2
Use try/accept and pull error messages out of the loop"""

error = "please enter a whole number between 1 and 10\n"
valid = False

# Continue asking until a valid amount is entered
while not valid:
     try:
          # Ask for amount
          user_balance = int(input("What do you aim to get on this quiz? :"))

     # Check if amount is too low
          if 0 < user_balance <= 10:
               valid = True

          else:
               print(error)

     except ValueError:
          print(error)


