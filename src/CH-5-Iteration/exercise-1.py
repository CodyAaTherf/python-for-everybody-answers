'''
Exercise 1: Write a program which repeatedly reads numbers until the
user enters “done”. Once “done” is entered, print out the total, count,
and average of the numbers. If the user enters anything other than a
number, detect their mistake using try and except and print an error
message and skip to the next number.
'''

n = 0
total = 0
count = 0
average = 0

while True:
    n = input("Enter a number: ")

    if n == "done":
        break

    try:
        n = float(n)
    except:
        print("Invalid input")
        continue

    total = total + n
    count = count + 1

average = total / count

print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")

'''
Output:
Enter a number: 8
Enter a number: 2
Enter a number: 9
Enter a number: 1
Enter a number: 0
Enter a number: 2
Enter a number: 5
Enter a number: f
Invalid input
Enter a number: eo
Invalid input
Enter a number: 2
Enter a number: 4
Enter a number: done
Total: 33.0
Count: 9
Average: 3.6666666666666665
'''