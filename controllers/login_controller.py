import pyodbc as py
from database.connection import conn


class LoginController:
    @staticmethod
    def login(email_tf, pwd_tf):
        user_id = email_tf.get()
        password = pwd_tf.get()

        select = f"SELECT * FROM GetCustomerByIDAndPassword(? , ?)"
        args = (user_id, password)

        cursor = conn.cursor()
        cursor.execute(select, args)

        result = cursor.fetchone()
        if result:
            print("Login successful")
            return True
            # Add code to navigate to the next page
        else:
            print("Login failed")
            return False
