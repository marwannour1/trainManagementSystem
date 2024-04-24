import tkinter as tk
from tkinter import messagebox


def show_login_page():
    login_frame.pack(fill="both", expand=True)
    signup_frame.pack_forget()
    home_frame.pack_forget()


def show_signup_page():
    signup_frame.pack(fill="both", expand=True)
    login_frame.pack_forget()
    home_frame.pack_forget()


def show_home_page():
    home_frame.pack(fill="both", expand=True)
    login_frame.pack_forget()
    signup_frame.pack_forget()


def login_attempt():
    username = username_entry.get()
    password = password_entry.get()
    # Placeholder for actual authentication logic
    messagebox.showinfo("Login", "Login successful!")
    show_home_page()


def signup_attempt():
    # Placeholder for signup logic
    messagebox.showinfo("Signup", "Signup successful!")
    show_login_page()


# Create the main window
root = tk.Tk()
root.title("Train Management System")

# Create frames for login, signup, and home pages
login_frame = tk.Frame(root)
signup_frame = tk.Frame(root)
home_frame = tk.Frame(root)

# Login page widgets
username_label = tk.Label(login_frame, text="Username")
username_label.pack()
username_entry = tk.Entry(login_frame)
username_entry.pack()

password_label = tk.Label(login_frame, text="Password")
password_label.pack()
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack()

login_button = tk.Button(login_frame, text="Login", command=login_attempt)
login_button.pack()

signup_button = tk.Button(login_frame, text="Signup", command=show_signup_page)
signup_button.pack()

# Signup page widgets
signup_label = tk.Label(signup_frame, text="Signup")
signup_label.pack()

name_label = tk.Label(signup_frame, text="Full Name")
name_label.pack()
name_entry = tk.Entry(signup_frame)
name_entry.pack()

email_label = tk.Label(signup_frame, text="Email")
email_label.pack()
email_entry = tk.Entry(signup_frame)
email_entry.pack()

password_label = tk.Label(signup_frame, text="Password")
password_label.pack()
password_entry = tk.Entry(signup_frame, show="*")
password_entry.pack()

signup_submit_button = tk.Button(signup_frame, text="Submit", command=signup_attempt)
signup_submit_button.pack()

# Home page widgets
home_label = tk.Label(home_frame, text="Welcome to the Home Page!")
home_label.pack()

# Initially, show the login page
show_login_page()

# Run the Tkinter event loop
root.mainloop()
import tkinter as tk
from tkinter import messagebox


def show_login_page():
    login_frame.pack(fill="both", expand=True)
    signup_frame.pack_forget()
    home_frame.pack_forget()


def show_signup_page():
    signup_frame.pack(fill="both", expand=True)
    login_frame.pack_forget()
    home_frame.pack_forget()


def show_home_page():
    home_frame.pack(fill="both", expand=True)
    login_frame.pack_forget()
    signup_frame.pack_forget()


def login_attempt():
    username = username_entry.get()
    password = password_entry.get()
    # Placeholder for actual authentication logic
    messagebox.showinfo("Login", "Login successful!")
    show_home_page()


def signup_attempt():
    # Placeholder for signup logic
    messagebox.showinfo("Signup", "Signup successful!")
    show_login_page()


# Create the main window
root = tk.Tk()
root.title("Train Management System")

# Create frames for login, signup, and home pages
login_frame = tk.Frame(root)
signup_frame = tk.Frame(root)
home_frame = tk.Frame(root)

# Login page widgets
username_label = tk.Label(login_frame, text="Username")
username_label.pack()
username_entry = tk.Entry(login_frame)
username_entry.pack()

password_label = tk.Label(login_frame, text="Password")
password_label.pack()
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack()

login_button = tk.Button(login_frame, text="Login", command=login_attempt)
login_button.pack()

signup_button = tk.Button(login_frame, text="Signup", command=show_signup_page)
signup_button.pack()

# Signup page widgets
signup_label = tk.Label(signup_frame, text="Signup")
signup_label.pack()

name_label = tk.Label(signup_frame, text="Full Name")
name_label.pack()
name_entry = tk.Entry(signup_frame)
name_entry.pack()

email_label = tk.Label(signup_frame, text="Email")
email_label.pack()
email_entry = tk.Entry(signup_frame)
email_entry.pack()

password_label = tk.Label(signup_frame, text="Password")
password_label.pack()
password_entry = tk.Entry(signup_frame, show="*")
password_entry.pack()

signup_submit_button = tk.Button(signup_frame, text="Submit", command=signup_attempt)
signup_submit_button.pack()

# Home page widgets
home_label = tk.Label(home_frame, text="Welcome to the Home Page!")
home_label.pack()

# Initially, show the login page
show_login_page()

# Run the Tkinter event loop
root.mainloop()
