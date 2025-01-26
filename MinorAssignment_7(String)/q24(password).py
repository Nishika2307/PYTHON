'''
Use regular expressions to validate secure passwords. Passwords must have a minimum of 8 characters and contain at 
least one each from uppercase characters, lowercase characters, digits, and punctuation characters, such as characters in ’!@#$%&∗?
′
.
'''

import re
def validate_password(password):
    # Define the regex pattern
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%&*?]).{8,}$"
    
    # Check if the password matches the pattern
    if re.match(pattern, password):
        return "Password is valid."
    else:
        return "Password is invalid."

# Input password from the user
password = input("Enter a password: ")

# Validate the password
print(validate_password(password))

'''
Enter a password: Passw0rd!
Password is valid.'''