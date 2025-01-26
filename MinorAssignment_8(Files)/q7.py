lines=["Python is a versatile programming language.\n","It is widely used in data science, web development, and automation"]

with open("f.txt","w") as f:
    f.writelines(lines)#takes a list or tuples with \n

with open("f.txt","r") as f:
    r=f.read()#file is read as a string
    k=r.split(" ")
    print(len(k))
    
'''
16'''    
