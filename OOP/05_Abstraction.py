'''
Abstraction is the concept of hiding the complex implement details and showing only 
the necessary features of an object.
It allows us to focus on what an object does rather than how it does it. In Python,
we can achieve abstraction using abstract classes and abstract methods.
'''
from abc import ABC, abstractmethod   # Import for abstraction

# 🔹 Abstract Class (Abstraction)
class ATM(ABC):

    @abstractmethod
    def withdraw(self, amount):
        pass   # Rule: every ATM must implement withdraw()


# 🔹 Concrete Class (Encapsulation + Abstraction implementation)
class BankATM(ATM):

    def __init__(self, balance):
        self.__balance = balance   # 🔒 Encapsulation (private variable)

    # 🔹 Implementing abstract method (Abstraction)
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn ₹{amount}")
        else:
            print("Insufficient balance")

    # 🔹 Encapsulation: controlled access to private data
    def get_balance(self):
        return self.__balance


# 🔹 Using the system (User side)
atm = BankATM(5000)   # Creating object with initial balance

atm.withdraw(1000)    # User only calls method (Abstraction)
print("Balance:", atm.get_balance())