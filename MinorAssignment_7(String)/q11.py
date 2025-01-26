'''
Write a script that reads a line of text, tokenizes the line using space characters as delimiters and
outputs only those words beginning with the letter ’b’ and ending with the letter ’d’.'''

str=input("Enter a string : ")
tokens =str.split(" ") 
print(tokens)
for i in tokens:
    if(i.startswith('b') and i.endswith('d')):
        print(i , end =" , ")

'''
Enter a string : ishi nishk bad nek baad
['ishi', 'nishk', 'bad', 'nek', 'baad']
bad baad'''