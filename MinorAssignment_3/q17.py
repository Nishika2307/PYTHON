'''
Create a function that takes a string and returns a new string where all the vowels are removed.'''

def remVowel(s):
    vowels = "aeiouAEIOU"  # Consider both lowercase and uppercase vowels
    result = ""
    
    for char in s:
        if char not in vowels:
            result += char  # Add the character to result if it's not a vowel
    
    return result

str=input("Enter a String : ")
res=remVowel(str)
print("String after removal of vowel" ,res)

'''
Enter a String : Python
String after removal of vowel Pythn
'''