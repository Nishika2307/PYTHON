import re
#q12
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Create and write to sample.txt
with open("sample.txt", "w") as f:
    f.write('''Hello, contact me at example1@example.com for more info. 
You can also reach me at test email@example.org or example1@example.com. 
Spam emails: spam@spammer.com, info@spammer.com, spam@spammer.com''')

# Extract emails and write to output.txt
with open("sample.txt", "r") as f:
    with open("output.txt", "w") as o1:
        k = f.read()
        for i in re.finditer(email_pattern, k):
            o1.write(i.group() + '\n')  # Write each email on a new line

# Read and display output.txt content
with open("output.txt") as o1:
    print("Extracted Emails from output.txt:")
    print(o1.read())  # Now this will show the contents of output.txt