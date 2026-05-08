name = input("Enter Your Name : ") # Input Function is used to take input from user.
print("Hello", name  , "DataType =", type(name)) # Input function always takes input as String.

# Follow is String Functions:

# len() function is used to find length of String.
print("Length of Name is : ", len(name)) 

# upper() function is used to convert string to Upper Case.
print("Upper Case Name is : ", name.upper())

# lower() function is used to convert string to Lower Case.
print("Lower Case Name is : ", name.lower()) 

# title() function is used to convert first character of each word to Upper Case.
print("Title Case Name is : ", name.title()) 

# capitalize() function is used to convert first character of string to Upper Case.
print("Capitalized Name is : ", name.capitalize())

# count() function is used to count occurrence of a substring in string.
substring = input("Enter Substring to Count in Name : ")    
print("Count of '", substring , "' in Name is : ", name.count(substring)) 

# find() function is used to find index of first occurrence of a substring in string.   
print("Index of first occurrence of '", substring , "' in Name is : ", name.find(substring)) 

# replace() function is used to replace a substring with another substring in string.       
new_substring = input("Enter New Substring to Replace in Name : ")    
print("Name after replacing '", substring , "' with '", new_substring , "' is : ", name.replace(substring, new_substring))


'''
String Slicing in Python
String Slicing is used to get a substring from a given string.
Syntax : string_name[start_index : end_index : step]
'''
print("First Character of Name is : ", name[0]) 
print("Last Character of Name is : ", name[-1]) 
print("First 3 Characters of Name is : ", name[0:3]) 
print("Characters from index 2 to 5 is : ", name[2:6])
print("Characters from index 0 to 6 with step 2 is : ", name[0:7:2])
print("Reversed Name is : ", name[::-1])
'''
Sring Slicing is based on index of characters in the string. Like Name is 
 0123456789 it is positive indexing
"DEV RAJGOR" 
-10-9-8-7-6-5-4-3-2-1 it is negative indexing
 ''' 