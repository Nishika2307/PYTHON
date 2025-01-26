def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

user = int(input("Enter a number: "))
sum= 0

for num in range(2, user):
    if is_prime(num):
        sum+= num

print(f"The sum of all prime numbers below {user} is {sum}.")

             
'''
Output
Enter a number: 20
The sum of all prime numbers below 20 is 77.
'''             