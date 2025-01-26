'''
Write a program to analyze the distribution of ticket prices in the Titanic dataset. Using Pandas, filter
and display the names of passengers who were under 18 years old on the Titanic.
Sample input files:
#titanic.csv
PassengerId,Survived,Pclass,Name,Sex,Age,Fare
1,1,1,”Allen, Miss. Elisabeth”,female,29,211.3375
2,0,3,”Moran, Mr. James”,male,25,7.925
3,1,2,”Brown, Mrs. Mary”,female,35,51.8625
4,0,3,”Smith, Mr. John”,male,40,8.05
5,1,1,”Clark, Miss. Martha”,female,18,81.8583
6,0,3,”Williams, Mr. Charles”,male,12,10.5
7,1,2,”Moore, Miss. Ann”,female,16,30.0708
8,0,3,”Wilson, Mr. Henry”,male,19,7.75
'''

#Q20
import pandas as pd

# Load the Titanic dataset
data = pd.read_csv("titanic.csv")

# 1. Analyze the distribution of ticket prices (Fare)
print("Distribution of ticket prices (Fare):")
print(data["Fare"].describe())

# 2. Filter and display the names of passengers under 18 years old
under_18 = data[data["Age"] < 18]
print(under_18)

print("\nPassengers under 18 years old:")
for name in under_18["Name"]:
    print(name)
