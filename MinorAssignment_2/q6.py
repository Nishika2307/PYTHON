num = int(input("Enter a number: "))
if num < 2:
    print(f"{num} is not a Prime number")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a Prime number")
    else:
        print(f"{num} is not a Prime number")

             
'''
Output
Enter a number: 4
4 is not a Prime number
'''             