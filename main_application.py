import tkinter as tk
from login_gui import create_login_page
from signup_gui import create_signup_page
from functions import show_login_page, show_signup_page

# from home_gui import create_home_page


def show_login_page():
    login_frame.pack(fill="both", expand=True)
    signup_frame.pack_forget()
    # home_frame.pack_forget()


def show_signup_page():
    signup_frame.pack(fill="both", expand=True)
    login_frame.pack_forget()
    print("hello")
    # home_frame.pack_forget()


# def show_home_page():
#     home_frame.pack(fill="both", expand=True)
#     login_frame.pack_forget()
#     signup_frame.pack_forget()

# Create the main window
root = tk.Tk()
root.title("Train Management System")

# Create frames for login, signup, and home pages
login_frame = create_login_page(root)
signup_frame = create_signup_page(root)
# home_frame = create_home_page(root)

# Initially, show the login page
show_login_page()

# Run the Tkinter event loop
root.mainloop()
