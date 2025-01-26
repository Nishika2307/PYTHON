'''
Write a function that takes a number as an input parameter and returns the corresponding text in
words, e.g., on input 452, the function should return ‘Four Five Two’. Use a dictionary for mapping
digits to their string representation.
'''
dict={"1": "One","2" : "Two" ,"3":"Three" ,"4" :"Four" ,"5": "Five" ,"6":"Six" ,"7":"Seven" ,"8":"Eight" ,"9":"Nine"}
n=input("Enter a number : ")
for i in n:
    if i in dict:
        print(dict[i],end=" ")

'''
Enter a number : 452
Four Five Two
'''