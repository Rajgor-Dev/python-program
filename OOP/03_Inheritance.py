#There are types of inheritance in python 
'''
1. Single Inheritance: A child class inherits from a single parent class.
2. Multiple Inheritance: A child class inherits from multiple parent classes.
3. Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another parent class.
4. Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
5. Hybrid Inheritance: A combination of two or more types of inheritance.
'''
# Example of Single Inheritance
class Person:  
      def __init__(self, name, age):
         self.name = name
         self.age = age
   
      def get_info(self):
         return f"Name: {self.name}, Age: {self.age}"
class Student(Person):  # Student inherits from Person
      def __init__(self, name, age, grade):
         Person.__init__(self, name, age)  # Call the parent class constructor
         self.grade = grade
   
      def get_student_info(self):
         return f"{self.get_info()}, Grade: {self.grade}"
      
# Example of Multiple Inheritance
class Teacher:
      def __init__(self, subject):
         self.subject = subject
   
      def get_subject(self):
         return f"Subject: {self.subject}"   
class TeachingAssistant(Student, Teacher):  # TeachingAssistant inherits from both Student and Teacher
      def __init__(self, name, age, grade, subject):
         Student.__init__(self, name, age, grade)
         Teacher.__init__(self, subject)
      def get_ta_info(self):
         return f"{self.get_student_info()}, {self.get_subject()}"
      
# Example of Multilevel Inheritance
class GraduateStudent(Student):  # GraduateStudent inherits from Student
      def __init__(self, name, age, grade, research_topic):
         super().__init__(name, age, grade)
         self.research_topic = research_topic
   
      def get_graduate_info(self):
         return f"{self.get_student_info()}, Research Topic: {self.research_topic}"
      
# Example of Hierarchical Inheritance
class Employee(Person):  # Employee inherits from Person 
      def __init__(self, name, age, position):
         super().__init__(name, age)
         self.position = position
   
      def get_employee_info(self):
         return f"{self.get_info()}, Position: {self.position}"
class Manager(Employee):  # Manager inherits from Employee
      def __init__(self, name, age, position, department):
         super().__init__(name, age, position)
         self.department = department
   
      def get_manager_info(self):
         return f"{self.get_employee_info()}, Department: {self.department}"     
      
# Example of Hybrid Inheritance
class Researcher(Person):  # Researcher inherits from Person
      def __init__(self, name, age, field):
         Person.__init__(self, name, age)
         self.field = field
   
      def get_researcher_info(self):
         return f"{self.get_info()}, Field: {self.field}"   
class ResearchAssistant(Researcher, Student):  # ResearchAssistant inherits from both Researcher and Student
      def __init__(self, name, age, field, grade):
         Person.__init__(self, name, age)
         self.field = field
         self.grade = grade
   
      def get_research_assistant_info(self):
         return f"{self.get_researcher_info()}, Grade: {self.grade}"
'''   
In summary, inheritance allows us to create new classes based on existing ones,
 promoting code reusability and a hierarchical class structure. 

The different types of inheritance provide flexibility in how classes can be related to each other,
 enabling developers to design their applications in a way that best fits their needs.
'''

# Example usage
if __name__ == "__main__":
    # Single Inheritance example
    student = Student("Alice", 20, "A")
    print(student.get_student_info())
    
    # Multiple Inheritance example
    ta = TeachingAssistant("Bob", 25, "B", "Math")
    print(ta.get_ta_info())
    
    # Multilevel Inheritance example
    grad_student = GraduateStudent("Charlie", 22, "A-", "AI Research")
    print(grad_student.get_graduate_info())
    
    # Hierarchical Inheritance example
    employee = Employee("David", 30, "Developer")
    print(employee.get_employee_info())
    
    manager = Manager("Eve", 35, "Senior Developer", "Engineering")
    print(manager.get_manager_info())
    
    # Hybrid Inheritance example
    researcher = Researcher("Frank", 28, "Physics")
    print(researcher.get_researcher_info())
    
    research_assistant = ResearchAssistant("Grace", 24, "Chemistry", "B+")
    print(research_assistant.get_research_assistant_info())