'''
Write a Python function that takes a string and returns a new string where every vowel in the input
string is replaced by the next vowel in sequence (a → e, e → i, i → o, o → u, u → a).'''

str=input("Enter string : ")
str=str.lower()
result=""
vowels="aeiou"
for i in str:
    if i in vowels:
        result+=vowels[(vowels.index(i)+1)%5]
    else:
        result+=i
print(result)

'''
Enter string : Hello 
hillu 
 '''
    
    
       