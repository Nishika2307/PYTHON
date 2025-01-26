import pandas as pd
series_a = pd.Series([7, 11, 13, 17])
print(series_a)
#b
series_b = pd.Series([100.0] * 5)
print(series_b)
#c
import numpy as np

series_c = pd.Series(np.random.randint(0, 100, size=20))
print(series_c.describe())
#d
temperatures = pd.Series([98.6, 98.9, 100.2, 97.9], index=['Julie', 'Charlie', 'Sam', 'Andrea'])
print(temperatures)
 #e
temp_dict = {'Julie': 98.6, 'Charlie': 98.9, 'Sam': 100.2, 'Andrea': 97.9}
series_d = pd.Series(temp_dict)
print(series_d)

'''
0     7
1    11
2    13
3    17
dtype: int64
0    100.0
1    100.0
2    100.0
3    100.0
4    100.0
dtype: float64
count    20.000000
mean     46.350000
std      26.053134
min       3.000000
25%      28.750000
50%      48.500000
75%      62.500000
max      91.000000
dtype: float64
Julie       98.6
Charlie     98.9
Sam        100.2
Andrea      97.9
dtype: float64
Julie       98.6
Charlie     98.9
Sam        100.2
Andrea      97.9
dtype: float64

'''