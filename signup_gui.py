import tkinter as tk
from tkinter import ttk

class SignUpPage:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.create_signup_page()

    def create_signup_page(self):
        signUp_frame = tk.Frame(self.root)

        # Style the application
        style = ttk.Style()
        style.theme_use("clam") # Use the 'clam' theme for a modern look
        style.configure("TLabel", font=("Arial", 12), background="white")
        style.configure("TButton", font=("Arial", 12), background="#007BFF", foreground="white")
        style.configure("TEntry", font=("Arial", 12), background="white")

        # Create the sign-up form
        self.username_label = ttk.Label(signUp_frame, text="First Name")
        self.username_entry = ttk.Entry(signUp_frame)
        self.lastname_label = ttk.Label(signUp_frame, text="Last Name")
        self.lastname_entry = ttk.Entry(signUp_frame)
        self.address_label = ttk.Label(signUp_frame, text="Address")
        self.address_entry = ttk.Entry(signUp_frame)
        self.phone_label = ttk.Label(signUp_frame, text="Phone Number")
        self.phone_entry = ttk.Entry(signUp_frame)
        self.password_label = ttk.Label(signUp_frame, text="Password")
        self.password_entry = ttk.Entry(signUp_frame, show="*") # Show '*' instead of actual characters for password

        # Position the labels and entries
        self.username_label.grid(row=0, column=0, padx=10, pady=10)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)
        self.lastname_label.grid(row=1, column=0, padx=10, pady=10)
        self.lastname_entry.grid(row=1, column=1, padx=10, pady=10)
        self.address_label.grid(row=2, column=0, padx=10, pady=10)
        self.address_entry.grid(row=2, column=1, padx=10, pady=10)
        self.phone_label.grid(row=3, column=0, padx=10, pady=10)
        self.phone_entry.grid(row=3, column=1, padx=10, pady=10)
        self.password_label.grid(row=4, column=0, padx=10, pady=10)
        self.password_entry.grid(row=4, column=1, padx=10, pady=10)

        submit_button = ttk.Button(signUp_frame, text="Submit", command=self.submit)
        submit_button.grid(row=5, column=1, padx=10, pady=10)

        signUp_frame.pack()

    def submit(self):
        self.controller.submit(self.username_entry, self.lastname_entry, self.address_entry, self.phone_entry, self.password_entry)
