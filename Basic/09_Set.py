# Set is collection of non-repetitive elements.
# Sets are mutable and unordered (not support indexing).

s = set()
print("Empty Set : ", s)
print("Data Type of s is : ", type(s))

data = {1, 2, 'Dev', 3, 4, 5, 5, 6, 7, 8, 8}
print("Data Set : ", data)

# Set Functions:

# add() function is used to add an element to the Set.
data.add(9)
print("Set after adding 9 : ", data)

# remove() function is used to remove an element from the Set.
data.remove(3)
print("Set after removing 3 : ", data)

# discard() function is used to remove an element from the Set if it is present.
data.discard(10)  # No error if 10 is not present   
print("Set after discarding 10 : ", data)

# pop() function is used to remove and return an arbitrary element from the Set.
removed_element = data.pop()
print("Removed Element using pop() : ", removed_element)
print("Set after popping an element : ", data)

# clear() function is used to remove all elements from the Set.
data.clear()
print("Set after clearing all elements : ", data)

# union() function is used to return a new Set that is the union of two Sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union of set1 and set2 : ", union_set)

# intersection() function is used to return a new Set that is the intersection of two Sets.
intersection_set = set1.intersection(set2)  
print("Intersection of set1 and set2 : ", intersection_set)