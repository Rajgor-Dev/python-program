# Polymorphism means same method name behaves differently for different objects.

class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

for animal in (Dog(), Cat()):
    animal.sound()
# Type of polymorphism: Method Overriding
class Animal:  
      def sound(self):
         print("Animal makes a sound")
class Dog(Animal):
      def sound(self):
         print("Bark")
class Cat(Animal):
      def sound(self):
         print("Meow")
objects = [Dog(), Cat()]
for obj in objects:
      obj.sound()  # This will call the overridden method in each class

# Type of polymorphism: Method Overloading (not natively supported in Python, but can be simulated)
class Calculator:
      def add(self, a, b, c=0):
         return a + b + c     
calc = Calculator()
print(calc.add(1, 2, 3))  # This will call the add method with three parameters
print(calc.add(1, 2))     # This will call the add method with two parameters, c will default to 0
