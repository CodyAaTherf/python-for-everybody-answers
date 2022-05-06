# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))
pay = hours * rate

if hours > 40:
    pay = (hours - 40) * (rate * 1.5) + (40 * rate)
    print(f"Pay: {pay}")
else:
    print(f"Pay: {pay}")

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