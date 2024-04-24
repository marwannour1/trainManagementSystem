import tkinter as tk
from tkinter import *

class LoginPage:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.create_login_page()

    def create_login_page(self):
        f = ("Times", 14)

        left_frame = Frame(self.root, bd=2, bg="#CCCCCC", relief=SOLID, padx=10, pady=10)

        Label(left_frame, text="Enter ID", bg="#CCCCCC", font=f).grid(row=0, column=0, sticky=W, pady=10)
        Label(left_frame, text="Enter Password", bg="#CCCCCC", font=f).grid(row=1, column=0, pady=10)

        self.email_tf = Entry(left_frame, font=f)
        self.pwd_tf = Entry(left_frame, font=f, show="*")
        login_btn = Button(left_frame, width=15, text="Login", font=f, relief=SOLID, cursor="hand2", command=self.login_user)
        signup_btn = Button(left_frame, width=15, text="Sign Up", font=f, relief=SOLID, cursor="hand2", command=self.controller.show_signup_page)

        self.email_tf.grid(row=0, column=1, pady=10, padx=20)
        self.pwd_tf.grid(row=1, column=1, pady=10, padx=20)
        login_btn.grid(row=2, column=1, pady=10, padx=20)
        signup_btn.grid(row=3, column=1, pady=10, padx=20)

        left_frame.pack()

    def login_user(self):
        self.controller.login_user(self.email_tf, self.pwd_tf)
