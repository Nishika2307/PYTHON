n=int(input("Enter an  integer :"))
l1=[] #empty list
while n!=1:
     for i in range(2,n+1):
          if(n%i==0):
               break
     print(i)
     print("n:",n)
     l1.append(i)
     n=n//i
     
l1.sort()
print (l1)

'''
Enter an  integer :120
2
n: 120
2
n: 60
2
n: 30
3
n: 15
5
n: 5
[2, 2, 2, 3, 5]
'''