'''
Write a Python program to print the substrings of a character having a particular frequency. For
’aabbbccccddddd’, you should print ’bbb’ if particular frequency is 3
'''

import re
# Input from the user
str_input = input("Enter string: ")
ch = input("Enter character: ")
fr = int(input("Enter frequency: "))

# Create a regex pattern to find substrings of 'ch' with the exact frequency 'fr'
pattern = f"{ch}{{{fr}}}"

# Find all matching substrings
matches = re.findall(pattern, str_input)

# Print the matches
for match in matches:
    print(match)

'''
Enter string: aabbbccccddddd
Enter character: b
Enter frequency: 3
bbb
'''