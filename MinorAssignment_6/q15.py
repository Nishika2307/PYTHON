import numpy as np
def median(arr):
    return np.median(arr)

def mode(arr):
    values, counts = np.unique(arr, return_counts=True)
    m = counts.argmax()
    return values[m]

# Test the functions
arr1 = np.random.randint(0, 10, (5, 5))
arr2 = np.random.randint(0, 10, (3, 3))
arr3 = np.random.randint(0, 10, (7, 7))
print("arr1 : \n" ,arr1)
print("arr2 : \n" ,arr2)
print("arr3 : \n" ,arr3)

print("Median of arr1:\n", median(arr1))
print("Mode of arr1:\n", mode(arr1))

print("Median of arr2:\n", median(arr2))
print("Mode of arr2:\n", mode(arr2))

print("Median of arr3:\n", median(arr3))
print("Mode of arr3:\n", mode(arr3))

'''
arr1 : 
 [[8 2 2 8 2]
 [8 7 0 1 8]
 [2 0 6 6 1]
 [7 5 8 4 7]
 [3 5 2 3 8]]
arr2 :
 [[9 4 2]
 [1 9 9]
 [6 3 4]]
arr3 :
 [[8 2 4 1 8 8 3]
 [8 4 5 9 4 5 8]
 [4 3 6 5 2 5 8]
 [9 6 5 3 1 7 2]
 [3 4 3 2 3 3 2]
 [7 6 7 2 7 8 1]
 [9 3 2 4 0 8 6]]
Median of arr1:
 5.0
Mode of arr1:
 8
Median of arr2:
 4.0
Mode of arr2:
 9
Median of arr3:
 4.0
Mode of arr3:
 3


'''