import pandas as pd
data = {
    'Column1': [1, 2, 3, 4],
    'Column2': [5, 6, 7, 8]
}
df = pd.DataFrame(data)
series = df['Column1']
print(series)

'''
0    1
1    2
2    3
3    4
Name: Column1, dtype: int64
'''