import numpy as np
import random
from random import randint

integers = np.array([1, 2, 3])

print(type(integers))


# LIST COMPREHENSION
# create a one-dimensional array from a list comprehension
# that produces even integers from 2 thorugh 20

integers = np.array([x for x in range(2, 21, 2)])
print(integers)

integers = np.array([[1, 2, 3], [4, 5, 6]])
print(integers)

floats = np.array([0.0, 0.1, 0.2, 0.3, 0.4])
print(floats)


a = integers.dtype
b = integers.ndim
c = integers.shape
d = integers.size

print()


for row in integers:
    print(row)
    for column in row:
        print(column, end=" ")


# runs all elements disregarding columns and rows
"""
for i in integers.flat:
    print(i)
"""

"""
# Create a 2 dimensional array of 5 ints each using the random module and list comprehension print out its dimension, shape, and size
a = np.array([[randint(1, 10) for x in range(5)], [randint(1, 10) for x in range(5)]])
print(a)
dimension = a.ndim
print("Dimension:", dimension)
shape = a.shape
print("Shape:", shape)
size = a.size
print("Size:", size)

# numpy version of that ^
b = np.array(np.random.randint(1, 10, size=(2, 5)))

print(b)
dimension = b.ndim
print("Dimension:", dimension)
shape = b.shape
print("Shape:", shape)
size = b.size
print("Size:", size)
"""


c = np.zeros(5)
d = np.ones(5)
e = np.ones((2, 4), dtype=int)
f = np.full((3, 5), 13)
g = np.arange(5)
h = np.arange(5, 10)
i = np.arange(10, 1, -2)


"""
print(
    np.linspace(0.0, 1.0, num=5)
)  # evenly spaced floating point numbers between the upper and lower limit specified
"""


"""
array1 = np.arange(1, 21)
# reshape method can change the dimension
array2 = array1.reshape(4, 5)  # (row, column)

print(array1, "\n", array2)
"""

"""
# large numbers
array3 = np.arange(1, 100001).reshape(4, 25000)

array4 = np.arange(1, 100001).reshape(100, 1000)

print(array3)
print(array4)
"""

# arithmetic operators
numbers = np.arange(1, 6)

numbers += 10

print(numbers)
print(numbers * 10)
print(numbers)

# multiplying integers by floating point arrays
# (result is a floating point array)
numbers2 = np.linspace(1.1, 5.5, 5)

print(numbers * numbers2)

print(numbers >= 13)
print(numbers2 < numbers)
print(numbers == numbers2)
