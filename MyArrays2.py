import numpy as np

grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])

# each row represents a Student
# each column represents a Test


a = grades.sum()
b = grades.min()
c = grades.max()
d = grades.mean()
e = grades.std()
f = grades.var()

g = grades.mean(axis=0)
# axis 0 looks at the first element in each row and averages them here
# axis 1 looks at the entire row (and here averages them)
print(g)
