'''
Write a program to find the number of occurrences of each letter present in a given string., e.g.,
str=‘mississippi’ ⇒ {‘m’: 1, ‘i’: 4, ‘s’: 4, ‘p’: 2}
'''
str=input("enter a string : ")
d=dict()
for i in str:
    if i in d:
        d[i] += 1  # Increment count if the character is already in the dictionary
    else:
        d[i] = 1  

print(d)

'''
enter a string : mississippi
{'m': 1, 'i': 4, 's': 4, 'p': 2}
'''