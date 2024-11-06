#Write a function that replaces all vowels in a string with the character ”*”.

def repVowel(s):
    vowels = "aeiouAEIOU"  # Consider both lowercase and uppercase vowels
    result = ""
    
    for char in s:
        if char not in vowels:
            result += char  # Add the character to result if it's not a vowel
        else:
            result+="*"
    
    return result

s=input("Enter a string : ")
print(repVowel(s))

'''
Enter a string : an apple
*n *ppl*
'''