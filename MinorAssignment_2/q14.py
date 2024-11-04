roomtype=input("Enter room type(standard,deluxe,suite)  : ")
stay=int(input("Enter length of stay : "))
season=input("Enter season type(peak,off) : ")
loyalty=input("Enter yes or no : ")
price=0
if(roomtype=="standard"):
    price=100*stay
elif(roomtype=="deluxe"):
    price=150*stay
elif(roomtype=="suite"):
    price=250*stay      
else:
    print("Invalid choice of room")
    price=0    
    
if(stay>3):
    price=price-0.1*price    
if(stay>7):
      price=price-0.2*price    

if(season=="peak"):
    price=price+0.2*price
else:
    price=price-0.15*price
    
if(loyalty=="yes"):
    price=price-0.05*price

print(f"The final booking cost : {price}")        

'''
o/p
Enter room type(standard,deluxe,suite)  : deluxe
Enter length of stay : 4
Enter season type(peak,off) : off
Enter yes or no : yes
The final booking cost : 436.05
'''
   
        