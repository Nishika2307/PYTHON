'''
Write a function that inputs a number and returns the product of digits of that number.
'''
def product_of_digits(n):
    if n == 0:
        return 0  # If n is 0, return 0, as product of digits of 0 is 0
    if n < 10:
        return n  # If it's a single digit, return it
    else:
        return (n % 10) * product_of_digits(n // 10)

n = int(input("Enter a number: "))
print("Product of digits of", n, ":", product_of_digits(n))

'''
Enter a number: 452
Product of digits of 452 : 40'''

