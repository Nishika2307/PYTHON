'''
Make a multilevel dictionary called life. Use these strings for the topmost keys: ‘animals’, ‘plants’,
and ‘other’. Make the ‘animals’ key refer to another dictionary with the keys ‘cats’, ‘octopi’, and
‘emus’. Make the ‘cats’ key refer to a list of strings with the values ‘Henri’, ‘Grumpy’, and ‘Lucy’.
Make all the other keys refer to empty dictionaries.
'''

# Creating the multilevel dictionary 'life'
life = {
    'animals': {
        'cats': ['Henri', 'Grumpy', 'Lucy'],
        'octopi': {},
        'emus': {}
    },
    'plants': {},
    'other': {}
}

# Displaying the dictionary
print(life)

'''
{'animals': {'cats': ['Henri', 'Grumpy', 'Lucy'], 'octopi': {}, 'emus': {}}, 'plants': {}, 'other': {}}'''
