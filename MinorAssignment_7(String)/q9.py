'''
Create a program to find the number of vowels and consonants in a string.
'''
str=input("Enter string : ")
vowel="aeiouAEIOU"
v=0
c=0
for i in str:
    if(i.isalpha()):
        if(i in vowel):
             v+=1
        else:
             c+=1
print(f" For {str} no of vowels ={v} and no of consonants ={c} ")        
'''
Enter string : apple ewn
 For apple ewn no of vowels =3 and no of consonants =5'''