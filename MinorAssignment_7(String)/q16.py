'''
Write a code to extract unique characters of a string in sorted order.
'''
# Input string from the user
str_input = input("Enter a string: ")

# Extract unique characters using a set and then sort them
unique_sorted_chars = sorted(set(str_input))

# Print the unique characters in sorted order
print("Unique characters in sorted order:", "".join(unique_sorted_chars))

'''
Enter a string: banana
Unique characters in sorted order: abn'''
