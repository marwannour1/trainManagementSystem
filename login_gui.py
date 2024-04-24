import tkinter as tk
from tkinter import *
import pyodbc as py

from database.connection import conn


def create_login_page(root):

    f = ("Times", 14)

    left_frame = Frame(root, bd=2, bg="#CCCCCC", relief=SOLID, padx=10, pady=10)

    Label(left_frame, text="Enter ID", bg="#CCCCCC", font=f).grid(
        row=0, column=0, sticky=W, pady=10
    )

    Label(left_frame, text="Enter Password", bg="#CCCCCC", font=f).grid(
        row=1, column=0, pady=10
    )

    email_tf = Entry(left_frame, font=f)
    pwd_tf = Entry(left_frame, font=f, show="*")
    login_btn = Button(
        left_frame,
        width=15,
        text="Login",
        font=f,
        relief=SOLID,
        cursor="hand2",
        command=lambda: login_user(email_tf, pwd_tf),
    )

    signup_btn = Button(
        left_frame,
        width=15,
        text="Sign Up",
        font=f,
        relief=SOLID,
        cursor="hand2",
        command=show_signup_page,
    )

    email_tf.grid(row=0, column=1, pady=10, padx=20)
    pwd_tf.grid(row=1, column=1, pady=10, padx=20)
    login_btn.grid(row=2, column=1, pady=10, padx=20)
    signup_btn.grid(row=3, column=1, pady=10, padx=20)  # Position the sign-up button

    return left_frame


def login_user(email_tf, pwd_tf):
    user_id = email_tf.get()
    password = pwd_tf.get()

    select = f"SELECT * FROM GetCustomerByIDAndPassword(? , ?)"
    args = (user_id, password)

    cursor = conn.cursor()
    cursor.execute(select, args)

    result = cursor.fetchone()
    if result:
        show_signup_page()
        print("Login successful")

    else:
        print("Login failed")

    # Add code to navigate to the sign-up page

    print("Navigating to sign-up page")


def show_signup_page():
    print("hi")
