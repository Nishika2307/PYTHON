'''
. Write a program to accept student name and marks from the user and create a dictionary. Also, display
student marks by taking student name as input
'''


name=input("enter student name : ")
marks=int(input("student marks : "))
t=dict()
t[name]=marks
print(t)
print(t[name])

'''
enter student name : Nishika
student marks : 89
{'Nishika': 89}
89'''