''''
Create a program that reads CSV data and converts it into a list of dictionaries.
Input file, sample.csv contains,
Name,Age,Email
Alice,30,alice@example.com
Bob,25,bob@example.com
Charlie,35,charlie@example.com
Output:
Successfully read 3 rows from ’data.csv’.
First 5 rows of the CSV data as dictionaries:
’Name’: ’Alice’, ’Age’: ’30’, ’Email’: ’alice@example.com’
’Name’: ’Bob’, ’Age’: ’25’, ’Email’: ’bob@example.com’
’Name’: ’Charlie’, ’Age’: ’35’, ’Email’: ’charlie@example.com
'''
import csv

# Create the CSV file with sample data
with open("sample.csv", 'w') as f:
    f.writer('''Name,Age,Email
Alice,30,alice@example.com
Bob,25,bob@example.com
Charlie,35,charlie@example.com''')

# Open the file in read mode
with open("sample.csv", 'r') as file:
    csv_reader = csv.DictReader(file)  # Read the CSV as dictionaries

    # Convert to a list of dictionaries
    data = list(csv_reader)

    # Output the results
    print(f"Successfully read {len(data)} rows from 'sample.csv'.")
    print("First 5 rows of the CSV data as dictionaries:")
    for row in data:
        print(row)

'''
Successfully read 3 rows from 'sample.csv'.
First 5 rows of the CSV data as dictionaries:
{'Name': 'Alice', 'Age': '30', 'Email': 'alice@example.com'}
{'Name': 'Bob', 'Age': '25', 'Email': 'bob@example.com'}
{'Name': 'Charlie', 'Age': '35', 'Email': 'charlie@example.com'}
'''