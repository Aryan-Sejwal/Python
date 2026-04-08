class Student:
    def __init__(self, name, sap_id, phy, chem, maths):
        self.name = name
        self.sap_id = sap_id
        self.phy = phy
        self.chem = chem
        self.maths = maths
    def display(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("SAP ID:", self.sap_id)
        print("Physics:", self.phy)
        print("Chemistry:", self.chem)
        print("Maths:", self.maths)
    def find_marks_percentage(self):
        total = self.phy + self.chem + self.maths
        percentage = total / 3
        return percentage
    def result(self):
        if self.phy > 40 and self.chem > 40 and self.maths > 40:
            print("Result: PASS")
        else:
            print("Result: FAIL")
n = int(input("Enter number of students: "))
students = []
for i in range(n):
    print(f"\nEnter details of student {i+1}")
    name = input("Name: ")
    sap_id = input("SAP ID: ")
    phy = int(input("Physics marks: "))
    chem = int(input("Chemistry marks: "))
    maths = int(input("Maths marks: "))
    s = Student(name, sap_id, phy, chem, maths)
    students.append(s)
for s in students:
    s.display()
    print("Percentage:", s.find_marks_percentage())
    s.result()
def class_average(students):
    total = 0
    for s in students:
        total += s.find_marks_percentage()
    return total / len(students)
print("\nClass Average Percentage:", class_average(students))