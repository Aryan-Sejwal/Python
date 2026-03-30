import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")

# Functions
def add():
    n1 = float(entry1.get())
    n2 = float(entry2.get())
    result_label.config(text="Result: " + str(n1 + n2))

def subtract():
    n1 = float(entry1.get())
    n2 = float(entry2.get())
    result_label.config(text="Result: " + str(n1 - n2))

def multiply():
    n1 = float(entry1.get())
    n2 = float(entry2.get())
    result_label.config(text="Result: " + str(n1 * n2))

def divide():
    n1 = float(entry1.get())
    n2 = float(entry2.get())
    if n2 == 0:
        result_label.config(text="Cannot divide by zero")
    else:
        result_label.config(text="Result: " + str(n1 / n2))

# Input fields
tk.Label(root, text="Enter Number 1").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Number 2").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Buttons
tk.Button(root, text="Add", command=add).pack(pady=2)
tk.Button(root, text="Subtract", command=subtract).pack(pady=2)
tk.Button(root, text="Multiply", command=multiply).pack(pady=2)
tk.Button(root, text="Divide", command=divide).pack(pady=2)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

# Run the app
root.mainloop()