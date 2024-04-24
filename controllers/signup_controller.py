import pyodbc as py
from database.connection import conn

class SignUpController:
    def __init__(self):
        self.cursor = conn.cursor()

    def submit(self, username_entry, lastname_entry, address_entry, phone_entry, password_entry):
        # Get the user's input
        fname = username_entry.get()
        lname = lastname_entry.get() # Get last name from lastname_entry field
        address = address_entry.get()
        phone_no = phone_entry.get()
        cpassword = password_entry.get() # Get password from password_entry field

        # Call the stored procedure to add the user
        self.cursor.execute("{CALL AddUser (?, ?, ?, ?, ?)}", fname, lname, address, phone_no, cpassword)
        conn.commit()

        # Close the connection
        self.cursor.close()
        conn.close()

        print("User added successfully.")
