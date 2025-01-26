'''
Write a Python function that takes two files of equal size as input from the user. The first file contains
weights of items and the second file contains corresponding prices. Create another file that should
contain price per unit weight for each item.
'''
with open('weight.txt','w') as f:
    f.write("12\n11\n34\n5\n65")
with open("prices.txt","w") as f:
    f.write("23.6\n45\n67.9\n62\n90")
'''
with open("price_per_weight.txt","w+") as f:
    f1=open("weight.txt",'r')
    f2=open("prices.txt",'r')
    col1=f1.readline()
    col2=f2.readline()
    while(col1):
        f.write(col1+" "+col2+'\n')
 '''

with open("price_per_weight.txt", "w") as f_out:
    with open("weight.txt", 'r') as f1, open("prices.txt", 'r') as f2:
        for col1, col2 in zip(f1, f2):  # Read both files line by line simultaneously
            f_out.write(col1.strip() + "\t " + col2.strip() + '\n')



with open("price_per_weight.txt","r+") as f:
    for i in f:
        print(i.strip())


        '''Used zip():

The zip() function reads lines from both files in parallel, ensuring that lines are correctly paired.'''