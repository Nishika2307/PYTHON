import numpy as np
arr = np.array([6, 9, 5, 1, 7, 5, 1, 0, 1, 5, 5, 0, 8, 9, 0, 7, 0, 7, 6, 5, 1, 1, 9, 5, 3, 8, 7, 9, 6, 3, 4, 5, 9, 7, 2, 7, 0, 2, 2, 6])

# Find unique elements and their counts
unique,counts =np.unique(arr, return_counts=True)
print(unique)
print(counts)
# Get the maximum count
max_count = np.max(counts)
print("Frequency:", max_count)
# Find the elements with the maximum count
most_frequent = unique[counts == max_count]
print("Most Frequent Values:",most_frequent)
'''
[0 1 2 3 4 5 6 7 8 9]
[5 5 3 2 1 7 4 6 2 5]
Frequency: 7
Most Frequent Values: [5]'''
