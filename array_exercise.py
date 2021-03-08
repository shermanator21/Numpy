## Numpy Exercise
import numpy as np

## Step 1: Create a 4x3 array of all 2s
print(
    "-----------------------------------------------   STEP ONE   -----------------------------------------------"
)

twoArray = np.full((4, 3), 2)
print(twoArray)

## Step 2: Create a 3x4 array with a range from 0 to 110 where each number increases by 10
print(
    "-----------------------------------------------   STEP TWO   -----------------------------------------------"
)
tenArray = np.arange(0, 111, 10).reshape(3, 4)
print(tenArray)

## Step 3: Change the layout of the above array to be 4x3, store it in a new array
print(
    "-----------------------------------------------   STEP THREE   -----------------------------------------------"
)
newTenArray = tenArray.reshape(4, 3)
print(newTenArray)

print()

## Step 4: Multiply every elemnt of the above array by 3 and store the new values in a different array
print(
    "-----------------------------------------------   STEP FOUR   -----------------------------------------------"
)
newArray = newTenArray * 3
print(newArray)

## Step 5: Multiply your array from step one by your array from step 2
print(
    "-----------------------------------------------   STEP FIVE   -----------------------------------------------"
)

"""
print(twoArray * tenArray)
## This errored out... why?
# columns do matter (must be same). rows do not
print()
"""

## Step 6: Comment out your code from Step 5 and then multiply your array from step 1 by your array from step 3
print(
    "-----------------------------------------------   STEP SIX   -----------------------------------------------"
)
print(twoArray * newTenArray)
## this worked! why?
print()
