# CLASS DECORAT
def logged(cls):
    """
    Class decorator that logs object creation.
    """

    class Wrapped(cls):

        def __init__(self, *args, **kwargs):

            print("=" * 40)
            print(f"[LOG] Creating object of class: {cls.__name__}")
            print(f"[LOG] Arguments received: {args}")
            print("=" * 40)

            # Call original constructor
            super().__init__(*args, **kwargs)

    return Wrapped

# USING CLASS DECORAT
@logged
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # PROPERTY GETTER
    @property
    def name(self):
        """
        Getter method.
        Allows: person.name
        """
        print("[GETTER] Getting name...")
        return self._name

    # PROPERTY SETTER
    @name.setter
    def name(self, value):
        """
        Setter method.
        Allows: person.name = value
        """
        print("[SETTER] Setting name...")

        # Validation
        if not isinstance(value, str):
            raise ValueError("Name must be a string")

        if len(value) < 2:
            raise ValueError("Name is too short")

        self._name = value

    # NORMAL METHOD
    def introduce(self):
        print(f"Hello! My name is {self._name} and I am {self._age} years old.")

    # STRING REPRESENTATION    
    def __repr__(self):
        return f"Person(name='{self._name}', age={self._age})"

# MAIN PROGRAM
if __name__ == "__main__":

    # Object creation
    person1 = Person("Alice", 22)
    print()

    # Getter automatically called
    print(person1.name)
    print()

    # Setter automatically called
    person1.name = "Bob"
    print()

    # Method call
    person1.introduce()
    print()

    # __repr__
    print(person1)


#Other Example of Proprty Decorator
class Employee:
   salary = 100 # Class attribute
   increment = 10
   @property
   def salary_after_increment(self):
      return self.salary + (self.salary * self.increment / 100)
   @salary_after_increment.setter
   def salary_after_increment(self, new_salary):
      self.increment = ((new_salary / self.salary)-1) * 100

e = Employee()
print("Current Salary:", e.salary)
print("Salary after increment:", e.salary_after_increment)
e.salary_after_increment = int(input("Enter new salary after increment: "))
print("New Increment Percentage:", e.increment ,"%")