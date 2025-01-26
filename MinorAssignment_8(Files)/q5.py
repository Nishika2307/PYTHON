'''
write code that reads the grades from the grades.txt file. Display the individual grades and their total,
count, and average'''

def sumgrade(grades):
   g=grades.split(",")
   print(g)
   sum=0
   for i in g:
     sum+=int(i)
   return sum



with open("grades.txt",'w') as f:
    f.write("90,99,100,60")

with open("grades.txt",'r') as f:
    grades=f.read()
    #print(grades)
    sum=sumgrade(grades)
    print("sum:",sum)

    print("average",sum/(grades.count(',')+1))