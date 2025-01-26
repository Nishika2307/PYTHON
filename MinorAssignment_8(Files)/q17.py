'''
Create a robust program to read user input and write it into a file, handling invalid inputs gracefull
'''
#q17
filename = "user_input.txt"

while True:
    user_input = input("Enter something to write into the file: ").strip()

    if user_input:
        try:
            with open(filename, 'a') as file:
                file.write(user_input + "\n")
            print("Data written successfully.")
            break  # Exit the loop after writing the input
        except Exception as e:
            print(f"Error writing to file: {e}")
    else:
        print("Input cannot be empty. Please try again.")