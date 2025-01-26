
'''Write a Python program that lets an instructor enter a student’s first and last name (strings) and three
exam grades (integers). Save each student’s data in a grades.csv file using the csv module, with each
record in the format:
firstname,lastname,exam1grade,exam2grade,exam3grade'''

import pandas as pd

def write_student_data():
    # Open the CSV file in append mode to add new records
    with open('grades.csv', mode='a', newline='') as file:
        writer = pd.write(file)
        
        # Prompt the instructor for student information
        first_name = input("Enter student's first name: ")
        last_name = input("Enter student's last name: ")
        
        # Input grades for the 3 exams
        try:
            exam1 = int(input("Enter grade for Exam 1: "))
            exam2 = int(input("Enter grade for Exam 2: "))
            exam3 = int(input("Enter grade for Exam 3: "))
        except ValueError:
            print("Invalid input. Please enter numeric grades.")
            return
        
        # Write the student data to the CSV file
        writer.writerow([first_name, last_name, exam1, exam2, exam3])
        print("Student data has been saved successfully.")
        

# Call the function to collect and save student data
write_student_data()
