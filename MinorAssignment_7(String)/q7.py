'''
 Write a Python program that checks if a string is a ”rotational palindrome.” A rotational palindrome
is a string that can be rearranged cyclically to form a palindrome
'''

s=input("Enter a string: ")
f=0
for i in range(len(s)):
    rotated = s[i:] + s[:i]  # Generate a rotated string
    if rotated == rotated[::-1]:  # Check if it's a palindrome
           f=1
if(f==1):
    print(f'"{s}" is a rotational palindrome.')
else:
    print(f'"{s}" is not a rotational palindrome.')
        
'''
Enter a string: aab
"aab" is a rotational palindrome.
'''    
    
