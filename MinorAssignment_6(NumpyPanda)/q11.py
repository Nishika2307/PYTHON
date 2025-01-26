import numpy as np
array1=np.array([[0,1],[2,3]])
array2=np.array([[4,5],[6,7]])
array3=np.vstack((array1,array2))
print(array3)
array4=np.hstack((array1,array2))
print(array4)
array5=np.vstack((array4,array4))
print(array5)
array6=np.hstack((array5,array5))
print(array6)

'''
[[0 1]
 [2 3]
 [4 5]
 [6 7]]
[[0 1 4 5]
 [2 3 6 7]]
[[0 1 4 5]
 [2 3 6 7]
 [0 1 4 5]
 [2 3 6 7]]
[[0 1 4 5 0 1 4 5]
 [2 3 6 7 2 3 6 7]
 [0 1 4 5 0 1 4 5]
 [2 3 6 7 2 3 6 7]]'''
 