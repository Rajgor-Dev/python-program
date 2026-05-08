import random

l = [random.randint(1, 100) for _ in range(10)]

for index, value in enumerate(l):
   print("All Indexes")   
   print(f"The item number at {index} is {value}")
   if index % 2 == 0:
      print("Even Index")
      print(f"The item number at {index} is {value}")  
      