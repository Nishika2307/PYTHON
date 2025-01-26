wamt=int(input("Enter amt to withdraw : "))
ATMamt=int(input("Enter amt in atm : "))
l1=[100,50,20,10]
if(wamt<ATMamt and wamt%10==0):
    for i in l1:
      if(wamt>0 and wamt//i>0):
        print("No of ",i," notes:",wamt//i)
        wamt=wamt%i
else:
   print("Invalid input")
   
'''
o/p
Enter amt to withdraw : 350
Enter amt in atm : 500
No of  100  notes: 3
No of  50  notes: 1
'''   