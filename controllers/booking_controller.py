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
        cursor = conn.cursor()
        # Correctly call the function in a SELECT statement and pass parameters
        cursor.execute("SELECT dbo.get_free_seats(?, ?) ")
        args= (HomeController.route_ID, "2024-6-6")
        row = cursor.fetchone()
        if row:
            return row[0] # Assuming the function returns a single value
        else:
            return None # Or handle the case where no result is returned
    @staticmethod
    def book_now(date_entry, ticket_entry, available_seats):
        selected_date = date_entry.get_date()
        ticket_count_str = ticket_entry.get()
        if ticket_count_str.isdigit() and int(ticket_count_str) > 0:
            ticket_count = int(ticket_count_str)
            if selected_date and ticket_count <= available_seats:
                 cursor = conn.cursor()
                 # Use a more standard syntax for calling stored procedures
                 cursor.execute("{CALL InsertTicket (?, ?, ?)}", (selected_date, LoginController.loginID, HomeController.route_id))
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
