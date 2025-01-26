'''
Write a Python function that sorts a list of tuples based on the second element of each tupl
'''
lst = [(1, 3), (3, 7), (3, 6)]
new_lst = sorted(lst, key=lambda x: x[1])
print(new_lst)

'''
[(1, 3), (3, 6), (3, 7)]
'''