import pyodbc as py
from database.connection import conn


class SignupController:
    new_user_id = None

    @staticmethod
    def submit(fname, lname, address, phone_no, cpassword):
        if len(cpassword) < 8:
            print("Password must be greater than or equal 8 characters.")
            return False

        if len(phone_no) != 11 or  not (phone_no.startswith("01")):
            print("Phone number must be 11 characters.")
            return False
        try:
            cursor = conn.cursor()
            cursor.execute(
                "{CALL AddUser (?, ?, ?, ?, ?)}", fname, lname, address, phone_no, cpassword
            )
            conn.commit()
            check = cursor.rowcount
            cursor = conn.cursor()
            cursor.execute("select dbo.GetLastUserID() as alo")
            new_user_id = cursor.fetchone()[0]
            print(new_user_id)
            SignupController.new_user_id = new_user_id
        except py.Error as ex:
            sqlstate = ex.args[0]
            if sqlstate == '42000':  # This is the SQL Server error code for RAISERROR
                return False
            else:
                print("A database error occurred:", ex)

        print("User added successfully.")
        return True
