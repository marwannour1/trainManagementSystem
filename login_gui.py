import tkinter as tk
from controllers.login_controller import LoginController


class LoginPage:
    def __init__(self, root):
        self.root = root
        self.login_frame = self.create_login_page(root)

    def create_login_page(self, root):
        f = ("Times", 14)
        login_frame = tk.Frame(
            root, bd=2, bg="#CCCCCC", relief=tk.SOLID, padx=10, pady=10
        )

        tk.Label(login_frame, text="Enter ID", bg="#CCCCCC", font=f).grid(
            row=0, column=0, sticky=tk.W, pady=10
        )
        tk.Label(login_frame, text="Enter Password", bg="#CCCCCC", font=f).grid(
            row=1, column=0, pady=10
        )

        email_tf = tk.Entry(login_frame, font=f)
        pwd_tf = tk.Entry(login_frame, font=f, show="*")
        login_btn = tk.Button(
            login_frame,
            width=15,
            text="Login",
            font=f,
            relief=tk.SOLID,
            cursor="hand2",
            command=lambda: self.loginLogic(email_tf, pwd_tf),
        )
        signup_btn = tk.Button(
            login_frame,
            width=15,
            text="Sign Up",
            font=f,
            relief=tk.SOLID,
            cursor="hand2",
            command=self.show_signup_page,
        )

        email_tf.grid(row=0, column=1, pady=10, padx=20)
        pwd_tf.grid(row=1, column=1, pady=10, padx=20)
        login_btn.grid(row=2, column=1, pady=10, padx=20)
        signup_btn.grid(row=3, column=1, pady=10, padx=20)

        return login_frame

    def loginLogic(self, email_tf, pwd_tf):
        success = LoginController.login(email_tf, pwd_tf)

        if success:
            self.show_home_page()
        else:
            tk.messagebox.showerror("Error", "Invalid ID or Password")

    def show_signup_page(self):
        from signup_gui import SignupPage

        self.login_frame.pack_forget()  # Hide the login frame
        self.signup_page = SignupPage(self.root)
        self.signup_page.signup_frame.pack(fill="both", expand=True)

    def show_home_page(self):
        from home_gui import HomePage
        from controllers.home_controller import HomeController

        self.login_frame.pack_forget()
        self.home_controller = HomeController()
        self.home_page = HomePage(self.root, self.home_controller)
