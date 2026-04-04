class Student:
    def __init__(self, n):
        self.students = []

        for i in range(n):
            print(f"\nEnter details of Student {i+1}")
            name = input("Enter Name: ")
            roll = input("Enter Roll No: ")

            marks = []
            for j in range(3):   # assuming 3 subjects
                m = float(input(f"Enter marks of subject {j+1}: "))
                marks.append(m)

            self.students.append({
                "name": name,
                "roll": roll,
                "marks": marks
            })

    # a) Display student details
    def display(self):
        print("\n--- Student Details ---")
        for s in self.students:
            print(f"Name: {s['name']}, Roll: {s['roll']}, Marks: {s['marks']}")

    # b) Find percentage
    def marks_percentage(self):
        print("\n--- Percentage ---")
        for s in self.students:
            total = sum(s['marks'])
            percent = total / len(s['marks'])
            print(f"{s['name']} Percentage: {percent:.2f}%")

    # c) Display result
    def result(self):
        print("\n--- Result ---")
        for s in self.students:
            if all(m > 40 for m in s['marks']):
                print(f"{s['name']} → PASS")
            else:
                print(f"{s['name']} → FAIL")

    # d) Class average
    def class_average(self):
        total_marks = 0
        total_subjects = 0

        for s in self.students:
            total_marks += sum(s['marks'])
            total_subjects += len(s['marks'])

        avg = total_marks / total_subjects
        print(f"\nClass Average: {avg:.2f}%")

# ---------------- MAIN ----------------
n = int(input("Enter number of students: "))
obj = Student(n)

obj.display()
obj.marks_percentage()
obj.result()
obj.class_average()