import tkinter as tk
from login_gui import LoginPage
from signup_gui import SignupPage


def main():
    root = tk.Tk()
    root.title("Login and Signup System")

    SignUp_page = SignupPage(root)
    SignUp_page.show_login_page()

    root.mainloop()


if __name__ == "__main__":
    main()
