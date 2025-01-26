'''
For the following dictionary, create lists of its keys, values, and items, and show those lists.
roman numerals = {‘I’: 1, ‘II’: 2, ‘III’: 3, ‘V’: 5}
'''
roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5}

# Creating lists for keys, values, and items
keys_list = list(roman_numerals.keys())
values_list = list(roman_numerals.values())
items_list = list(roman_numerals.items())

# Displaying the lists
print("List of keys:", keys_list)
print("List of values:", values_list)
print("List of items:", items_list)

'''
List of keys: ['I', 'II', 'III', 'V']
List of values: [1, 2, 3, 5]
List of items: [('I', 1), ('II', 2), ('III', 3), ('V', 5)]'''
