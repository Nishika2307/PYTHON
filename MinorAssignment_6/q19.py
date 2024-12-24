import pandas as pd

# Convert lists to Series
s1 = pd.Series([1, 2, 3, 4, 2])
s2 = pd.Series([3, 4, 5, 6])

# Find elements in s1 not in s2
result = s1[~s1.isin(s2)]
print(result)
'''
0    1
1    2
4    2
dtype: int64
'''