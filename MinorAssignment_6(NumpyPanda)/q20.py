import pandas as pd

s = pd.Series([1, 1, 3, 7, 88, 12, 88, 23, 3, 1, 9, 0])
# Find index of first occurrence of smallest and largest value
min_index = s.idxmin()
max_index = s.idxmax()
print(f"Index of smallest value: {min_index}")
print(f"Index of largest value: {max_index}")

'''

Index of smallest value: 11
Index of largest value: 4
'''