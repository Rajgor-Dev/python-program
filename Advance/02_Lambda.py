# Lambda functions are anonymous functions that can have any number of arguments but only one expression. 
# They are often used for short, simple functions.
# That are not worth defining with a full function definition.


# def cube(x):
#    return x ** 3

"""
Syntax: 
variable = lambda arguments: expression
""" 
cube = lambda x: x ** 3
print("Cube of 3:", cube(3))  