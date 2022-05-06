# Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

c = float(input("Enter a temperature in Celsius: "))
f = c * 9 / 5 + 32
print(f"{c}C is {f}F")

'''
Output:
Enter a temperature in Celsius: 100
100.0C is 212.0F
'''