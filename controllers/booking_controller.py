import pyodbc as py
from database.connection import conn
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from controllers.home_controller import HomeController
from controllers.login_controller import LoginController

class BookingController:
    @staticmethod
    def get_available_seats():
       select= "SELECT dbo.get_free_seats(?, ?) AS free_seats"  # SQL query to call the user-defined function
       args = ('2024-05-01', HomeController.route_id)  # Parameters for the function call
       cursor = conn.cursor()
        # Execute the SQL query with parameters
       cursor.execute(select, args)

        # Fetch the result of the query
       result = cursor.fetchone()

       if result:
            return result[0] # Assuming the function returns a single value
       else:
            return None # Or handle the case where no result is returned
    @staticmethod
    def book_now(date_entry, ticket_entry, available_seats):
        selected_date = date_entry.get_date()
        selected_date_str = selected_date.strftime('%Y-%m-%d')
        print(type(selected_date_str))
        ticket_count_str = ticket_entry.get()
        if ticket_count_str.isdigit() and int(ticket_count_str) > 0:
            ticket_count = int(ticket_count_str)
            if selected_date and ticket_count <= available_seats:
                print(selected_date, ticket_count)
                cursor = conn.cursor()
                select = "{CALL InsertTicket (?, ?, ?)}"
                args = (selected_date_str, LoginController.loginID, HomeController.route_id)
                cursor.execute(select, args)
                conn.commit()
            
            else:
                messagebox.showerror(
                    "Error",
                    "Please select a date or the number of tickets exceeds available seats.",
                )
        else:
            messagebox.showerror(
                "Error", "Please enter a valid number of tickets greater than 0."
            )
        return False
