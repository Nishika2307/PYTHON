'''
Create a program that determines and displays the number of unique characters in a string entered by
the user, e.g., Hello, World! has 10 unique characters, while zzz has only one unique character. Use
a dictionary or set to solve this problem
'''

s=input("Enter a string : ")
se=set()
for i in s:
        se.add(i)
print(se)
print(len(se))

'''
Enter a string : Nishika
{'k', 'N', 'i', 'a', 's', 'h'}
6
'''