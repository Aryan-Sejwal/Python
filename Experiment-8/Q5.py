import tkinter as tk
from tkinter import messagebox
import os

FILE_NAME = "users.txt"

# Load users from file
def load_users():
    users = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            for line in f:
                username, password = line.strip().split(",")
                users[username] = password
    return users

# Save new user
def save_user(username, password):
    with open(FILE_NAME, "a") as f:
        f.write(f"{username},{password}\n")

# ---------------- SIGNUP WINDOW ----------------
def open_signup():
    signup_window = tk.Toplevel(root)
    signup_window.title("Signup")
    signup_window.geometry("300x250")

    tk.Label(signup_window, text="Create Account", font=("Arial", 14)).pack(pady=10)

    tk.Label(signup_window, text="Username").pack()
    username_entry = tk.Entry(signup_window)
    username_entry.pack()

    tk.Label(signup_window, text="Password").pack()
    password_entry = tk.Entry(signup_window, show="*")
    password_entry.pack()

    def signup():
        username = username_entry.get()
        password = password_entry.get()

        users = load_users()

        if username in users:
            messagebox.showerror("Error", "Username already exists!")
        elif username == "" or password == "":
            messagebox.showwarning("Warning", "Fields cannot be empty!")
        else:
            save_user(username, password)
            messagebox.showinfo("Success", "Account created successfully!")
            signup_window.destroy()

    tk.Button(signup_window, text="Signup", command=signup).pack(pady=10)

# ---------------- LOGIN FUNCTION ----------------
def login():
    username = username_entry.get()
    password = password_entry.get()

    users = load_users()

    if username in users and users[username] == password:
        messagebox.showinfo("Success", f"Welcome {username}!")
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Login System")
root.geometry("300x250")

tk.Label(root, text="Login", font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Username").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root, text="Login", command=login).pack(pady=10)
tk.Button(root, text="Signup", command=open_signup).pack()

root.mainloop()