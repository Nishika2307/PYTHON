year=int(input("enter the year : "))
if(year%4==0):
    if(year%100==0):
       if(year%400==0):
          print(f"{year} is a leap year")
       else:
          print(f"{year} is not a leap year")
  
else:
   print(f"{year} not a leap year")
   

'''
Output
enter the year : 2021
2021 not a leap year
'''
   