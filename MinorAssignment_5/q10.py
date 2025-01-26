'''
Write a program to find the number of occurrences of each vowel present in a given string, and also
print the vowels.
'''

str=input("Enter a string : ")
vowels="aeiouAEIOU"
dict={}
for i in str:
    if i in vowels:
        if i in dict:
           dict[i]+=1
        else:
            dict[i]=1
               
print(dict)
'''
Enter a string : apple
{'a': 1, 'e': 1}'''
        
