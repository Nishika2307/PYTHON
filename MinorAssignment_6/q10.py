import numpy as np
arr=np.reshape(np.arange(1,16),(3,5))
print(arr)
print("Second row")
print(arr[1:2])
print("Column 5")
print(arr[:,4])
print("row 0 and row 1")
print(arr[0:2])
print("column 2 to 4")
print(arr[:,2:])
print("Element in row 1 column 4")
print(arr[1,4])
print(arr[0:2,0:5:2])

'''
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]]
Second row
[ 6  7  8  9 10]
Column 5
[ 5 10 15]
row 0 and row 1
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]]
column 2 to 4
[[ 3  4  5]
 [ 8  9 10]
 [13 14 15]]
Element in row 1 column 4
10
[[ 1  3  5]
 [ 6  8 10]]

'''