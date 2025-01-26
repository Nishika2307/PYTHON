'''
Write a Python program to find the length of the longest word in a sentence'''

str=input("Enter a string : ")
l=str.split()
max=0
w=''
'''for i in range(len(l)):
    if (len(l[i])> max):
        max=len(l[i])
        w=l[i]
print(f"Longest word {w} with length {max}")
'''
'''
Nishi Ishika Pratyush
Longest word Pratyush with length 8
'''
for i in l:
    if(len(i)>max):
       max=len(i)
       w=i
print(f" {w} = {max}")       
        