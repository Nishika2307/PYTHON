'''Write a Python function to check whether an alphabet is a vowel or consonant.'''

def Vowel(a):
    a=a.lower()
    vowels="aeiou"
    if a in vowels:
        return True
    return False

l=input("Enter a letter : ")
if Vowel(l):
    print("The character is vowel:",l)
else:
    print("The character is consonent:",l)
    
'''
Enter a letter : b
The character is consonent: b
Enter a letter : e
The character is vowel: e
'''