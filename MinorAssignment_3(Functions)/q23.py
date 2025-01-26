'''
Write a function that returns the index of each vowel in a string using a for loop.'''

def vowels(s):
   vowel="aeiou"
   vow=[i for i in range(len(s)) if(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u')]
   return vow

s=input("Enter a string : ")
print(vowels(s.lower()))

'''
Enter a string : an apple
[0, 3, 7]
'''