'''
Define a function that returns the sum of all the elements in a specified column in a matrix. Write a
Python program that reads a 3-by-4 matrix and displays the sum of each column. Here is a sample
run:
Enter a 3-by-4 matrix row by row:
1.5 2 3 4
5.5 6 7 8
9.5 1 3 1
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

    print("sum of",i,"row:",sum(res[i]))

for i in range(M):
    print(res[i])