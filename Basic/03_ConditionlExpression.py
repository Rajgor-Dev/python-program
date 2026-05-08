# Conditional Expression (Ternary Operator) or If-Else Expression in Python

# Syntax: value_if_true if condition else value_if_false
x = 10
y = 20
max_value = x if x > y else y
print("Maximum value is:", max_value)

# Another example of Inline If-Else Expression
age = 18
status = "Adult" if age >= 18 else "Minor"
print("Status:", status)

# Nested If-Else Expression
a1 = int(input("Enter your Number 1 :"))
a2 = int(input("Enter your Number 2 :"))
a3 = int(input("Enter your Number 3 :"))
a4 = int(input("Enter your Number 4 :"))

if(a1>a2 and a1>a3 and a1>a4):
    print("Gratest Number is A1", a1)
elif(a2>a1 and a2>a3 and a2>a4):    
    print("Gratest Number is A2", a2)
elif(a3>a1 and a3>a2 and a3>a4):
    print("Grates Number is A3",a3)
else:
    print("Gratest Number is A4", a4)