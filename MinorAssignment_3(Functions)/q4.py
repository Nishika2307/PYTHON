'''
Write a function that takes a string as input and returns the reversed string.'''

'''def reversing(str):
    rev = ""
    for i in range(len(str) - 1, -1, -1):
        rev += str[i]  # Append the character at the reversed index
    return rev
    '''
def reversing(str):
    return str[::-1]    

# Get user input
s = input("Enter a string: ")
rev = reversing(s)
print(f"String after reversing : {rev}")

'''
o/p
Enter a string: nishi
String after reversing : ihsin
'''

        
        