'''
Identify two exceptions that may be raised while executing the following statement:
result = a + b
'''
a=input("Enter a  : ")
b=input("Enter b : ")
try:
    result = a + b
    print("Result:", result)

except (NameError,ValueError) as e:
    print(f"{e}")
