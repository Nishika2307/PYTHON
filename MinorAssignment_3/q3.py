'''
Write a Python function to add the squares of the even numbers between 1 and 50 (both included).'''

def squares(num):
    return num*num
  
total=0
for i in range(2,51,2):
    total+=squares(i)
print("Squares of even numbers :" ,total)
    
'''
Squares of even numbers : 22100
'''
