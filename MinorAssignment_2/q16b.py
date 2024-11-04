import math
def fact(a):
    if(a==1):
      return 1
    else:
      return a*fact(a-1)

n=int(input("enter the limit of the series:"))
x=int(input("enter the value of x:"))
i=1
sum=1
while(i<n):
    sum+=math.pow(x,i)/fact(i)
    i+=1

print("Sum : ",sum)

'''
o/p

'''