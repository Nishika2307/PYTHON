
digits={"0":"ZERO","1":"ONE","2":"TWO","3":"THREE","4":"FOUR","5":"FIVE","6":"SIX","7":"SEVEN","8":"EIGHT","9":"NINE"}
n=input("Enter a Number:")
#unique_digits=set(n)
for i in n:
    if i in digits:
        print(digits[i],end=" ")