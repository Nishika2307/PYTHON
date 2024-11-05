'''Write a Python function to check whether an alphabet is a vowel or consonant.'''

def Vowel(a):
    a=a.lower()
    if(a =="a" or a=="e" or a =="i" or a=="i" or a=="o" or a=="u"):
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