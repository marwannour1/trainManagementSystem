import pyodbc as py
from database.connection import conn


class SignupController:
    @staticmethod
    def submit(fname, lname, address, phone_no, cpassword):
        cursor = conn.cursor()
        cursor.execute(
            "{CALL AddUser (?, ?, ?, ?, ?)}", fname, lname, address, phone_no, cpassword
        )
        conn.commit()

        print("User added successfully.")
        return True
