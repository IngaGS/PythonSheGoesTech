#TASK8:
# Write a Python program that reads a JSON file containing a list of dictionaries, sorts the list by a specific key,
# and writes the sorted list back to the file.
import json

with open('data.json') as f:
    data = json.load(f)

data_sorted = sorted(data, key=lambda x: x['age'])

with open('data.json', 'w') as f:
    json.dump(data_sorted, f)

#TASK 9: Write a Python program that reads a CSV file containing student grades, calculates
# their average score and writes the average to a new file.
import csv

def get_lenght(file_path):
    with open("data.csv") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        return len(reader_list)

def append_data(file_path, Student, Grade):
    fieldnames = ['ID', 'Student', 'Grade']
    next_id = get_lenght(file_path)
    with open(file_path, "a",
              newline='') as csvfile:  # the newline padaro, kad duomenys rasytusi kiekvienoj eilutej, kitaip viena eilute praleidzia ir rasosi i kas antra
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()
        writer.writerow({"ID": next_id, "Student": Student, "Grade": Grade})

# append_data("data.csv", "Justin", 5)
# append_data("data.csv", "Inga", 10)
# append_data("data.csv", "Sandra", 7)
# append_data("data.csv", "Olegas", 9)
# append_data("data.csv", "Renata", 6)
# append_data("data.csv", "Vita", 8)
#
# with open('data.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile)
#     next(reader) # skip header row
#     grades = []
#     for row in reader:
#         if len(row) >= 3:
#             grades.append(float(row[2]))
#
# average_grade = sum(grades) // len(grades)
# print(grades)
# append_data("data.csv", "Average: ", average_grade)


#TASK 10: Write a Python program that reads a CSV file containing student grades and writes a
# new CSV file with the grades sorted by student name.
# import os
#
# with open('data.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile)
#     header = next(reader)
#     rows = [row for row in reader]
#
# def sort_by_student_name(row):
#     return row[1]
#
# sorted_rows = sorted(rows, key=sort_by_student_name)
#
# with open('sorted_data.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(header)
#     for i, row in enumerate(sorted_rows):
#         writer.writerow([i+1] + row[1:])
#
# os.replace('sorted_data.csv', 'data.csv')