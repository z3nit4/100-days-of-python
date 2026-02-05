"""
Writing a Function that:
- Takes a number
- Returns whether it's even or odd
"""
def even_or_odd(n):
    if n % 2 == 0:
        return "Your number is Even"
    else:
        return "Your number is Odd"

number = int(input("Enter any number: "))
print(even_or_odd(number))