'''
Write a function that takes a string as a parameter and returns a string with every successive repetitive
character replaced with a star(*). For example, ’balloon’ is returned as ’bal*o*n’
'''
str=input("Enter a string : ")
strr=""
length=len(str)
for i in range(length):
    if(i<length-1 and str[i]==str[i+1]):
        strr+="*"
    else:
        strr+=str[i]

print(strr)
       
'''
Enter a string : balloon
ba*l*on'''

        
        
    