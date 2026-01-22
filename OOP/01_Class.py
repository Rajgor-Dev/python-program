# Class is a blueprint for creating objects.
#  It defines a set of attributes and methods that the created objects will have.

class Student:
    # Constructor to initialize the attributes
    def __init__(self, name, age, grade): #self define the instance means the object itself
        self.name = name
        self.age = age
        self.grade = grade
    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
# Creating an object of the Student class
name = input("Enter student's name: ")
age = int(input("Enter student's age: "))
grade = input("Enter student's grade: ")
student1 = Student(age, name, grade)
# Accessing the method of the Student class
print(student1.get_info())
    