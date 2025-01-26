a=int(input("enter a number : "))
while(a<0):
    a=int(input("enter a number : "))
else:
    if(a%2==0):
        print("ans:",a*2)
    else:
        print("ans:",a**2)
    
    
'''
Output
enter a number : -9
enter a number : -5
enter a number : -3
enter a number : 2
ans: 4
'''    