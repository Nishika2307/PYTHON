def perfect(num):
    if(num<1):
        return 0
    sum=0
    for i in range(1,num):
        if(num%i==0):
            sum+=i
    
    if(num==sum):
        return  1
    else:
        return -1    
    
num=int(input("Enter a number : "))
ans=perfect(num)
if(ans==1):
    print(f"Perfect number : {num}")
elif (ans ==-1):
    print(f"Not a Perfect number : {num}")
else:
    print(f"Number is not a natural number {num}")
        
    
        
            
            
        
    

    

    