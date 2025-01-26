'''
25. Use regular expressions and the findall function to count the number of digits, non-digit characters,
whitespace characters and words in a string.'''

import re

def count_patterns(text):
    # Count digits
    digits = len(re.findall(r'\d', text))
    
    # Count non-digit characters
    non_digits = len(re.findall(r'\D', text))
    
    # Count whitespace characters
    whitespaces = len(re.findall(r'\s', text))
    
    # Count words
    words = len(re.findall(r'\b\w+\b', text))
    
    # Print results
    print(f"Number of digits: {digits}")
    print(f"Number of non-digits: {non_digits}")
    print(f"Number of whitespace characters: {whitespaces}")
    print(f"Number of words: {words}")

# Input from the user
text = input("Enter a string: ")

# Count the patterns
count_patterns(text)

'''
Enter a string: nihhin 44n2n ndn87
Number of digits: 5
Number of non-digits: 13
Number of whitespace characters: 2
Number of words: 3
'''