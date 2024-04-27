import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from controllers.signup_controller import SignupController


class SignupPage:
    def __init__(self, root):
        self.root = root
        self.signup_frame = self.create_signup_page(root)

    def create_signup_page(self, root):
        signUp_frame = tk.Frame(root)

        # Style the application
        style = ttk.Style()
        style.theme_use("clam")  # Use the 'clam' theme for a modern look
        style.configure("TLabel", font=("Arial", 12), background="white")
        style.configure(
            "TButton", font=("Arial", 12), background="#007BFF", foreground="white"
        )
        style.configure("TEntry", font=("Arial", 12), background="white")

        # Create the sign-up form
        username_label = ttk.Label(signUp_frame, text="First Name")
        username_entry = ttk.Entry(signUp_frame)
        lastname_label = ttk.Label(signUp_frame, text="Last Name")
        lastname_entry = ttk.Entry(signUp_frame)
        address_label = ttk.Label(signUp_frame, text="Address")
        address_entry = ttk.Entry(signUp_frame)
        phone_label = ttk.Label(signUp_frame, text="Phone Number")
        phone_entry = ttk.Entry(signUp_frame)
        password_label = ttk.Label(signUp_frame, text="Password")
        password_entry = ttk.Entry(
            signUp_frame, show="*"
        )  # Show '*' instead of actual characters for password

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

        submit_button = ttk.Button(
            signUp_frame,
            text="Submit",
            command=lambda: self.submitLogic(
                username_entry.get(),
                lastname_entry.get(),
                address_entry.get(),
                phone_entry.get(),
                password_entry.get(),
            ),
        )
        submit_button.grid(row=5, column=1, padx=10, pady=10)

        return_button = ttk.Button(
            signUp_frame,
            text="Return to Login",
            command=self.show_login_page,
        )
        return_button.grid(row=6, column=1, padx=10, pady=10)

        return signUp_frame

    def submitLogic(
        self, username_entry, lastname_entry, address_entry, phone_entry, password_entry
    ):
        success = SignupController.submit(
            username_entry, lastname_entry, address_entry, phone_entry, password_entry
        )

        if success:
            messagebox.showinfo(
                "Success",
                "User added successfully. your ID is: "
                + str(SignupController.new_user_id),
            )
            self.show_login_page()

    def show_login_page(self):
        from login_gui import LoginPage

        self.signup_frame.pack_forget()  # Hide the signup frame
        self.login_page = LoginPage(self.root)
        self.login_page.login_frame.pack(fill="both", expand=True)
