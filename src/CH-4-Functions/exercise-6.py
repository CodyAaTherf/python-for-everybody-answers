'''
Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters
(hours and rate).
'''

def computepay(hours , rate):
    if hours > 40:
        pay = (hours - 40) * (rate * 1.5) + (40 * rate)
        print(f"Pay: {pay}")
    else:
        print(f"Pay: {hours * rate}")

hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))

computepay(hours , rate)

'''
Output:

Enter hours: 45
Enter rate: 10
Pay: 475.0
--------------------
Enter hours: 20
Enter rate: 10
Pay: 200.0
'''