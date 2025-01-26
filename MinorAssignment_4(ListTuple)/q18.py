'''
You can compute the standard deviation with the following formula; you have to store the individual
numbers using a list so that they can be used after the mean is obtained.
mean =
Pn
i=1 xi
n
=
x1 + x2 + x3 + · · · + xn
n
deviation =
sPn
i=1(xi − mean)
2
n − 1
Write a Python program that prompts the user to enter ten numbers and displays the mean and standard
deviation, as shown in the following sample run:
Enter ten numbers: 1.9 2.5 3.7 2 1 6 3 4 5 2
The mean is 3.11
The standard deviation is 1.55738.

'''

# mean = (x1 + x2 + x3 + ... + xn) / n
# deviation = sqrt((sum(xi - mean)^2) / (n - 1))

import math

numbers = [int(input("Enter  a number :" )) for _ in range(11)]
print(numbers)
mean = sum(numbers) /10
std_dev = math.sqrt(sum((x - mean) ** 2 for x in numbers) / 10- 1)

print("Mean:", mean)
print("Standard Deviation:", std_dev)

'''
Enter  a number:3
Enter  a number:4
Enter  a number:5
Enter  a number:5
Enter  a number:3
Enter  a number:5
List: [3, 4, 5, 3, 5]
Enter element to search: 3
Enter element to search: 3
3 is present 2 times in the list.'''
