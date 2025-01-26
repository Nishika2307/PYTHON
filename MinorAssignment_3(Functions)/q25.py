'''
Write a function to check if two numbers are coprime.
co-prime:hcf is 1 or check if both nos are prime
'''

def gcd(a, b):
    # Use the Euclidean algorithm to find the GCD
    while b != 0:
        a, b = b, a % b
    return a

def prime(a):
    for i in range(2,a):
        if(a%i==0):
            return False
    return True

def printPrime(a,b):
    for i in range(a,b):
        if prime(i)==True:
            print(i,end=",")

num1=int(input("Enter 1st number : "))
num2=int(input("Enter 2nd number : "))
res=gcd(num1,num2)
if(res==1 or printPrime(num1,num2)):
    print(f"{num1} and {num2} are coprime")
else:
    print(f"{num1} and {num2} are not  coprime")
    
'''
Enter 1st number : 15
Enter 2nd number : 8
15 and 8 are coprime
Enter 1st number : 4
Enter 2nd number : 6
5,4 and 6 are not  coprime
'''