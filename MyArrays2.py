import numpy as np
import random

grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])

# each row represents a Student
# each column represents a Test

"""
a = grades.sum()
b = grades.min()
c = grades.max()
d = grades.mean()
e = grades.std()
f = grades.var()

g = grades.mean(axis=0)
# axis 0 looks at the first element in each row and averages them here
# axis 1 looks at the entire row (and here averages them)
print("Average of each test", g)

h = grades.mean(axis=1)
print("Average of each student", h)

numbers = np.array([1, 4, 9, 16, 25, 36])
sqrt = np.sqrt(numbers)
print(sqrt)

numbers2 = np.arange(1, 7) * 10

np_add = np.add(numbers, numbers2)

print(np_add)

np_multiply = np.multiply(numbers2, 5)

numbers3 = numbers2.reshape(2, 3)

numbers4 = np.array([2, 4, 6])

np_multiply2 = np.multiply(numbers3, numbers4)
print(np_multiply2)
# works bc the number of columns match up


# Indexing and Slicing

grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])

# to select a single element
a = grades[0, 1]  # (first row, second column)
print(a)

# to select a single row
b = grades[1]
print(b)

# to select multiple sequential rows (remember upper limit not included)
c = grades[0:2]
print(c)

# to select non-sequential rows
d = grades[[1, 3]]
print(d)

# all rows in first column (practical: gets test1 for all students)
e = grades[:, 0]
print(e)

# to get test 1 and 3 for all students
f = grades[:, [0, 2]]
print(f)
"""

"""
# Class Exercise
grades = np.random.randint(60, 101, 12).reshape(3, 4)
print(grades)

avg_all = grades.mean()
print(avg_all)
avg_test = grades.mean(axis=0)
print(avg_test)
avg_student = grades.mean(axis=1)
print(avg_student)
"""

"""

# shallow copies (view)
numbers = np.arange(1, 6)
print(numbers)
numbers2 = numbers.view()
print(numbers2)

numbers[1] *= 10  # manipulating numbers also manipulates numbers2 here

print(numbers2)

# slice views
numbers2 = numbers2[0:3]

numbers[1] *= 20
print(numbers2)


# Deep copies
# The array method copt returns a new array object with a deep copy of the original array
numbers = np.arange(1, 6)
numbers2 = numbers.copy()

numbers[1] *= 10  # manipulating numbers does not manipulate numbers2 here

print(numbers)
print(numbers2)
"""

# ----------
# The method reshape returns a view (shallow copy) or the original but resize does (deep copy)

grades = np.array([[87, 96, 70], [100, 87, 90]])

a = grades.reshape(1, 6)
print(grades)
print(a)

b = grades.resize(1, 6)

print(grades)
print(b)

# produces a deep copy into one dimensional array
flattened = grades.flatten()

# produces a shallow copy into one dimensional array
raveled = grades.ravel()

raveled[0] = 100

print(grades)

raveled[5] = 99

print(grades)

# Transpose the columns and rows
t = grades.T

print(t)

print(grades)


grades = np.array([[87, 96, 70], [100, 87, 90]])

grades2 = np.array([[87, 96, 70], [100, 87, 90]])

# adds more columns
h_grades = np.hstack((grades, grades2))

print(h_grades)

# adds more rows
v_grades = np.vstack((grades, grades2))

print(v_grades)