marks=int(input("Enter marks : "))

if(marks>=90 and marks<=100):
    print(f"Excellent !! \nGrade is A for marks={marks}")
elif(marks>=80 and marks<=89):
    print(f"Good \nGrade is B for marks={marks}")
elif(marks>=70 and marks<=79):
    print(f"Average \nGrade is C for marks={marks}")
elif(marks>=60 and marks<=69):
    print(f"Needs Improvement \nGrade is D for marks={marks}")
else:
    print(f"Failing \nGrade is F for marks={marks}")        
    
    
'''
OUTPUT
Enter marks : 79
Average 
Grade is C for marks=79
'''           
    
        