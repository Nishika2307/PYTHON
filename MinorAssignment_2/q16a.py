
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
while(i<=n):
    if(i%2==0):
        sum+=math.pow(x,2*i)/fact(2*i)
    else:
        sum-=math.pow(x,2*i)/fact(2*i)
    i+=1

print("Sum : ",sum)

'''
o/p
enter the limit of the series:3
enter the value of x:1
Sum :  0.5402777777777777
'''