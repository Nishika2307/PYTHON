import numpy as np
arr=np.reshape(np.arange(2,19,2),(3,3))
print(arr)
arr1=np.reshape(np.arange(9,0,-1),(3,3))
print(arr1)
print(arr*arr1)
'''
[[ 2  4  6]
 [ 8 10 12]
 [14 16 18]]
[[9 8 7]
 [6 5 4]
 [3 2 1]]
 [[18 32 42]
 [48 50 48]
 [42 32 18]]
 
 
 '''
