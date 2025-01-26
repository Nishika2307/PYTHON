'''
. Implement a program that reads a titanic1.CSV file into a Pandas DataFrame and finds the passenger
with the longest name.
'''
import pandas as pd
data=pd.read_csv("titanic1.csv")
max=""
for i in data["Name"]:
    if len(i)>len(max):
        max=i

print(max)
'''
Allen, Miss. Elisabeth'''