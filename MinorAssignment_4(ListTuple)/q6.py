'''Input 10 integers from the keyboard into a list. The number to be searched is entered through the
keyboard by the user. Write a Python program to find if the number to be searched is present in the
list and if it is present, display the number of times it appears in the list.'''

def searching(lst, ele):
    count = lst.count(ele)
    if count > 0:
        print(f"{ele} is present {count} times in the list.")
    else:
        print(f"{ele} is not present in the list.")


lst=[int(input("Enter  a number:")) for _  in range(5)] 
print(f"List: {lst}")
ele = int(input("Enter element to search: "))
searching(lst, ele)

'''
Enter  a number:3
Enter  a number:4
Enter  a number:5
Enter  a number:5
Enter  a number:3
Enter  a number:5
List: [3, 4, 5, 3, 5]
Enter element to search: 3
3 is present 2 times in the list.
'''
