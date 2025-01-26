'''
Create a function that returns the nth number in the Fibonacci sequence
0,1,1,2,3,5,8,13'''
def Fibo(a,b,pos):
    if pos==0:
        return b
    else:
       return Fibo(b,a+b,pos-1)

pos=int(input("Enter the position : "))
print(Fibo(0,1,pos-2))

'''
Enter the position : 6
5
'''