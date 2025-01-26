'''
Write a Python program to print M-by-N list in the tabular format
'''
M=int(input("enter M : "))
N=int(input("enter N : "))
res=list()
innerl=list()
for i in range(M):
    
    for j in range(N):
        a=eval(input("enter a number"))
        innerl.append(a)
    innerl2=innerl.copy()#list(inner1);inner[:]<--as innerl is mutable there =fire create copy before deleting enlse res will be nothing
    res.append(innerl2)
    innerl.clear()
    
for i in range(M):
    print(res[i])
    
    
'''
enter M : 3
enter N : 2
enter a number1
enter a number3
enter a number4
enter a number1
enter a number2
enter a number1
[1, 3]
[4, 1]
[2, 1]'''