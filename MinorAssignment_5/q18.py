'''
You are given two lists of integers: list1 and list2. Write a Python function analyze sets(list1,
list2) that performs the following tasks:
• Creates two sets, set1 and set2, from list1 and list2.
• Finds the symmetric difference of set1 and set2 (elements that are in either set, but not both).
• For each element in the symmetric difference:
– If the element is even, multiply it by 2.
– If the element is odd, add 5 to it.
• Return a sorted list of the modified elements.
'''
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
set1 = set(list1)
set2 = set(list2)
print("Both the sets " ,set1 ,set2)
symmetric_diff = set1 ^ set2  #keep the items not present in both sets
print("Symmetric Difference ",symmetric_diff)
modified_elements = []
for element in symmetric_diff:
        if element % 2 == 0:  # If the element is even
            modified_elements.append(element * 2)
        else:  # If the element is odd
            modified_elements.append(element + 5)


print(sorted(modified_elements))

'''
Both the sets  {1, 2, 3, 4, 5} {4, 5, 6, 7, 8}
Symmetric Difference  {1, 2, 3, 6, 7, 8}
[4, 6, 8, 12, 12, 16]'''
