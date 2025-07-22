
import tkinter as tk
from tkinter import messagebox
import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="PWD#sql",
        database="hostelmatrix"
    )

class StudentLoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Login")
        self.root.geometry("300x300")
        self.build_login()

    def build_login(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Student Login", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.root, text="Username").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        tk.Label(self.root, text="Password").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.root, text="Login", command=self.login).pack(pady=10)
        tk.Button(self.root, text="Don't have an account? Signup", command=self.build_signup).pack(pady=5)

    def build_signup(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Student Signup", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.root, text="Username").pack()
        self.new_username = tk.Entry(self.root)
        self.new_username.pack(pady=5)

        tk.Label(self.root, text="Password").pack()
        self.new_password = tk.Entry(self.root, show="*")
        self.new_password.pack(pady=5)

        tk.Label(self.root, text="Confirm Password").pack()
        self.confirm_password = tk.Entry(self.root, show="*")
        self.confirm_password.pack(pady=5)

        tk.Button(self.root, text="Signup", command=self.signup).pack(pady=10)
        tk.Button(self.root, text="Back to Login", command=self.build_login).pack(pady=5)

    def signup(self):
        username = self.new_username.get()
        password = self.new_password.get()
        confirm_password = self.confirm_password.get()

        if not username or not password:
            messagebox.showerror("Error", "All fields are required")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return

        try:
            db = connect_db()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM students WHERE username = %s", (username,))
            if cursor.fetchone():
                messagebox.showerror("Error", "Username already exists")
                return
            cursor.execute("INSERT INTO students (username, password) VALUES (%s, %s)", (username, password))
            db.commit()
            messagebox.showinfo("Success", "Signup successful! Please login.")
            self.build_login()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", str(err))
        finally:
            db.close()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Please enter username and password")
            return

        try:
            db = connect_db()
            cursor = db.cursor()
            cursor.execute("SELECT password FROM students WHERE username = %s", (username,))
            result = cursor.fetchone()

            if result is None:
                messagebox.showerror("Login Failed", "User does not exist")
            elif result[0] != password:
                messagebox.showerror("Login Failed", "Invalid username or password")
            else:
                messagebox.showinfo("Login Success", f"Welcome {username}!")
                self.root.destroy()
                from dashboard import DashboardApp
                new_root = tk.Tk()
                DashboardApp(new_root, role="student")
                new_root.mainloop()

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", str(err))
        finally:
            db.close()

# Run this file to start the UI
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentLoginApp(root)
    root.mainloop()

