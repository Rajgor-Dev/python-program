# Handling Exceptions in Python is through try, except, else, and finally blocks.
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Invalid input type. Enter Numbers only."
    else:       # Executes if no exception occurs
        return f"The result is {result}"
    finally:    # Always executes
            print("Execution of divide_numbers is complete.")
            
print(divide_numbers(10,2))
print(divide_numbers(10,0))
print(divide_numbers(10,"a"))

# Custom Exception
try:
    a = int(input("Enter a positive integer: "))
    if a<0 :
        raise ValueError("Negative value entered.")
    else:
        print(f"You entered: {a}")
except ValueError as ve:
    if "invalid literal" in str(ve):
        print("Error: Invalid input. Please enter an integer.")
    else:
        print(f"Custom Exception: {ve}")
