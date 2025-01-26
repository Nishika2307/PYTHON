'''
Write a function to implement a basic calculator that can add, subtract, multiply, and divide two
numbers based on user input.'''

def calculator(num1,num2,op):
    match(op):
        case '1':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        case '2':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        case '3':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        case '4':
            if num2 == 0:
                print("Error! Division by zero.")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        case _:
            print("Invalid input. Please select a valid operation.")

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
op=input("Enter operator : ")
calculator(num1,num2,op)



'''
Enter first number: 5
Enter second number: 2
1. Add
2. Subtract
3. Multiply
4. Divide
Enter operator : 3
5 * 2 = 10

Enter first number: 4
Enter second number: 0
1. Add
2. Subtract
3. Multiply
4. Divide
Enter operator : 4
Error! Division by zero.
'''