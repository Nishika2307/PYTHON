import numpy as np
array = np.random.randint(0, 10, (4, 4)) 
print(array)
sorted_array=np.sort(array, axis=0)
print(sorted_array)

'''
[[8 0 0 2]
 [4 0 5 0]
 [5 6 8 4]
 [9 5 5 3]]
[[4 0 0 0]
 [5 0 5 2]
 [8 5 5 3]
 [9 6 8 4]]'''