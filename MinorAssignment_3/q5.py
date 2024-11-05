'''
Write a function that takes a positive integer and returns the number of digits.'''

def counting(num):
    count=0
    while(num>0):
        count+=1
        num//=10
    return count

num=int(input("Enter a number : "))
c=counting(num)
print(f"No of digits in {num} is {c}")
        
'''
Enter a number : 1243
No of digits in 1243 is 4
'''