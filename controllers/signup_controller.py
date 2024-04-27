import pyodbc as py
from database.connection import conn


class SignupController:
    new_user_id = None

    @staticmethod
    def submit(fname, lname, address, phone_no, cpassword):
        if len(cpassword) < 8:
            print("Password must be greater than or equal 8 characters.")
            return False

        if len(phone_no) != 11:
            print("Phone number must be 11 characters.")
            return False

        cursor = conn.cursor()
        cursor.execute(
            "{CALL AddUser (?, ?, ?, ?, ?)}", fname, lname, address, phone_no, cpassword
        )
        conn.commit()
        cursor = conn.cursor()
        cursor.execute("select dbo.GetLastUserID() as alo")
        new_user_id = cursor.fetchone()[0]
        print(new_user_id)
        SignupController.new_user_id = new_user_id

        print("User added successfully.")
        return True
