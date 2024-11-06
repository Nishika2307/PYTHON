'''
Write a function that removes all punctuation from a string.'''

def removepunc(s):
    ans=""
    for k in s:
        if((ord(k)>=97 and ord(k)<=122) or (ord(k)>=65 and ord(k)<=90) ):
            ans=ans+k
    return ans

str=input("Enter a string  : ")
print(removepunc(str))

'''
Enter a string  : G-$h+l#q
Ghlq'''
