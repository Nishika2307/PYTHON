'''
Write a Python function to find the first, second and third greatest digit in a number.
Sample Number: 6328
Expected Output: 8, 6, 3
'''

n=int(input("Enter a number : "))
Tmax,Smax,max=0,0,0
while(n!=0):
    el=n%10
    if (max<el):
        Tmax=Smax
        Smax=max
        max=el
    elif(el>Smax):
        Tmax=Smax
        Smax=el
    elif(el>Tmax):
        Tmax=el
    else:
        pass
    n=n//10
print("max:",max,"Second max:",Smax,"Third max:",Tmax)