def perfect(num):
    if(num<1):
        return 0 #not a natural number
    sum=0
    for i in range(1,num):
        if(num%i==0):
            sum+=i
    
    if(num==sum):
        return  1  #for perfect number
    else:
        return -1    #for not perfect number
    
num=int(input("Enter a number : "))
ans=perfect(num)
if(ans==1):
    print(f"Perfect number : {num}")
elif (ans ==-1):
    print(f"Not a Perfect number : {num}")
else:
    print(f"Number is not a natural number {num}")
        
    
'''
o/p
Enter a number : 9
Not a Perfect number : 9
Enter a number : -3
Number is not a natural number -3
'''       
            
            
        
    

    

    