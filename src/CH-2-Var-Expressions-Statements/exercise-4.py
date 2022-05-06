'''
Exercise 4: Assume that we execute the following assignment statements:
width = 17
height = 12.0
For each of the following expressions, write the value of the expression and the type (of the value of the expression).
1. width//2
2. width/2.0
3. height/3
4. 1 + 2 * 5
'''

width = 17
height = 12.0

print(f"1. Value of width = {width//2} and type = {type(width//2)}")
print(f"2. Value of width = {width/2.0} and type = {type(width/2.0)}")
print(f"3. Value of height = {height/3} and type = {type(height/3)}")
print(f"4. Value of 1 + 2 * 5 = {1 + 2 * 5} and type = {type(1 + 2 * 5)}")

'''
Output:
1. Value of width = 8 and type = <class 'int'>
2. Value of width = 8.5 and type = <class 'float'>
3. Value of height = 4.0 and type = <class 'float'>
4. Value of 1 + 2 * 5 = 11 and type = <class 'int'>
'''