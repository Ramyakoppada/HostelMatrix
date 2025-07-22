import tkinter as tk
from tkinter import messagebox
from dashboard import DashboardApp

class AdminLoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Login - HostelMatrix")
        self.root.geometry("400x300")

        tk.Label(root, text="Admin Login", font=("Arial", 18)).pack(pady=20)

        tk.Label(root, text="Username").pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=5)

        tk.Label(root, text="Password").pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(root, text="Login", command=self.login).pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "123":
            messagebox.showinfo("Success", "Login successful.")
            self.root.destroy()
            dashboard_root = tk.Tk()
            DashboardApp(dashboard_root, role="admin")
            dashboard_root.mainloop()
        else:
            messagebox.showerror("Login Failed", "Invalid admin credentials.")
