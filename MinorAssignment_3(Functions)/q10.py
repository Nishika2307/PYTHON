'''
Create a function that returns all the unique permutations of a given string.'''

from itertools import permutations

def unique_permutations(string):
    # Generate all permutations and store them in a set to ensure uniqueness
    unique_perms = set(''.join(p) for p in permutations(string))
    return list(unique_perms)  # Convert the set back to a list

# Example usage
string = "AAB"
result = unique_permutations(string)
print(result)

'''
['AAB', 'BAA', 'ABA']
'''