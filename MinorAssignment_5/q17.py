'''
Using the sets {‘red’, ‘green’, ‘blue’}, and {‘cyan’, ‘green’, ‘blue’, ‘magenta’, ‘red’},
display the results of:
a) comparing the sets using each of the comparison operators.
b) combining the sets using each of the mathematical set operators
'''
# Define the two sets
set1 = {'red', 'green', 'blue'}
set2 = {'cyan', 'green', 'blue', 'magenta', 'red'}

# a) Comparing the sets using each of the comparison operators

print("a) Comparison Operators:")

# Check if set1 is a subset of set2
print(f"set1 <= set2 (set1 is a subset of set2): {set1 <= set2}")

# Check if set1 is a proper subset of set2
print(f"set1 < set2 (set1 is a proper subset of set2): {set1 < set2}")

# Check if set1 is equal to set2
print(f"set1 == set2 (set1 is equal to set2): {set1 == set2}")

# Check if set1 is a superset of set2
print(f"set1 >= set2 (set1 is a superset of set2): {set1 >= set2}")

# Check if set1 is a proper superset of set2
print(f"set1 > set2 (set1 is a proper superset of set2): {set1 > set2}")

# Check if set1 and set2 are disjoint (no common elements)
print(f"set1.isdisjoint(set2) (set1 and set2 are disjoint): {set1.isdisjoint(set2)}")


# b) Combining the sets using each of the mathematical set operators

print("\nb) Mathematical Set Operators:")

# Union (combines all elements from both sets, removing duplicates)
union_set = set1 | set2
print(f"set1 | set2 (Union of set1 and set2): {union_set}")

# Intersection (returns only the common elements between both sets)
intersection_set = set1 & set2
print(f"set1 & set2 (Intersection of set1 and set2): {intersection_set}")

# Difference (returns elements in set1 but not in set2)
difference_set1 = set1 - set2
print(f"set1 - set2 (Difference of set1 and set2): {difference_set1}")

# Symmetric Difference (returns elements in set1 or set2, but not in both)
symmetric_difference_set = set1 ^ set2
print(f"set1 ^ set2 (Symmetric difference of set1 and set2): {symmetric_difference_set}")

'''
a) Comparison Operators:
set1 <= set2 (set1 is a subset of set2): True
set1 < set2 (set1 is a proper subset of set2): True
set1 == set2 (set1 is equal to set2): False
set1 >= set2 (set1 is a superset of set2): False
set1 > set2 (set1 is a proper superset of set2): False
set1.isdisjoint(set2) (set1 and set2 are disjoint): False

b) Mathematical Set Operators:
set1 | set2 (Union of set1 and set2): {'red', 'green', 'blue', 'magenta', 'cyan'}
set1 & set2 (Intersection of set1 and set2): {'red', 'green', 'blue'}
set1 - set2 (Difference of set1 and set2): set()
set1 ^ set2 (Symmetric difference of set1 and set2): {'magenta', 'cyan'}
'''