# Function is a block of reusable code that performs a specific task.

# Defining a function
def greet(name):
    return f"Hello, {name}!"
# Calling the function
print(greet("Yash"))  


def palindrome_check(string):
    # Check if the string is equal to its reverse
    return string == string[::-1]
txt = input("Enter a string: ")
if palindrome_check(txt.lower()):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
