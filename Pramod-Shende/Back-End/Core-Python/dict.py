#1)Create a dictionary with student names as keys and marks as values.
students = {
    "Pramod": 85,
    "Rushikesh": 90,
    "Saras": 78,
    "Rohan": 92,
    "Rahul": 88
}
print(students)

#2)Add a new student and marks to the dictionary.
students["Yogesh"] = 80
print(students)

#3)Update the marks of a specific student.
students["Pramod"] = 95
print(students)

#4)Delete a student record from the dictionary.
students.pop("Rahul",88)
print(students)

#5)Print all student names (keys).
print(students.keys())

#6)Print all student marks (values).
print(students.values())

#7)Find the student who has the highest marks.
highest = max(students.values())
for student, marks in students.items():
    if marks == highest:
        print(student,marks)
#8)Check whether a specific student exists in the dictionary.
sname = "Rohan"
if sname in students:
    print("sname is exists in dictionary.")
else:
    print("sname does not exist in dictionary.")

#9)Count the total number of students in the dictionary.
total_students = len(students)
print(total_students)

#10)Create a nested dictionary to store student details (name, roll number, marks).
s_details = {
    "Pramod": {"roll_number": 1, "marks": 95},
    "Rushikesh": {"roll_number": 2, "marks": 90},
    "Rohan": {"roll_number": 4, "marks": 92},
    "Rahul": {"roll_number": 5, "marks": 88},
    "Yogesh": {"roll_number": 6, "marks": 80}
}
print(s_details)