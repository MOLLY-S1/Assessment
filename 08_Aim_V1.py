""" component 8
ask for user to aim what to get on quiz
 """
# What to aim to get
aim = int(input("What do you aim to get on this quiz? : "))
# Ask until valid amount is entered
while not 1 <= aim <= 10:
     print("please enter a whole number between 1 and 10")
     # Ask for input
     aim = int(input("What do you aim to get on this quiz? :"))


