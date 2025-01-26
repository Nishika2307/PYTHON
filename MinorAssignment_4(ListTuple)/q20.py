'''
Write a Python program to create a new list that contains the square of every element in a given list
using list comprehension
'''

n=int(input("Enter size : "))
lst=[int(input("Enter  a number : ")) for _ in range(n)]
new_lst=[x*x for x in lst]
print(new_lst)

'''
Enter size : 3
Enter  a number : 2
Enter  a number : 1
Enter  a number : 3
[4, 1, 9]'''
