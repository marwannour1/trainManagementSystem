import pyodbc as py
from database.connection import conn

class LoginController:
    def __init__(self):
        pass

    def show_signup_page(self):
        # Implement the logic to show the sign-up page
        print("Showing sign-up page")

    def login_user(self, email_tf, pwd_tf):
        user_id = email_tf.get()
        password = pwd_tf.get()

        select = f"SELECT * FROM GetCustomerByIDAndPassword(? , ?)"
        args = (user_id, password)

        cursor = conn.cursor()
        cursor.execute(select, args)

        result = cursor.fetchone()
        if result:
            print("Login successful")
        else:
            print("Login failed")

        # Add code to navigate to the sign-up page

