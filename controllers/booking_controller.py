import pyodbc as py
from database.connection import conn
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class BookingController:

    @staticmethod
    def book_now(date_entry, ticket_entry, available_seats):
        selected_date = date_entry.get_date()
        ticket_count_str = ticket_entry.get()
        if ticket_count_str.isdigit() and int(ticket_count_str) > 0:
            ticket_count = int(ticket_count_str)
            if selected_date and ticket_count <= available_seats:
                # Simulate booking logic
                booking_successful = (
                    True  # Change this based on your actual booking logic
                )
                if booking_successful:
                    messagebox.showinfo("Success", "Booking successful!")
                else:
                    messagebox.showerror("Error", "Booking failed. Please try again.")
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
