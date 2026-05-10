import numpy as np

print("1. ARRAY CREATION")
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

arr2 = np.array([[1, 2], [3, 4]])
print("2D Array:\n", arr2)

# 2. ARRAY ATTRIBUTES
print("\n2. ARRAY ATTRIBUTES")

print("Shape:", arr2.shape)
print("Dimensions:", arr2.ndim)
print("Data Type:", arr2.dtype)
print("Size:", arr2.size)

# 3. SPECIAL ARRAY CREATION
print("\n3. SPECIAL ARRAYS")

zeros = np.zeros((2, 3))
print("Zeros Array:\n", zeros)

ones = np.ones((2, 2))
print("Ones Array:\n", ones)

range_arr = np.arange(1, 11, 2)
print("Range Array:", range_arr)

# 4. MATHEMATICAL OPERATIONS
print("\n4. MATHEMATICAL OPERATIONS")

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("Addition:", np.add(a, b))
print("Subtraction:", np.subtract(a, b))
print("Multiplication:", np.multiply(a, b))
print("Division:", np.divide(a, b))

# 5. STATISTICAL FUNCTIONS
print("\n5. STATISTICAL FUNCTIONS")

data = np.array([10, 20, 30, 40, 50])

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Maximum:", np.max(data))
print("Minimum:", np.min(data))
print("Standard Deviation:", np.std(data))

# 6. RANDOM FUNCTIONS
print("\n6. RANDOM FUNCTIONS")

random_numbers = np.random.randint(1, 100, size=5)
print("Random Numbers:", random_numbers)

# 7. TRIGONOMETRIC FUNCTIONS
print("\n7. TRIGONOMETRIC FUNCTIONS")

angle = 0

print("Sin:", np.sin(angle))
print("Cos:", np.cos(angle))
print("Tan:", np.tan(angle))

# 8. LOGARITHMIC & EXPONENTIAL FUNCTIONS
print("\n8. LOGARITHMIC & EXPONENTIAL FUNCTIONS")

print("Log Value:", np.log(10))
print("Log10 Value:", np.log10(100))
print("Exponential Value:", np.exp(2))

# 9. SEARCHING & SORTING
print("\n9. SEARCHING & SORTING")

arr = np.array([50, 10, 40, 20, 30])

print("Original Array:", arr)
print("Sorted Array:", np.sort(arr))
print("Index of Maximum Value:", np.argmax(arr))

# 10. RESHAPING ARRAY
print("\n10. RESHAPING ARRAY")

numbers = np.arange(1, 13)

reshaped = numbers.reshape(3, 4)

print("Original Array:", numbers)
print("Reshaped Array:\n", reshaped)

# 11. MATRIX OPERATIONS
print("\n11. MATRIX OPERATIONS")

matrix1 = np.array([[1, 2],
                    [3, 4]])

matrix2 = np.array([[5, 6],
                    [7, 8]])

print("Matrix Multiplication:\n", np.dot(matrix1, matrix2))

# 12. BOOLEAN FILTERING
print("\n12. BOOLEAN FILTERING")

values = np.array([5, 12, 18, 7, 25])

filtered = values[values > 10]

print("Original Values:", values)
print("Values Greater Than 10:", filtered)
