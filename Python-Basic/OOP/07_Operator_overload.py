"""
Operator overloading is use for operatin on class objects like +,-,*,/ etc. 
we can use these operators on class objects by defining special methods in the class.
 these special methods are called magic methods or dunder methods (double underscore methods).
"""
class Calculation:
      def __init__(self, value):
         self.value = value
   
      def __add__(self, other):
         return self.value + other.value
   
      def __sub__(self, other):
         return self.value - other.value
   
      def __mul__(self, other):
         return self.value * other.value
   
      def __truediv__(self, other):
         if other.value != 0:
               return self.value / other.value
         else:
               raise ValueError("Cannot divide by zero")
obj1 = Calculation(int(input("Enter first number: ")))
obj2 = Calculation(int(input("Enter second number: ")))
print("Addition:", obj1 + obj2)  # Uses __add__
print("Subtraction:", obj1 - obj2)  # Uses __sub__
print("Multiplication:", obj1 * obj2)  # Uses __mul__
print("Division:", obj1 / obj2)  # Uses __truediv__