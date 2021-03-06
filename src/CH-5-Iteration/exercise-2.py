'''
Exercise 2: Write another program that prompts for a list of numbers
as above and at the end prints out both the maximum and minimum of
the numbers instead of the average.
'''

n = input("Enter a list of numbers separated by a comma: ")
numbers = [int(i) for i in n.split(',')]

print(f"Maximum: {max(numbers)}")
print(f"Minimum: {min(numbers)}")

'''
Output:
Enter a list of numbers separated by a comma: 3,4,2,1,6,4,6 
Maximum: 6
Minimum: 1
'''