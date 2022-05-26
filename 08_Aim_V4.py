""" Component 8 Aim V4
Now a function
"""


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


# Main Routine
aim = num_check("What score do you aim to get on this quiz? :", 1, 10)
