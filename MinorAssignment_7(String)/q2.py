'''
Write a function that takes two strings and returns True if they are anagrams and False otherwise. A
pair of strings is anagram if the letters in one word can be arranged to form the second one.
'''

def is_anagram(s1, s2):
    # Remove spaces and convert to lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    # Check if sorted characters of both strings are the same
    return sorted(s1) == sorted(s2)

# Test the function
ss1 = input("Enter the first string: ")
ss2 = input("Enter the second string: ")
print("Anagram:", is_anagram(ss1, ss2))

'''
Enter the first string: Listen
Enter the second string: Silent
Anagram: True'''