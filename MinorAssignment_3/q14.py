'''
Write a function to determine if a given number is an Armstrong number. (An Armstrong number is
a number that is equal to the sum of its digits, each raised to the power of the number of digits, e.g.,
153 = 13 + 53 + 33, 1634 = 14 + 64 + 34 + 44).'''
def count(n):
    if n==0:
     return 0
    return 1+count(n//10)

def armstrong(n,c):
  if(n==0):
   return 0
  else:
   return (n%10)**c+armstrong(n//10,c)

n=int(input("Enter a number : "))
if(n==armstrong(n,count(n))):
  print("yes armstrong:",n)
else:
  print("not armstrong:",n)
  
'''
o/p
Enter a number : 153
yes armstrong: 153
Enter a number : 123
not armstrong: 123
'''
  