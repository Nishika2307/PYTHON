str=input("Enter  a string : ")
n=len(str)
for i in range (0,n):
    r=""
    for j in range(i,n):
        r+=str[j]
        print (r ,end=" , ")
        
'''
Output
Enter  a string : abc
a , ab , abc , b , bc , c ,
'''        
    