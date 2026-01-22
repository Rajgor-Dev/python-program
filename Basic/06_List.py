# List are containers to store a set of values in a single variable with any data type.
# List are mutable i.e. we can change, add or remove elements from a list.

data = ["dev","rajgor",25,5.9,True] # Creating a List with multiple data types.
print("Data List : ", data) # Printing the List.
print("Data Type of data is : ", type(data)) # Printing the data type of List.

# Accessing elements of List using index.
print("First Element of List is : ", data[0]) # Accessing first element.

# Accessing all elements of List using loop.
print("All Elements of List are : ")
for element in data:
    print(element,end=" ") #Normal print provide new line so using end=" " to print in same line.
print()  # For new line after printing all elements.

# List Functions:
# sort() function is used to sort elements of List in ascending order.
numbers = [5, 2, 9, 1, 5, 6]
print("\nNumbers List before sorting : ", numbers)
numbers.sort() 
print("Numbers List after sorting : ", numbers)

# reverse() function is used to reverse elements of List.
numbers.reverse()  
print("Numbers List after reversing : ", numbers)

# append() function is used to add an element at the end of List.
numbers.append(10)
print("Numbers List after appending 10 : ", numbers)

# insert() function is used to add an element at a specific index of List.
numbers.insert(2, 15) # Inserting 15 at index 2
print("Numbers List after inserting 15 at index 2 : ", numbers)

# remove() function is used to remove an element from List.
numbers.remove(5) 
print("Numbers List after removing 5 : ", numbers)

# pop() function is used to remove and return an element from a specific index of List.
popped_element = numbers.pop(3) 
print("Popped Element at index 3 : ", popped_element)
print("Numbers List after popping element at index 3 : ", numbers)