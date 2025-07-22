


import tkinter as tk
from dashboard import DashboardApp

def student_interface():
    root = tk.Tk()
    app = DashboardApp(root, role="student")
    root.mainloop()

