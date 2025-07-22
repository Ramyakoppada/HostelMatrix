


# import tkinter as tk
# from admin import admin_interface
# from student import student_interface
# from db import setup_database

# def main_window():
#     root = tk.Tk()
#     root.title("Hostel Matrix - Login")
#     root.geometry("300x200")

#     tk.Label(root, text="Welcome to Hostel Matrix", font=("Arial", 14)).pack(pady=20)

#     tk.Button(root, text="Admin Panel", width=20, command=lambda: [root.destroy(), admin_interface()]).pack(pady=5)
#     tk.Button(root, text="Student Panel", width=20, command=lambda: [root.destroy(), student_interface()]).pack(pady=5)

#     root.mainloop()

# if __name__ == "__main__":
#     setup_database()  # Ensures DB and tables exist before GUI
#     main_window()



# main.py

# import tkinter as tk
# from dashboard import DashboardApp  # or wherever your DashboardApp class is

# def main_window():
#     root = tk.Tk()
    
#     # Example role selection (you can customize)
#     def login_as_admin():
#         root.destroy()
#         new_root = tk.Tk()
#         DashboardApp(new_root, role="admin")
#         new_root.mainloop()

#     def login_as_student():
#         root.destroy()
#         new_root = tk.Tk()
#         DashboardApp(new_root, role="student")
#         new_root.mainloop()

#     root.title("HostelMatrix Home")
#     root.geometry("300x200")

#     tk.Label(root, text="Welcome to HostelMatrix").pack(pady=10)
#     tk.Button(root, text="Login as Admin", command=login_as_admin).pack(pady=5)
#     tk.Button(root, text="Login as Student", command=login_as_student).pack(pady=5)

#     root.mainloop()

# if __name__ == "__main__":
#     main_window()


# import tkinter as tk

# def main_window():
#     root = tk.Tk()
#     root.title("HostelMatrix Home")
#     root.geometry("300x200")

#     def login_as_admin():
#         root.destroy()
#         from admin_login import AdminLoginApp
#         new_root = tk.Tk()
#         AdminLoginApp(new_root)
#         new_root.mainloop()

#     def login_as_student():
#         root.destroy()
#         from dashboard import DashboardApp
#         new_root = tk.Tk()
#         DashboardApp(new_root, role="student")
#         new_root.mainloop()

#     tk.Label(root, text="Welcome to HostelMatrix").pack(pady=10)
#     tk.Button(root, text="Login as Admin", command=login_as_admin).pack(pady=5)
#     tk.Button(root, text="Login as Student", command=login_as_student).pack(pady=5)

#     root.mainloop()

# if __name__ == "__main__":
#     main_window()


import tkinter as tk

def main_window():
    root = tk.Tk()
    root.title("HostelMatrix Home")
    root.geometry("300x200")

    def login_as_admin():
        root.destroy()
        from admin_login import AdminLoginApp
        new_root = tk.Tk()
        AdminLoginApp(new_root)
        new_root.mainloop()

    def login_as_student():
        root.destroy()
        from student_login import StudentLoginApp  # Make sure this file exists
        new_root = tk.Tk()
        StudentLoginApp(new_root)
        new_root.mainloop()

    tk.Label(root, text="Welcome to HostelMatrix", font=("Arial", 14)).pack(pady=20)
    tk.Button(root, text="Login as Admin", command=login_as_admin, width=20).pack(pady=5)
    tk.Button(root, text="Login as Student", command=login_as_student, width=20).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main_window()
