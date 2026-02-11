name = input("Enter Name: ")
roll_no = input("Enter Roll Number: ")
sap_id = input("Enter SAP ID: ")
sem = input("Enter Semester: ")
course = input("Enter Course: ")
print("\nEnter marks of 5 subjects:")
pds = int(input("PDS: "))
python = int(input("Python: "))
chemistry = int(input("Chemistry: "))
english = int(input("English: "))
physics = int(input("Physics: "))
total_marks = pds + python + chemistry + english + physics
percentage = total_marks / 5
cgpa = percentage / 10
if cgpa <= 3.4:
    grade = "F"
elif cgpa <= 5.0:
    grade = "C+"
elif cgpa <= 6.0:
    grade = "B"
elif cgpa <= 7.0:
    grade = "B+"
elif cgpa <= 8.0:
    grade = "A"
elif cgpa <= 9.0:
    grade = "A+"
else:
    grade = "O (Outstanding)"
print("\n---------- GRADE SHEET ----------")
print("Name:", name)
print("Roll Number:", roll_no, "\tSAP ID:", sap_id)
print("Sem:", sem, "\t\tCourse:", course)

print("\nSubject Name\tMarks")
print("PDS\t\t", pds)
print("Python\t\t", python)
print("Chemistry\t", chemistry)
print("English\t\t", english)
print("Physics\t\t", physics)

print("\nPercentage:", percentage, "%")
print("CGPA:", round(cgpa, 1))
print("Grade:", grade)
