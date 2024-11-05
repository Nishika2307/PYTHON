'''
Write a Python program that takes the name of a month as input and returns the number of days in
that month.
Input: The name of the Month: February
Output: No. of days: 28/29 days'''

def days(a):
    a=a.lower()
    match(a):
        case "january" | "march" | "may" | "june" | "july" | "august" | "october" | "december" :
            return "31"
        case "february":
            return "28/29"
        case _:
            return "30"
        
    
    
n=input("Enter the month name : ")
print(days(n))

'''
Enter the month name : may
31
'''