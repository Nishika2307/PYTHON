import pandas as pd
#a
temp_dict = {
    'Maxine': [96.5, 98.2, 97.8],
    'James': [99.1, 98.3, 98.7],
    'Amanda': [97.8, 98.1, 98.5]
}
temperatures_df = pd.DataFrame(temp_dict)
print(temperatures_df)
print()

#b
temperatures_df = pd.DataFrame(temp_dict, index=['Morning','Afternoon','Evening'])
print(temperatures_df)
print()

#c
maxine_temps = temperatures_df['Maxine']
print(maxine_temps)

#d
morning_temps = temperatures_df.iloc[0]
print(morning_temps)

#e
morningevenings_temps = temperatures_df.iloc[0:2]
print(morningevenings_temps)

#f
amanda_maxine_temps = temperatures_df[['Amanda', 'Maxine']]
print(amanda_maxine_temps)

#g
specific_temps = temperatures_df.loc[['Morning', 'Afternoon'], ['Amanda', 'Maxine']]
print(specific_temps)

#h
temp_stats = temperatures_df.describe()
print(temp_stats)
  

#i
transposed_temps = temperatures_df.T
print(transposed_temps)

#j
sorted_temps = temperatures_df[sorted(temperatures_df.columns)]
print(sorted_temps)

'''

   Maxine  James  Amanda
0    96.5   99.1    97.8
1    98.2   98.3    98.1
2    97.8   98.7    98.5

           Maxine  James  Amanda
Morning      96.5   99.1    97.8
Afternoon    98.2   98.3    98.1
Evening      97.8   98.7    98.5

Morning      96.5
Afternoon    98.2
Evening      97.8
Name: Maxine, dtype: float64
Maxine    96.5
James     99.1
Amanda    97.8
Name: Morning, dtype: float64
           Maxine  James  Amanda
Morning      96.5   99.1    97.8
Afternoon    98.2   98.3    98.1
           Amanda  Maxine
Morning      97.8    96.5
Afternoon    98.1    98.2
Evening      98.5    97.8
           Amanda  Maxine
Morning      97.8    96.5
Afternoon    98.1    98.2
          Maxine  James     Amanda
count   3.000000    3.0   3.000000
mean   97.500000   98.7  98.133333
std     0.888819    0.4   0.351188
min    96.500000   98.3  97.800000
25%    97.150000   98.5  97.950000
50%    97.800000   98.7  98.100000
75%    98.000000   98.9  98.300000
max    98.200000   99.1  98.500000
        Morning  Afternoon  Evening
Maxine     96.5       98.2     97.8
James      99.1       98.3     98.7
Amanda     97.8       98.1     98.5
           Amanda  James  Maxine
Morning      97.8   99.1    96.5
Afternoon    98.1   98.3    98.2
Evening      98.5   98.7    97.8
'''