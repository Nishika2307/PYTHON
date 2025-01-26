'''Write a Python program that randomly fills in 0s and 1s into a 4-by-4 matrix, prints the matrix, and
finds the first row and column with the most 1s. Here is a sample run of the program:
0011
0011
1101
1010
The largest row index: 2
The largest column index: 2
'''

import random
M=int(input("No of rows :"))
N=int(input("No of columns :"))
res=list()
innerl=list()
for i in range(M):
    
    for j in range(N):
        a=random.randint(0,1)
        innerl.append(a)
    innerl2=innerl.copy()#list(inner1);inner[:]    <--as innerl is mutable there =fire create copy before deleting enlse res will be nothing
    res.append(innerl2)
    innerl.clear()

mr=0
mc=0
r,c=0,0
for i in range(M):
    print(res[i])
for i in range(M):
    if(res[i].count(1)>mr):
        r=i
        mr=res[i].count(1)



