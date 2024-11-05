n=int(input("enter the Limit : "))
sum=0
for i in range(0,n):
    if(i%2!=0):
        sum-=2*i+1
    else:
        sum+=2*i+1


print("Sum : ",sum)

'''
enter the Limit : 3
Sum :  3
'''