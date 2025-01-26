'''
Write a function to calculate the factorial of a number using a loop.
'''

def fact(num):
    if num==0:
        return 1
    else:
        return num*fact(num-1)
    
a=int(input("Enter a number : "))
print("factorial :",fact(a))

'''
Enter a number : 5
factorial : 120
'''
