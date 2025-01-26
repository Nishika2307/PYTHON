'''
Write a Python program that prompts the user to enter a list and displays whether the list is sorted or
not. Here is a sample run. Note that the first number in the input indicates the number of elements in
the list. This number is not part of the list. Here is the sample run:
Enter list: 8 10 1 5 16 61 9 11 1
The list is not sorted
Enter list: 10 1 1 3 4 4 5 7 9 11 21
The list is already sorted

'''
n=int(input("Enter size : "))
lst = [int(input("Enter  a number : ")) for _ in range(n)]
ortedlist=sorted(lst)
is_sorted=ortedlist==lst
print("The list is already sorted" if is_sorted else "The list is not sorted")

'''
Enter size : 4
Enter  a number : 1
Enter  a number : 2
Enter  a number : 3
Enter  a number : 4
The list is already sorted
'''
