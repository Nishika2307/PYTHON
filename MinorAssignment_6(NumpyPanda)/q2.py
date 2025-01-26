import numpy as np

# Create a 2x2 numpy array with values from 0 to 3
arr= np.reshape(np.arange(0, 4),(2, 2))
print(arr)
# Element-wise operations
print(arr*3)  # Multiply each element by 3
print(arr+7)  # Add 7 to each element
print(arr*2)  # Multiply each element by 2

'''
[[0 1]
 [2 3]]
[[0 3]
 [6 9]]
[[ 7  8]
 [ 9 10]]
[[0 2]
 [4 6]]'''
 