import numpy as np
arr=np.reshape(np.arange(1,17),(4,4))
print("Original ")
print(arr)
arr[[0,1]]=arr[[1,0]] #swapping first 2 rows
print("Swapping first 2 rows ")
print(arr)
arr[:,[0,1]]=arr[:,[1,0]]
print("Swapping first 2 columns")
print(arr)

'''
Original 
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]
 [13 14 15 16]]
Swapping first 2 rows
[[ 5  6  7  8]
 [ 1  2  3  4]
 [ 9 10 11 12]
 [13 14 15 16]]
Swapping first 2 columns
[[ 6  5  7  8]
 [ 2  1  3  4]
 [10  9 11 12]
 [14 13 15 16]]
'''