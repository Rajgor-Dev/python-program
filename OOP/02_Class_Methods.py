# There are three types of methods in a class:
'''
1. Instance Method: It takes self as the first parameter and can 
access or modify instance attributes.

2. Class Method: It takes cls as the first parameter and can 
access or modify class attributes. It is defined using @classmethod.

3. Static Method: It does not take self or cls and cannot 
access class or instance attributes directly. It is defined using @staticmethod.
'''

class Student:
    school_name = "ABC School"  # Class attribute shared by all Student objects

    def __init__(self, name, age, grade):
        self.name = name    # Instance attribute
        self.age = age      # Instance attribute
        self.grade = grade  # Instance attribute

    def get_info(self):  # Instance method
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    @classmethod
    def get_school_name(cls):  # Class method
        return f"School Name: {cls.school_name}"

    @classmethod
    def change_school_name(cls, new_name):  # Class method modifying class attribute
        cls.school_name = new_name

    @classmethod
    def from_string(cls, student_data):  # Alternative constructor using class method
        name, age, grade = student_data.split(',')
        return cls(name.strip(), int(age.strip()), grade.strip())

    @staticmethod
    def is_passing(grade):  # Static method for a grade check
        passing_grades = ['A', 'B', 'C', 'D']
        return True if grade.upper() in passing_grades else False


# Demonstrating the difference between instance methods and class methods
student1 = Student(
    input("Enter student's name: "),
    int(input("Enter student's age: ")),
    input("Enter student's grade: ")
)

print(student1.get_info())  # instance method reads data from this specific object
print(Student.get_school_name())  # class method reads class-level data
print(student1.get_school_name())  # same class method can be called from an instance too
print("Passing:", Student.is_passing(student1.grade))

# Change the class-level school name using a class method
Student.change_school_name("XYZ Academy")
print(Student.get_school_name())
print(student1.get_school_name())  # reflects the changed class attribute for all instances

# Create another student using class method alternative constructor
student2 = Student.from_string("Ali, 14, B")
print(student2.get_info())
print(student2.get_school_name())
print("Passing:", student2.is_passing(student2.grade))