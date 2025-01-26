'''
Write a function to check if a string is an Anagram of another string. (An anagram is a word or phrase
formed by rearranging the letters of a different word or phrase, typically using all the original letters
exactly once, e.g. tom marvolo riddle⇝ i am lord voldemort)
'''

''' An anagram requires that both strings contain the same characters with the same frequencies, but they can be in any order.'''

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
Enter the first string: tom marvolo riddle
Enter the second string: i am lord voldemort
Anagram: True

Enter the first string: jskdkam
Enter the second string: sngnkmla
Anagram: False
'''
