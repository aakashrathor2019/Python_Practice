import csv

d  = [
    {'Name': 'Nikhil', 'Branch': 'COE', 'Year': '2', 'CGPA': '9.0'},
    {'Name': 'Sanchit', 'Branch': 'COE', 'Year': '2', 'CGPA': '9.1'},
    {'Name': 'Aditya', 'Branch': 'IT', 'Year': '2', 'CGPA': '9.3'},
    {'Name': 'Sagar', 'Branch': 'SE', 'Year': '1', 'CGPA': '9.5'},
    {'Name': 'Prateek', 'Branch': 'MCE', 'Year': '3', 'CGPA': '7.8'},
    {'Name': 'Sahil', 'Branch': 'EP', 'Year': '2', 'CGPA': '9.1'}
]

f = ['Name', 'Branch', 'Year', 'CGPA']
file_name = "college_records.csv"

with open(file_name, 'w', newline='') as csvfile:
    csvwriter = csv.DictWriter(csvfile, fieldnames= f)
    csvwriter.writeheader()

    csvwriter.writerows(d)
    print(f"Data written to {file_name} successfully")