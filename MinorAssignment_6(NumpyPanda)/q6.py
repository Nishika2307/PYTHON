import numpy as np
arr=np.reshape(np.arange(0,6),(2,3))
arr=arr*2
print(arr)
flatten_array=arr.reshape(-1)
print("Flattened array",flatten_array)
print("Original ",arr)
raveled_array=arr.ravel()
print("Flattened using ravel",raveled_array)
print("Original",arr)

'''
[[ 0  2  4]
 [ 6  8 10]]
Flattened array [ 0  2  4  6  8 10]
Original  [[ 0  2  4]
 [ 6  8 10]]
Flattened using ravel [ 0  2  4  6  8 10]
Original [[ 0  2  4]
 [ 6  8 10]]'''
 