import tkinter as tk
from tkinter import messagebox
import sqlite3
conn = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    course TEXT
)
""")
try:
    cursor.execute("ALTER TABLE students ADD COLUMN age TEXT")
except:
    pass  
conn.commit()
def register_student():
    name = entry_name.get()
    email = entry_email.get()
    course = entry_course.get()
    age = entry_age.get()
    if name == "" or email == "" or course == "" or age == "":
        messagebox.showerror("Error", "All fields are required!")
        return
    try:
        cursor.execute(
            "INSERT INTO students (name, email, course, age) VALUES (?, ?, ?, ?)",
            (name, email, course, age)
        )
        conn.commit()
        messagebox.showinfo("Success", "Student Registered Successfully!")
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_course.delete(0, tk.END)
        entry_age.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("400x300")
tk.Label(root, text="Name").pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack()
tk.Label(root, text="Email").pack(pady=5)
entry_email = tk.Entry(root)
entry_email.pack()
tk.Label(root, text="Course").pack(pady=5)
entry_course = tk.Entry(root)
entry_course.pack()
tk.Label(root, text="Age").pack(pady=5)
entry_age = tk.Entry(root)
entry_age.pack()
tk.Button(root, text="Register", command=register_student).pack(pady=20)
root.mainloop()
conn.close()