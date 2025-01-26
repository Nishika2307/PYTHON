'''
Write a python program to check if a string is symmetric or asymmetric'''
# Input from the user
str_input = input("Enter a string: ")

# Check if the string is symmetric (palindrome)
if str_input == str_input[::-1]:
    print("The string is symmetric.")
else:
    print("The string is asymmetric.")

'''
Enter a string: madam
The string is symmetric.
'''