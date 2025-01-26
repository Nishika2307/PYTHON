'''
Define a function to check if a given string is a palindrome. Example: madam ⟲ madam, racecar ⟲
racecar.'''

'''
def reversing(str):
    rev = ""
    for i in range(len(str) - 1, -1, -1):
        rev += str[i]  
    return rev
'''
def reversing(str):
    return str[::-1]
# Get user input
s = input("Enter a string: ")
rev = reversing(s)
if(rev==s):
    print(f"Pallindrome String : {s} ")
else:
    print(f"Not Pallindrome String : {s} ")


''''
Enter a string: madam
Pallindrome String : madam
Enter a string: abcd
Not Pallindrome String : abcd
'''