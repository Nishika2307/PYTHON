'''
Check whether a sentence contains more than one space between words. If so, remove the extra
spaces and display the results. For example, ’Hello World’ should become ’Hello World’.

'''
# Input sentence from the user
str_input = input("Enter string: ")
str=str_input.split()
# Replace multiple spaces with a single space
result =' '.join(str)

# Display the result
print("Modified string:", result)

'''
Enter string:  Hello   World    how  are you   ?
Modified string: Hello World how are you ?
'''