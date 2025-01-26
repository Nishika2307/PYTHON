'''
A dictionary which maps country names to Internet top-level domains (TLDs) is given as follows:
tlds = {‘Canada’: ‘ca’, ‘United States’: ‘us’, ‘Mexico’: ‘mx’}
Perform the following tasks and display the results:
a) Check whether the dictionary contains the key ‘Canada’.
b) Check whether the dictionary contains the key ‘France’.
c) Iterate through the key-value pairs and display them in a two-column format.
d) Add the key–value pair ‘Sweden’ and ‘sw’ (incorrect TLD).
e) Update the value for the key ‘Sweden’ to ‘se’ (correct TLD).
f) Use dictionary comprehension to reverse the keys and values.
'''

dict ={"Canada": "ca", "United States": "us", "Mexico": "mx"}
#a
if "Canada" in dict :
       print("Contains")
else:
     print("Does not contain")
#b     
if "France" in dict :
       print("Contains")
else:
     print("Does not contain")
#c
for x ,y in dict.items():
    print(f"{x} :  {y}\n")  
#d    
dict.update({"Sweden" :"sw"})
print(dict)

#e
dict["Sweden"]="se"
print(dict)

#f
    
reversed_dict = {v:k for k, v in dict.items()}
print("\nReversed dictionary:", reversed_dict)
    
'''
Does not contain
Canada :  ca

United States :  us

Mexico :  mx

{'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx', 'Sweden': 'sw'}
{'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx', 'Sweden': 'se'}

Reversed dictionary: {'ca': 'Canada', 'us': 'United States', 'mx': 'Mexico', 'se': 'Sweden'}'''      
