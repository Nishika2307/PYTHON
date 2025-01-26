''''
Write a Python program that removes all occurrences of a specific element from a list
'''
n=int(input("Enter range : "))
lst=[int(input("Enter the element : ")) for _ in range(n)]
# Remove all occurrences of the element using list comprehension
element=int(input("Enter element to remove : "))
lst = [x for x in lst if x != element]

print(f"List after removing all occurrences of {element}:", lst)

#List after removing all occurrences of 3: [1, 2, 4, 5, 6]