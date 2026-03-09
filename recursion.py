# RECURSION

# A function calling itself to solve a smaller version of the same problem.
# Instead of using loops, the function keeps calling itself until it reaches a base case (the condition that stops the recursion).

# 9! = 9 * 8 * 7 * 6 * 5 * 4 *3 * 2 * 1 # Non-recursive factorial of 9

# 9! = 9 * 8! # Recursive factorial

# Non-recursive
n = 7 
fact = 1
while n> 0:
    fact = fact * n 
    n -= 1

print(fact)

# Recursive 
def factorial(n):
    if n < 1:
        return 1
    else:
        number = n * factorial(n-1)
        return number
    
print(factorial(7))


# Non-recursive function to calculate Fibonacci numbers.
def fibonacci(n):
    a, b = 0, 1
    for x in range(n):
        a, b = b, a+b

    return a

print(fibonacci(15))

# Recursive function to calculate Fibonacci numbers.
def fibonacci2(n):
    if n <= 1:
        return n
    else:
        return(fibonacci2(n-1) + fibonacci2(n-2))
    
print(fibonacci2(25)) # ~1000 recursive calls creates a RecursionError - using too many recursions (stack overflow)