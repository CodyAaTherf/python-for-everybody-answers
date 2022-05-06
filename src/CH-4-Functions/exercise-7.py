'''
Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and
print( a )grade as a string
'''

def computegrade(score):
    if score <= 1.0:
        if score >= 0.9:
            return "A"
        elif score >= 0.8:
            return "B"
        elif score >= 0.7:
            return "C"
        elif score >= 0.6:
            return "D"
        elif score < 0.6:
            return "F"
    else:
        return "Bad score"

score = float(input("Enter score: "))
print(computegrade(score))