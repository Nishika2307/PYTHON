'''
Write a function that takes a string of lowercase alphabets as inputs and gives an output by shifting
them by one letter ahead. Note that if the string has ’z’, then it will be treated as ’a’. Example: python
7→ qzuipo, pythonzabc 7→ qzuipobbcd.
'''
def one_ahead(s):
    k=""
    for i in s:
        if(i=='z'):
            k=k+'a'
        else:
            k=k+chr(ord(i)+1)
    return k

s=input("Enter a string : ")
print(s,"->",one_ahead(s))

'''
Enter a string : python
python -> qzuipo'''
