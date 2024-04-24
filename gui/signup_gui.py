import tkinter as tk
from tkinter import ttk
import pyodbc as py

conn = py.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-23V77CE;"
    "Database=TrainManagementSys;"
    "Trusted_Connection=yes;"
)

# Establish a connection
cursor = conn.cursor()

# Create the main window
root = tk.Tk()
root.title("Sign Up")
root.geometry("400x400")

# Style the application
style = ttk.Style()
style.theme_use('clam') # Use the 'clam' theme for a modern look
style.configure('TLabel', font=('Arial', 12), background='white')
style.configure('TButton', font=('Arial', 12), background='#007BFF', foreground='white')
style.configure('TEntry', font=('Arial', 12), background='white')

# Create the sign-up form
username_label = ttk.Label(root, text="First Name")
username_entry = ttk.Entry(root)
lastname_label = ttk.Label(root, text="Last Name")
lastname_entry = ttk.Entry(root)
address_label = ttk.Label(root, text="Address")
address_entry = ttk.Entry(root)
phone_label = ttk.Label(root, text="Phone Number")
phone_entry = ttk.Entry(root)
password_label = ttk.Label(root, text="Password")
password_entry = ttk.Entry(root, show="*") # Show '*' instead of actual characters for password

# Position the labels and entries
username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry.grid(row=0, column=1, padx=10, pady=10)
lastname_label.grid(row=1, column=0, padx=10, pady=10)
lastname_entry.grid(row=1, column=1, padx=10, pady=10)
address_label.grid(row=2, column=0, padx=10, pady=10)
address_entry.grid(row=2, column=1, padx=10, pady=10)
phone_label.grid(row=3, column=0, padx=10, pady=10)
phone_entry.grid(row=3, column=1, padx=10, pady=10)
password_label.grid(row=4, column=0, padx=10, pady=10)
password_entry.grid(row=4, column=1, padx=10, pady=10)

# Add a submit button
def submit():
    # Get the user's input
    fname = username_entry.get()
    lname = lastname_entry.get()  # Get last name from lastname_entry field
    address = address_entry.get()
    phone_no = phone_entry.get()
    cpassword = password_entry.get()  # Get password from password_entry field

    # Call the stored procedure to add the user
    cursor.execute("{CALL AddUser (?, ?, ?, ?, ?)}", fname, lname, address, phone_no, cpassword)
    conn.commit()

    # Close the connection
    cursor.close()
    conn.close()

    print("User added successfully.")

submit_button = ttk.Button(root, text="Submit", command=submit)
submit_button.grid(row=5, column=1, padx=10, pady=10)

# Run the application
root.mainloop()
