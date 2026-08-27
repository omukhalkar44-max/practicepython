import numpy as np

# Create float array
arr = np.array([10.5, 20.75, 30.25, 40.90, 50.10], dtype=float)

print("Array:", arr)
print("Data Type:", arr.dtype)

# Mathematical operations
print("Sum:", np.sum(arr))
print("Average:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))


##############################
import numpy as np

marks = np.array([85.5, 39.5, 72.0, 28.5, 91.5, 45.0, 33.5], dtype=float)

print("Marks:")
print(marks)

# Boolean condition
passed = marks >= 40

print("\nBoolean Result:")
print(passed)

# Get passing marks
print("\nPassing Marks:")
print(marks[passed])

# Get failing marks
print("\nFailing Marks:")
print(marks[~passed])

# Number of students
print("\nTotal Students:", len(marks))

# Number of passed students
print("Passed Students:", np.sum(passed))

# Number of failed students
print("Failed Students:", np.sum(~passed))

# Passing percentage
percentage = (np.sum(passed) / len(marks)) * 100

print("Passing Percentage:", percentage, "%")

# Highest passing mark
print("Highest Mark:", np.max(marks))

# Average marks
print("Average Marks:", np.mean(marks))
