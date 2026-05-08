lst = [1, 2, 3, 4, 5]

# Map Example 
squared = list(map(lambda x: x ** 2, lst))
print("Squared List:", squared)

# Filter Example
even_numbers = list(filter(lambda x: x % 2 == 0, lst))
print("Even Numbers:", even_numbers)

# Reduce Example
from functools import reduce
mul = reduce(lambda x, y: x * y, lst)
print("Reduce :", mul)