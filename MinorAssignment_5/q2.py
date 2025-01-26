'''
. Write a program to enter names and percentage of marks in a dictionary and display the information
on the screen.
'''
d=eval(input("enter names:marks : "))
print(d)
for name, marks in d.items():
    print(f"{name} : {marks}")
    
'''
{"Nishi " :89 ,"Ishi" :76 ,"Mini" :97 }
{'Nishi ': 89, 'Ishi': 76, 'Mini': 97}
Nishi   :  89
Ishi  :  76
Mini  :  97'''