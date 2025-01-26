'''
Write a Python program to find the second largest value in a list of n elements.
'''
n=int(input("Enter size : "))
lst=[int(input("Enter  a number : ")) for _ in range(n)]
new_list=sorted(lst,reverse=True)
print(new_list[1])

'''
Enter size : 4
Enter  a number : 1
Enter  a number : 2
Enter  a number : 4
Enter  a number : 3
3
'''