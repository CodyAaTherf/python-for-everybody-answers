# '''
# Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message
# and exiting the program. The following shows two executions of the program:

# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input

# Enter Hours: forty
# Error, please enter numeric input

# '''

# hours = input("Enter Hours: ")
# rate = input("Enter Rate: ")

# try:
#     pay = hours * rate

#     if hours > 40:
#         pay = (hours - 40) * (rate * 1.5) + (40 * rate)
#         print(f"Pay: {pay}")
#     else:
#         print(f"Pay: {pay}")
# except:
#     print("Error , please enter numeric input")