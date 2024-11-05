num=int(input("Enter a positive integer : "))
rev=0
while(num!=0):
    d=num%10
    rev=rev*10+d
    num//=10
print("Number after reversing the order of digits : ",rev)    

'''
Enter a positive integer : 1234
Number after reversing the order of digits :  4321
'''