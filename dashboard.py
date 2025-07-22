


# import tkinter as tk
# from tkinter import ttk, messagebox
# from db import connect_db

# class DashboardApp:
#     def __init__(self, root, role):
#         self.root = root
#         self.role = role
#         self.root.title(f"{role.capitalize()} Panel - HostelMatrix")
#         self.root.geometry("900x600")

#         self.sidebar = tk.Frame(self.root, width=200, relief='solid', borderwidth=1)
#         self.sidebar.pack(side='left', fill='y')

#         self.main_content = tk.Frame(self.root, relief='solid', borderwidth=1)
#         self.main_content.pack(side='right', fill='both', expand=True)

#         self.add_sidebar_buttons()
#         self.load_content("Dashboard")

#     def add_sidebar_buttons(self):
#         if self.role == "admin":
#             options = ["Dashboard", "Add Hostels", "View Available Rooms", "View Student Bookings", "Complaints", "Logout"]
#         else:
#             options = ["Dashboard", "Book Room", "Submit Complaint", "Logout"]

#         for option in options:
#             button = tk.Button(self.sidebar, text=option, width=20, command=lambda o=option: self.load_content(o))
#             button.pack(pady=5)

#     def load_content(self, section):
#         for widget in self.main_content.winfo_children():
#             widget.destroy()

#         if section == "Dashboard":
#             self.load_dashboard_summary()
#         elif section == "Add Hostels" and self.role == "admin":
#             self.load_add_hostel()
#         elif section == "View Available Rooms" and self.role == "admin":
#             self.load_available_rooms()
#         elif section == "View Student Bookings" and self.role == "admin":
#             self.load_student_bookings()
#         elif section == "Complaints" and self.role == "admin":
#             self.load_complaints()
#         elif section == "Book Room" and self.role == "student":
#             self.load_booking_section()
#         elif section == "Submit Complaint" and self.role == "student":
#             self.load_complaint_form()
#         # elif section == "Logout":
#         #     self.root.destroy()
#         elif section == "Logout":
#             self.root.destroy()
#             import main  # or your main file name (it should define `main_window()` or similar)
#             main.main_window()  # call the function that launches the home screen


#     def load_dashboard_summary(self):
#         tk.Label(self.main_content, text="Dashboard Overview", font=("Arial", 18, "bold")).pack(pady=20)

#         con = connect_db()
#         cur = con.cursor()

#         cur.execute("SELECT COUNT(*) FROM hostels")
#         hostel_count = cur.fetchone()[0]

#         cur.execute("SELECT COUNT(*) FROM complaints")
#         complaint_count = cur.fetchone()[0]

#         cur.execute("SELECT COUNT(*) FROM bookings")
#         booking_count = cur.fetchone()[0]

#         con.close()

#         card_frame = tk.Frame(self.main_content)
#         card_frame.pack(pady=10, padx=20, fill="x")

#         def create_card(parent, title, count, bg_color):
#             card = tk.Frame(parent, bg=bg_color, width=200, height=100, bd=2, relief="groove")
#             card.pack(side="left", padx=15, pady=10, expand=True, fill="both")
#             tk.Label(card, text=title, font=("Arial", 14, "bold"), bg=bg_color, fg="white").pack(pady=(10, 0))
#             tk.Label(card, text=str(count), font=("Arial", 24, "bold"), bg=bg_color, fg="white").pack(pady=(5, 10))

#         create_card(card_frame, "Total Hostels", hostel_count, "#3498db")
#         create_card(card_frame, "Total Bookings", booking_count, "#2ecc71")
#         create_card(card_frame, "Total Complaints", complaint_count, "#e74c3c")

#     def load_add_hostel(self):
#         tk.Label(self.main_content, text="Add New Hostel", font=("Arial", 14)).pack(pady=10)

#         tk.Label(self.main_content, text="Hostel Name").pack()
#         name_entry = tk.Entry(self.main_content)
#         name_entry.pack()

#         tk.Label(self.main_content, text="AC (Yes/No)").pack()
#         ac_var = tk.StringVar(value="no")
#         ac_frame = tk.Frame(self.main_content)
#         ac_frame.pack()
#         tk.Radiobutton(ac_frame, text="Yes", variable=ac_var, value="yes").pack(side='left', padx=10)
#         tk.Radiobutton(ac_frame, text="No", variable=ac_var, value="no").pack(side='left', padx=10)

#         tk.Label(self.main_content, text="Total Rooms").pack()
#         room_entry = tk.Entry(self.main_content)
#         room_entry.pack()

#         def add_hostel():
#             name = name_entry.get()
#             ac = ac_var.get()
#             try:
#                 total = int(room_entry.get())
#             except ValueError:
#                 messagebox.showerror("Invalid", "Total rooms must be a number.")
#                 return

#             if not name:
#                 messagebox.showerror("Invalid", "Hostel name is required.")
#                 return

#             is_ac = 1 if ac == "yes" else 0

#             con = connect_db()
#             cur = con.cursor()
#             try:
#                 cur.execute("INSERT INTO hostels (hostel_name, is_ac, total_rooms, available_rooms) VALUES (%s, %s, %s, %s)",
#                             (name, is_ac, total, total))
#                 con.commit()
#                 messagebox.showinfo("Success", "Hostel added successfully.")
#             except Exception as e:
#                 messagebox.showerror("Database Error", str(e))
#             finally:
#                 con.close()

#             name_entry.delete(0, tk.END)
#             room_entry.delete(0, tk.END)
#             ac_var.set("no")

#         tk.Button(self.main_content, text="Add Hostel", command=add_hostel).pack(pady=10)

#     def load_available_rooms(self):
#         tk.Label(self.main_content, text="Available Rooms", font=("Arial", 14)).pack(pady=10)
#         tree = ttk.Treeview(self.main_content, columns=("ID", "Hostel Name", "AC", "Total", "Available"), show='headings')
#         for col in tree["columns"]:
#             tree.heading(col, text=col)
#         tree.pack(fill='both', expand=True)

#         con = connect_db()
#         cur = con.cursor()
#         cur.execute("SELECT * FROM hostels WHERE available_rooms > 0")
#         for row in cur.fetchall():
#             tree.insert('', 'end', values=row)
#         con.close()

#     def load_student_bookings(self):
#         tk.Label(self.main_content, text="Student Bookings", font=("Arial", 14)).pack(pady=10)
#         tree = ttk.Treeview(self.main_content, columns=("Booking ID", "Student", "Hostel ID", "Room"), show='headings')
#         for col in tree["columns"]:
#             tree.heading(col, text=col)
#         tree.pack(fill='both', expand=True)

#         con = connect_db()
#         cur = con.cursor()
#         cur.execute("SELECT * FROM bookings")
#         for row in cur.fetchall():
#             tree.insert('', 'end', values=row)
#         con.close()

#     def load_complaints(self):
#         tk.Label(self.main_content, text="Complaints", font=("Arial", 14)).pack()
#         tree = ttk.Treeview(self.main_content, columns=("ID", "Student", "Message", "Status"), show='headings')
#         for col in tree["columns"]:
#             tree.heading(col, text=col)
#         tree.pack(pady=10, fill='x')

#         con = connect_db()
#         cur = con.cursor()
#         cur.execute("SELECT * FROM complaints")
#         for row in cur.fetchall():
#             tree.insert('', 'end', values=row)
#         con.close()

#         def update_status():
#             selected = tree.focus()
#             if not selected:
#                 messagebox.showerror("Error", "Please select a complaint to update.")
#                 return
#             values = tree.item(selected, 'values')
#             complaint_id = values[0]
#             new_status = status_var.get()
#             con = connect_db()
#             cur = con.cursor()
#             cur.execute("UPDATE complaints SET status=%s WHERE id=%s", (new_status, complaint_id))
#             con.commit()
#             con.close()
#             tree.item(selected, values=(values[0], values[1], values[2], new_status))
#             messagebox.showinfo("Success", "Complaint status updated.")

#         status_var = tk.StringVar()
#         status_dropdown = ttk.Combobox(self.main_content, textvariable=status_var, values=["Pending", "In Progress", "Resolved"])
#         status_dropdown.pack()
#         tk.Button(self.main_content, text="Update Status", command=update_status).pack(pady=5)

#     def load_booking_section(self):
#         tk.Label(self.main_content, text="Enter Your Name:").pack()
#         name_entry = tk.Entry(self.main_content)
#         name_entry.pack()

#         tree = ttk.Treeview(self.main_content, columns=("ID", "Name", "AC", "Total", "Available"), show='headings')
#         for col in tree["columns"]:
#             tree.heading(col, text=col)
#         tree.pack(pady=10, fill='x')

#         def refresh():
#             for row in tree.get_children():
#                 tree.delete(row)
#             con = connect_db()
#             cur = con.cursor()
#             cur.execute("SELECT * FROM hostels")
#             for row in cur.fetchall():
#                 tree.insert('', 'end', values=row)
#             con.close()

#         def book():
#             selected = tree.focus()
#             student = name_entry.get()
#             if not selected or not student:
#                 messagebox.showerror("Error", "Select a hostel and enter your name.")
#                 return
#             values = tree.item(selected, 'values')
#             hostel_id, total, available = values[0], int(values[3]), int(values[4])
#             if available <= 0:
#                 messagebox.showerror("Full", "No rooms available.")
#                 return
#             room_number = total - available + 1
#             con = connect_db()
#             cur = con.cursor()
#             cur.execute("INSERT INTO bookings (student_name, hostel_id, room_number) VALUES (%s, %s, %s)",
#                         (student, hostel_id, room_number))
#             cur.execute("UPDATE hostels SET available_rooms = available_rooms - 1 WHERE id = %s", (hostel_id,))
#             con.commit()
#             con.close()
#             refresh()
#             messagebox.showinfo("Success", f"Room {room_number} booked!")

#         tk.Button(self.main_content, text="Refresh", command=refresh).pack()
#         tk.Button(self.main_content, text="Book Room", command=book).pack()
#         refresh()

#     def load_complaint_form(self):
#         tk.Label(self.main_content, text="Enter Your Name:").pack()
#         name_entry = tk.Entry(self.main_content)
#         name_entry.pack()
#         tk.Label(self.main_content, text="Complaint:").pack()
#         complaint_entry = tk.Entry(self.main_content, width=50)
#         complaint_entry.pack()

#         def submit():
#             student = name_entry.get()
#             msg = complaint_entry.get()
#             if not student or not msg:
#                 messagebox.showerror("Missing", "Enter name and complaint.")
#                 return
#             con = connect_db()
#             cur = con.cursor()
#             cur.execute("INSERT INTO complaints (student_name, message) VALUES (%s, %s)", (student, msg))
#             con.commit()
#             con.close()
#             messagebox.showinfo("Submitted", "Complaint recorded.")
#             complaint_entry.delete(0, tk.END)

#         tk.Button(self.main_content, text="Submit", command=submit).pack()



import tkinter as tk
from tkinter import ttk, messagebox
from db import connect_db

class DashboardApp:
    def __init__(self, root, role, username=None):
        self.root = root
        self.role = role
        self.username = username  # current logged in student username
        self.root.title(f"{role.capitalize()} Panel - HostelMatrix")
        self.root.geometry("900x600")

        self.sidebar = tk.Frame(self.root, width=200, relief='solid', borderwidth=1)
        self.sidebar.pack(side='left', fill='y')

        self.main_content = tk.Frame(self.root, relief='solid', borderwidth=1)
        self.main_content.pack(side='right', fill='both', expand=True)

        self.add_sidebar_buttons()
        self.load_content("Dashboard")

    def add_sidebar_buttons(self):
        if self.role == "admin":
            options = ["Dashboard", "Add Hostels", "View Available Rooms", "View Student Bookings", "Complaints", "Logout"]
        else:
            options = ["Dashboard", "Book Room", "View Booked Room", "Submit Complaint", "Logout"]

        for option in options:
            button = tk.Button(self.sidebar, text=option, width=20, command=lambda o=option: self.load_content(o))
            button.pack(pady=5)

    def load_content(self, section):
        for widget in self.main_content.winfo_children():
            widget.destroy()

        if section == "Dashboard":
            self.load_dashboard_summary()
        elif section == "Add Hostels" and self.role == "admin":
            self.load_add_hostel()
        elif section == "View Available Rooms" and self.role == "admin":
            self.load_available_rooms()
        elif section == "View Student Bookings" and self.role == "admin":
            self.load_student_bookings()
        elif section == "Complaints" and self.role == "admin":
            self.load_complaints()
        elif section == "Book Room" and self.role == "student":
            self.load_booking_section()
        elif section == "Submit Complaint" and self.role == "student":
            self.load_complaint_form()
        elif section == "View Booked Room" and self.role == "student":
            self.load_booked_room()
        elif section == "Logout":
            self.root.destroy()
            import main
            main.main_window()

    def load_dashboard_summary(self):
        tk.Label(self.main_content, text="Dashboard Overview", font=("Arial", 18, "bold")).pack(pady=20)

        con = connect_db()
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) FROM hostels")
        hostel_count = cur.fetchone()[0]

        cur.execute("SELECT COUNT(*) FROM complaints")
        complaint_count = cur.fetchone()[0]

        cur.execute("SELECT COUNT(*) FROM bookings")
        booking_count = cur.fetchone()[0]
        con.close()

        card_frame = tk.Frame(self.main_content)
        card_frame.pack(pady=10, padx=20, fill="x")

        def create_card(parent, title, count, bg_color):
            card = tk.Frame(parent, bg=bg_color, width=200, height=100, bd=2, relief="groove")
            card.pack(side="left", padx=15, pady=10, expand=True, fill="both")
            tk.Label(card, text=title, font=("Arial", 14, "bold"), bg=bg_color, fg="white").pack(pady=(10, 0))
            tk.Label(card, text=str(count), font=("Arial", 24, "bold"), bg=bg_color, fg="white").pack(pady=(5, 10))

        create_card(card_frame, "Total Hostels", hostel_count, "#3498db")
        create_card(card_frame, "Total Bookings", booking_count, "#2ecc71")
        create_card(card_frame, "Total Complaints", complaint_count, "#e74c3c")

    def load_add_hostel(self):
        tk.Label(self.main_content, text="Add New Hostel", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.main_content, text="Hostel Name").pack()
        name_entry = tk.Entry(self.main_content)
        name_entry.pack()

        tk.Label(self.main_content, text="AC (Yes/No)").pack()
        ac_var = tk.StringVar(value="no")
        ac_frame = tk.Frame(self.main_content)
        ac_frame.pack()
        tk.Radiobutton(ac_frame, text="Yes", variable=ac_var, value="yes").pack(side='left', padx=10)
        tk.Radiobutton(ac_frame, text="No", variable=ac_var, value="no").pack(side='left', padx=10)

        tk.Label(self.main_content, text="Total Rooms").pack()
        room_entry = tk.Entry(self.main_content)
        room_entry.pack()

        def add_hostel():
            name = name_entry.get()
            ac = ac_var.get()
            try:
                total = int(room_entry.get())
            except ValueError:
                messagebox.showerror("Invalid", "Total rooms must be a number.")
                return

            if not name:
                messagebox.showerror("Invalid", "Hostel name is required.")
                return

            is_ac = 1 if ac == "yes" else 0

            con = connect_db()
            cur = con.cursor()
            try:
                cur.execute("INSERT INTO hostels (hostel_name, is_ac, total_rooms, available_rooms) VALUES (%s, %s, %s, %s)",
                            (name, is_ac, total, total))
                con.commit()
                messagebox.showinfo("Success", "Hostel added successfully.")
            except Exception as e:
                messagebox.showerror("Database Error", str(e))
            finally:
                con.close()

            name_entry.delete(0, tk.END)
            room_entry.delete(0, tk.END)
            ac_var.set("no")

        tk.Button(self.main_content, text="Add Hostel", command=add_hostel).pack(pady=10)

    def load_available_rooms(self):
        tk.Label(self.main_content, text="Available Rooms", font=("Arial", 14)).pack(pady=10)
        tree = ttk.Treeview(self.main_content, columns=("ID", "Hostel Name", "AC", "Total", "Available"), show='headings')
        for col in tree["columns"]:
            tree.heading(col, text=col)
        tree.pack(fill='both', expand=True)

        con = connect_db()
        cur = con.cursor()
        cur.execute("SELECT * FROM hostels WHERE available_rooms > 0")
        for row in cur.fetchall():
            tree.insert('', 'end', values=row)
        con.close()

    def load_student_bookings(self):
        tk.Label(self.main_content, text="Student Bookings", font=("Arial", 14)).pack(pady=10)
        tree = ttk.Treeview(self.main_content, columns=("Booking ID", "Student", "Hostel ID", "Room"), show='headings')
        for col in tree["columns"]:
            tree.heading(col, text=col)
        tree.pack(fill='both', expand=True)

        con = connect_db()
        cur = con.cursor()
        cur.execute("SELECT * FROM bookings")
        for row in cur.fetchall():
            tree.insert('', 'end', values=row)
        con.close()

    def load_complaints(self):
        tk.Label(self.main_content, text="Complaints", font=("Arial", 14)).pack()
        tree = ttk.Treeview(self.main_content, columns=("ID", "Student", "Message", "Status"), show='headings')
        for col in tree["columns"]:
            tree.heading(col, text=col)
        tree.pack(pady=10, fill='x')

        con = connect_db()
        cur = con.cursor()
        cur.execute("SELECT * FROM complaints")
        for row in cur.fetchall():
            tree.insert('', 'end', values=row)
        con.close()

        def update_status():
            selected = tree.focus()
            if not selected:
                messagebox.showerror("Error", "Please select a complaint to update.")
                return
            values = tree.item(selected, 'values')
            complaint_id = values[0]
            new_status = status_var.get()
            con = connect_db()
            cur = con.cursor()
            cur.execute("UPDATE complaints SET status=%s WHERE id=%s", (new_status, complaint_id))
            con.commit()
            con.close()
            tree.item(selected, values=(values[0], values[1], values[2], new_status))
            messagebox.showinfo("Success", "Complaint status updated.")

        status_var = tk.StringVar()
        status_dropdown = ttk.Combobox(self.main_content, textvariable=status_var, values=["Pending", "In Progress", "Resolved"])
        status_dropdown.pack()
        tk.Button(self.main_content, text="Update Status", command=update_status).pack(pady=5)

    def load_booking_section(self):
        tk.Label(self.main_content, text="Enter Your Name:").pack()
        name_entry = tk.Entry(self.main_content)
        name_entry.pack()

        tree = ttk.Treeview(self.main_content, columns=("ID", "Name", "AC", "Total", "Available"), show='headings')
        for col in tree["columns"]:
            tree.heading(col, text=col)
        tree.pack(pady=10, fill='x')

        def refresh():
            for row in tree.get_children():
                tree.delete(row)
            con = connect_db()
            cur = con.cursor()
            cur.execute("SELECT * FROM hostels")
            for row in cur.fetchall():
                tree.insert('', 'end', values=row)
            con.close()

        def book():
            selected = tree.focus()
            student = name_entry.get()
            if not selected or not student:
                messagebox.showerror("Error", "Select a hostel and enter your name.")
                return
            values = tree.item(selected, 'values')
            hostel_id, total, available = values[0], int(values[3]), int(values[4])
            if available <= 0:
                messagebox.showerror("Full", "No rooms available.")
                return
            room_number = total - available + 1
            con = connect_db()
            cur = con.cursor()
            cur.execute("INSERT INTO bookings (student_name, hostel_id, room_number) VALUES (%s, %s, %s)",
                        (student, hostel_id, room_number))
            cur.execute("UPDATE hostels SET available_rooms = available_rooms - 1 WHERE id = %s", (hostel_id,))
            con.commit()
            con.close()
            refresh()
            messagebox.showinfo("Success", f"Room {room_number} booked!")

        tk.Button(self.main_content, text="Refresh", command=refresh).pack()
        tk.Button(self.main_content, text="Book Room", command=book).pack()
        refresh()

    def load_complaint_form(self):
        tk.Label(self.main_content, text="Enter Your Name:").pack()
        name_entry = tk.Entry(self.main_content)
        name_entry.pack()
        tk.Label(self.main_content, text="Complaint:").pack()
        complaint_entry = tk.Entry(self.main_content, width=50)
        complaint_entry.pack()

        def submit():
            student = name_entry.get()
            msg = complaint_entry.get()
            if not student or not msg:
                messagebox.showerror("Missing", "Enter name and complaint.")
                return
            con = connect_db()
            cur = con.cursor()
            cur.execute("INSERT INTO complaints (student_name, message) VALUES (%s, %s)", (student, msg))
            con.commit()
            con.close()
            messagebox.showinfo("Submitted", "Complaint recorded.")
            complaint_entry.delete(0, tk.END)

        tk.Button(self.main_content, text="Submit", command=submit).pack()

    def load_booked_room(self):
        tk.Label(self.main_content, text="Your Booked Room", font=("Arial", 14)).pack(pady=10)

        if not self.username:
            tk.Label(self.main_content, text="Username not found in session.").pack()
            return

        con = connect_db()
        cur = con.cursor()
        cur.execute("""
            SELECT b.booking_id, h.hostel_name, b.room_number 
            FROM bookings b
            JOIN hostels h ON b.hostel_id = h.id
            WHERE b.student_name = %s
            ORDER BY b.booking_id DESC LIMIT 1
        """, (self.username,))
        result = cur.fetchone()
        con.close()

        if result:
            booking_id, hostel_name, room_number = result
            tk.Label(self.main_content, text=f"Booking ID: {booking_id}").pack(pady=5)
            tk.Label(self.main_content, text=f"Hostel Name: {hostel_name}").pack(pady=5)
            tk.Label(self.main_content, text=f"Room Number: {room_number}").pack(pady=5)
        else:
            tk.Label(self.main_content, text="No room booked yet.").pack()

