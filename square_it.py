"""
Write a function that:
Takes one number
Returns the square of that number
"""

def square_it(n):
    return n * n

number = input("What number would you like to square?: ")

print(square_it(int(number)))

# Small reminder
# Functions don’t auto-output. return is how data leaves a function