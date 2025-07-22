
import tkinter as tk
from dashboard import DashboardApp

def admin_interface():
    root = tk.Tk()
    app = DashboardApp(root, role="admin")
    root.mainloop()


