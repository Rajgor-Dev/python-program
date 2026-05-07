# Python has built-in functions to handle file operations such as opening, reading, writing, and closing files.
"""
Functions to Handle Files:
open(): This function is used to open a file. 
read(): This function reads the content of a file.
readline(): This function reads a single line from a file.
readlines(): This function reads all the lines of a file and returns them as a list.
write(): This function writes data to a file.
close(): This function closes an opened file.

Modes of Opening a File:
r - Read mode (default): Opens a file for reading. 
w - Write mode: Opens a file for writing. If the file exists, it truncates the file. If it doesn't exist, it creates a new file.
a - Append mode: Opens a file for appending. If the file exists, it adds data to the end of the file. If it doesn't exist, it creates a new file.
rw - Read and Write mode: Opens a file for both reading and writing.
rb - Read Binary mode: Opens a file for reading in binary format.
rt - Read Text mode: Opens a file for reading in text format.
"""
f = open("example.txt", "w")  
f.write("Hello, World!\n")     
f.write("Welcome to file handling in Python.\n")
f.close()              

f = open("example.txt", "r") 
content = f.read()  
print(content)
f.close()

f = open("example.txt", "a")  
f.write("This line is appended.\n") 
f.close()

f = open("example.txt", "r") 
lines = f.readlines()   
for line in lines:
    print(line, end='')
f.close()          

