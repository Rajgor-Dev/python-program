# Tuples are similar to lists but are immutable.
# i.e. we cannot change, add or remove elements from a tuple.

data = ("dev","rajgor",25,5.9,True) 
print("Data Tuple : ", data) 
print("Data Type of data is : ", type(data)) 

# Accessing elements of Tuple using index.
print("First Element of Tuple is : ", data[0]) 

# Accessing all elements of Tuple using loop.
print("All Elements of Tuple are : ")
for element in data:
    print(element,end=" ") 
print() 

# Tuple Functions:
# count() function is used to count occurrence of an element in Tuple.
print("Count of 'dev' in Tuple is : ", data.count("dev"))
# index() function is used to find index of first occurrence of an element in Tuple.
print("Index of 'rajgor' in Tuple is : ", data.index("rajgor"))
