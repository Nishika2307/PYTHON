'''
Write a function to check if a given number is a perfect number. (A number is called a perfect number
if it is equal to the sum of its real divisors, e.g., 6=1+2+3, 28=1+2+4+7+14).
'''

def perfect(n,sum):
    for i in range(1,n):
        if(n%i==0):
            sum+=i
    return sum
            
 
n=int(input("Enter a number : "))
if(perfect(n,0) == n):
  print("yes perfect:",n)
else:
  print("not perfect:",n)
  
  
'''
Enter a number : 6
yes perfect: 6

Enter a number : 56
not perfect: 56
'''
