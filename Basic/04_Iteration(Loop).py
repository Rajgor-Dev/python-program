'''
Iteration or Loop type as follows:
1. for loop
2. while loop
3. for-else loop
4. while-else loop
'''
# 1. for loop
print("For Loop Example Define First 5 odd numbers:")
for i in range(1,10,2):
    print( i, end=' ')
print()

# 2. while loop
print("While Loop Example:")    
count = 0
while count < 5:
    print("Count is:", count, end=' ')
    count += 1
print()
# 3. for-else loop
print("For-Else Loop Example:")
for i in range(5):
    print("Iteration:", i, end=' ')
else:
    print("Loop completed successfully.")
print()
# else block executes when the loop is not terminated by a break statement or 
# when the loop condition becomes false.
n = int(input("Enter a number to print its multiplication table in reverse order: "))
for i in range(10, 0, -1):
    print(f"{n} X {i} = {n*i}")