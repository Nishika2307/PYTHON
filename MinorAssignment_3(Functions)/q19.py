'''
Create a function to find the greatest common divisor (GCD) of two numbers using a while loop.
'''
''' Euclidean algorithm, which repeatedly replaces the larger number by the remainder when the larger
    number is divided by the smaller one, until one of the numbers becomes zero. The other number at that point will be the GCD.'''

def gcd(a, b):
    # Use the Euclidean algorithm to find the GCD
    while b != 0:
        a, b = b, a % b
    return a

# Input numbers
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

# Output the GCD
print(f"The GCD of {a} and {b} is: {gcd(a, b)}")

'''
Enter 1st number: 48
Enter 2nd number: 18
The GCD of 48 and 18 is: 6
'''