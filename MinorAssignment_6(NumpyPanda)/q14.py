import numpy as np
random_array = np.random.randint(0, 100, (5, 5)) # 0 (inclusive) and 100 (exclusive).
print("Array:\n", random_array)
counts = np.bincount(random_array.flatten())
print("Counts:\n",counts)
'''
Array:
 [[ 5 80 99 12  4]
 [92 22 88 85 62]
 [79 67 48 73 54]
 [45  5  5 94 28]
 [ 8 17 33 98 51]]
Counts:
 [0 0 0 0 1 3 0 0 1 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 1 0 0 0
 0 0 0 0 0 0 0 0 1 0 0 1 0 0 1 0 0 1 0 0 0 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 1
 0 0 0 0 0 1 1 0 0 0 0 1 0 0 1 0 0 0 1 0 1 0 0 0 1 1]
 '''
