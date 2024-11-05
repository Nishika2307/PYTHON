n=int(input("Enter a number :"))
fact=1
i=1
while(fact<=n):
    fact=fact*i
    if(fact==n):
        print(i,"! =",n)
        break
    i+=1
if(fact>n):
    print("not",i)
    
'''
Enter a number :120
5 ! = 120
'''    