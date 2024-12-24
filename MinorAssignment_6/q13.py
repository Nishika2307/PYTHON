import numpy as np
k=np.array(['_','*'])
res=np.tile(k,(5,5))
print(res)

''''
[['_' '*' '_' '*' '_' '*' '_' '*' '_' '*']
 ['_' '*' '_' '*' '_' '*' '_' '*' '_' '*']
 ['_' '*' '_' '*' '_' '*' '_' '*' '_' '*']
 ['_' '*' '_' '*' '_' '*' '_' '*' '_' '*']
 ['_' '*' '_' '*' '_' '*' '_' '*' '_' '*']]

The np.tile() function is used to repeat the contents of the array. 
The argument (5, 5) means you want to tile the array k in a 5x5 pattern'''