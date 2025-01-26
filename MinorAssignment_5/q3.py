'''
Write a program to take a user-input dictionary and print the sum of the values.'''
# Taking input for the dictionary
d = eval(input("Enter a dictionary (e.g., {'key': value}): "))

# Calculating the sum of the values in the dictionary
sum_values = sum(d.values())

# Displaying the sum of the values
print(f"The sum of the values is: {sum_values}")

'''
Enter a dictionary (e.g., {'key': value}): {"Nishi " :89 ,"Ishi" :76 ,"Mini" :97 }
The sum of the values is: 262'''
