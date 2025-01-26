'''
Given a string s and index i, write a python program to delete the ith value from s
'''
# Input string and index from the user
str_input = input("Enter string: ")
i = int(input("Enter index: "))

# Remove the character at the i-th index using slicing
if 0 <= i < len(str_input):
    str_input = str_input[:i] + str_input[i+1:]

# Print the updated string
print("Updated string:", str_input)

'''
Enter string: Nishika
Enter index: 2
Updated string: Nihika
'''