# Recursion Function is a function that calls itself in order to solve a problem.
def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n - 1)
no = int(input("Enter a number to find its factorial: "))
print(factorial(no))  

def fibonacci(n):
    # Base case: if n is 0 or 1, return n
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case: sum of the two preceding numbers
        return fibonacci(n - 1) + fibonacci(n - 2)
num = int(input("Enter a number to find its Fibonacci value: "))
for i in range(num):
    print(fibonacci(i), end=" ")