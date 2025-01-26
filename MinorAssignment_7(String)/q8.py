'''
Implement a program to check if a string is a valid URL.

'''
def is_valid_url(url):
    # Check if the URL starts with 'http://' or 'https://'
    if url.startswith(('http://', 'https://')):
        # Check if there is at least one dot in the remaining part of the URL (after 'http:// or 'https://')
        if '.' in url[7:]:
            return True
    return False

# Example usage
input_url = input("Enter a URL: ")
if is_valid_url(input_url):
    print(f'"{input_url}" is a valid URL.')
else:
    print(f'"{input_url}" is not a valid URL.')
    
'''
Enter a URL: http://fbwbqb.com
"http://fbwbqb.com" is a valid URL.
'''    