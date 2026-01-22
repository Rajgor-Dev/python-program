# Dictionary is a collection of key-value pairs.
# Dictionaries are mutable and unordered.
# Keys in a dictionary must be unique and immutable (e.g., strings, numbers, tuples).
# Values can be of any data type.

data = {"name": "dev", "surname": "rajgor", "age": 25, "height": 5.9, 
        "marks": {"php": 85, "python": 90}, "is_student": True}
print("Data Dictionary : ", data)
print("Data Type of data is : ", type(data))

# Accessing elements of Dictionary using key.
print("Name in Dictionary is : ", data["name"])

# Accessing all keys of Dictionary.
for key in data.keys():
    print("Key :", key)
print()
#Accessing all values of Dictionary.
for value in data.values():
    print("Value :", value)
print()
# Accessing all elements of Dictionary using loop.
print("All Elements of Dictionary are : ")
for key, value in data.items():
    print(key, ":", value)
print()

# Dictionary Functions:
# get() function is used to get value of a key in Dictionary.
age = data.get("age")
print("Age from Dictionary using get() : ", age)

# keys() function is used to get all keys of Dictionary.
keys = data.keys()
print("Keys in Dictionary using keys() : ", keys)

# values() function is used to get all values of Dictionary.
values = data.values()
print("Values in Dictionary using values() : ", values)

# items() function is used to get all key-value pairs of Dictionary.
items = data.items()
print("Items in Dictionary using items() : ", items,type(items))

# update() function is used to update value of a key in Dictionary.
data.update({"age": 26})
print("Dictionary after updating age : ", data)

# pop() function is used to remove a key-value pair from Dictionary.
removed_value = data.pop("is_student")
print("Removed Value using pop() : ", removed_value)
print("Dictionary after popping is_student : ", data)

# clear() function is used to remove all elements from Dictionary.
data.clear()
print("Dictionary after clearing all elements : ", data)