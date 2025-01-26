'''
Write a function to print all prime numbers between 1 and 100.
'''
def prime(a):
    for i in range(2,a):
        if(a%i==0):
            return False
    return True

def printPrime(a,b):
    for i in range(a,b):
        if prime(i)==True:
            print(i,end=",")

a=int(input("enter start limit : "))
b=int(input("enter end limit : "))
printPrime(a,b)


'''
enter start limit : 1
enter end limit : 100
1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,
'''