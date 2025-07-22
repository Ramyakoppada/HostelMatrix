
# import mysql.connector

# DB_NAME = "hostelmatrix"

# TABLES = {
#     "hostels": (
#         """
#         CREATE TABLE IF NOT EXISTS hostels (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             name VARCHAR(100),
#             ac BOOLEAN,
#             total_rooms INT,
#             available_rooms INT
#         )
#         """
#     ),
#     "bookings": (
#         """
#         CREATE TABLE IF NOT EXISTS bookings (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             student_name VARCHAR(100),
#             hostel_id INT,
#             room_number INT,
#             FOREIGN KEY (hostel_id) REFERENCES hostels(id) ON DELETE CASCADE
#         )
#         """
#     ),
#     "complaints": (
#         """
#         CREATE TABLE IF NOT EXISTS complaints (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             student_name VARCHAR(100),
#             message TEXT,
#             status VARCHAR(20) DEFAULT 'Pending'
#         )
#         """
#     )
# }

# def connect_db():
#     # Step 1: Connect to MySQL Server (no DB selected yet)
#     root_conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="PWD#sql"  # Change this if needed
#     )
#     root_cursor = root_conn.cursor()

#     # Step 2: Create the database if it doesn't exist
#     root_cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
#     root_cursor.execute(f"USE {DB_NAME}")

#     # Step 3: Create tables if they don't exist
#     for table_name, table_sql in TABLES.items():
#         root_cursor.execute(table_sql)

#     root_conn.commit()
#     root_cursor.close()
#     root_conn.close()

#     # Step 4: Return a connection to the newly created DB
#     return mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="PWD#sql",
#         database=DB_NAME
#     )

# # Optional: Create DB & Tables immediately if script is run directly
# if __name__ == "__main__":
#     connect_db()
#     print("✅ Database and tables created successfully.")


# import mysql.connector

# def connect_db():
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="PWD#sql",  # Change as needed
#         database="hostelmatrix"
#     )
#     return conn

# def setup_database():
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="PWD#sql"
#     )
#     cursor = conn.cursor()
#     cursor.execute("CREATE DATABASE IF NOT EXISTS hostelmatrix")
#     conn.close()

#     conn = connect_db()
#     cursor = conn.cursor()

#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS hostels (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         hostel_name VARCHAR(255),
#         is_ac BOOLEAN,
#         total_rooms INT,
#         available_rooms INT
#     )
#     """)

#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS students (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         student_name VARCHAR(255)
#     )
#     """)

#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS bookings (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         student_name VARCHAR(255),
#         hostel_id INT,
#         room_number INT,
#         FOREIGN KEY (hostel_id) REFERENCES hostels(id)
#     )
#     """)

#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS complaints (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         student_name VARCHAR(255),
#         message TEXT,
#         status VARCHAR(50) DEFAULT 'Pending'
#     )
#     """)

#     conn.commit()
#     conn.close()



# db.py

import mysql.connector

def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="PWD#sql",  # Change as needed
        database="hostelmatrix"
    )
    return conn

def setup_database():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="PWD#sql"
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS hostelmatrix")
    conn.close()

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS hostels (
        id INT AUTO_INCREMENT PRIMARY KEY,
        hostel_name VARCHAR(255),
        is_ac BOOLEAN,
        total_rooms INT,
        available_rooms INT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL
    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bookings (
        id INT AUTO_INCREMENT PRIMARY KEY,
        student_name VARCHAR(255),
        hostel_id INT,
        room_number INT,
        FOREIGN KEY (hostel_id) REFERENCES hostels(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS complaints (
        id INT AUTO_INCREMENT PRIMARY KEY,
        student_name VARCHAR(255),
        message TEXT,
        status VARCHAR(50) DEFAULT 'Pending'
    )
    """)

    conn.commit()
    conn.close()

# Run this once to set up the database
if __name__ == "__main__":
    setup_database()
