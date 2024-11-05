'''
Create a function that returns the nth number in the Fibonacci sequence.'''
def Fibo(a,b,pos):
    if pos==0:
        return b
    else:
       return Fibo(b,a+b,pos-1)

pos=int(input("Enter the position : "))
print(Fibo(0,1,pos-2))