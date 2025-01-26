'''
Make an English-to-French dictionary called e2f and print it. Here are your starter words: dog is
chien, cat is chat, and walrus is morse.
'''
e2f={ "dog" :"chien",
      "cat": "chat",
      "walrus" :"morse"}

search=input("Enter key : ")
if search in e2f :
       print(f"For {search} the french word is {e2f[search]}")
else:
     print("Word not found in the dictionary.")
           
'''
Enter key : walrus
For walrus the french word is morse
'''