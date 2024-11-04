
row=int(input("Enter the row number :"))
column=input("Enter the column character : ")
print("The Ascii of column is:",ord(column))
if((row+ord(column))%2==0):
    print("Colour of the box is black")
else:
     print("Colour of the box is white")
        
    
    
