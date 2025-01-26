'''
 Solve the problem of dividing two numbers, handling invalid inputs like zero or non-numeric values.'''
 
try:
    a = int(input("Enter a number (numerator): "))
    b = int(input("Enter a number (denominator): "))
    
    # Perform the division
    result = a / b
    
except (ValueError, ZeroDivisionError) as e:
    # Handle invalid input or division by zero
    print("Error:", e)
else:
    # If no exception occurs, print the result
    print(f"The result of {a} divided by {b} is: {result}")

''''
Enter a number (numerator): 34
Enter a number (denominator): 2
The result of 34 divided by 2 is: 17.0'''
