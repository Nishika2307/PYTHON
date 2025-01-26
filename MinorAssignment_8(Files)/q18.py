'''Write a program to merge two CSV files containing Titanic data and print the combined dataset.
Sample Input Files:
#titanic1.csv
PassengerId,Survived,Pclass,Name,Sex,Age
1,1,1,”Allen, Miss. Elisabeth”,female,29
2,0,3,”Moran, Mr. James”,male,25
#titanic2.csv
PassengerId,Survived,Pclass,Name,Sex,Age
3,1,2,”Brown, Mrs. Mary”,female,35
4,0,3,”Smith, Mr. John”,male,40 '''

import pandas as pd

# Initial data for titanic1.csv
titanic1_data = '''PassengerId,Survived,Pclass,Name,Sex,Age
1,1,1,"Allen, Miss. Elisabeth",female,29
2,0,3,"Moran, Mr. James",male,25
'''

# Write the data into titanic1.csv
with open("titanic1.csv", "w") as f1:
    f1.write(titanic1_data)

# Initial data for titanic2.csv
titanic2_data = '''PassengerId,Survived,Pclass,Name,Sex,Age
3,1,2,"Brown, Mrs. Mary",female,35
4,0,3,"Smith, Mr. John",male,40
'''

# Write the data into titanic2.csv
with open("titanic2.csv", "w") as f2:
    f2.write(titanic2_data)

print("Data written to titanic1.csv and titanic2.csv.")


# Load the first CSV file
titanic1 = pd.read_csv('titanic1.csv')

# Load the second CSV file
titanic2 = pd.read_csv('titanic2.csv')

# Merge the two datasets
combined_data = pd.concat([titanic1, titanic2], ignore_index=True)

# Print the combined dataset
print(combined_data)