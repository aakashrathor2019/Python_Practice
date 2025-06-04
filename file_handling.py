import csv

# Field names
f = ['Name', 'Branch', 'Year', 'CGPA']

# Data rows of CSV file
r = [
    ['Nikhil', 'COE', '2', '9.0'],
    ['Sanchit', 'COE', '2', '9.1'],
    ['Aditya', 'IT', '2', '9.3'],
    ['Sagar', 'SE', '1', '9.5'],
    ['Prateek', 'MCE', '3', '7.8'],
    ['Sahil', 'EP', '2', '9.1']
]

# Name of the CSV file
fn = "university_records.csv"

# Writing to CSV file
with open(fn, 'w', newline='') as csvfile:
    # Creating a CSV writer object
    csvwriter = csv.writer(csvfile)
    
    # Writing the field names
    csvwriter.writerow(f)
    
    # Writing the data rows
    csvwriter.writerows(r)