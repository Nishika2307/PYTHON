'''
Write a Python program that generates a tuple where each element is the square of an integer from 1
to 10.
'''

tpl = tuple(i ** 2 for i in range(1, 11))
print("Tuple:", tpl)

'''
list1=[]
for i in range(1,11):
    list1.append(i*i)

print(tuple(list1))'''