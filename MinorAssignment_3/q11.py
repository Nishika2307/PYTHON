'''
Create a function that determines whether a string can be rearranged to form a palindrome.
'''
from collections import Counter
def can_rearrange_to_palindrome(s):
    # Count frequency of each character in the string
    freq = Counter(s)
    
    # Count how many characters have an odd frequency
    odd_count = 0
    for count in freq.values():
        if count % 2 != 0:
           odd_count += 1
    # For a string to be rearranged into a palindrome:
    # There can be at most one character with an odd frequency.
    return odd_count

# Test cases
str=input("Enter the string : ")
if(can_rearrange_to_palindrome(str)<=1):
    print("True")
else:
    print("False")

'''
Enter the string : hello
False
Enter the string : civic
True

'''
