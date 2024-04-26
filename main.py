import tkinter as tk
from tkcalendar import DateEntry
import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class CustomDateEntry(DateEntry):
    def __init__(self, master=None, **kw):
        DateEntry.__init__(self, master, **kw)
        self.set_date(datetime.date.today())
        self.bind("<FocusIn>", self.check_date)

    def check_date(self, event):
        if self.get_date() < datetime.date.today():
            self.set_date(datetime.date.today())


class BookingPage:
    def __init__(self, root):
        self.root = root
        self.available_seats = 10  # Example variable for available seats
        self.selected_date = None  # Variable to store the selected date
        self.ticket_count = 0  # Variable to store the number of tickets
        self.setup_gui()

    def setup_gui(self):
        # Create a frame to hold the widgets
        frame = tk.Frame(self.root)
        frame.pack(padx=20, pady=20)

        # Label to display the number of available seats
        available_seats_label = tk.Label(
            frame,
            text=f"Number of available seats = {self.available_seats}",
            font=("Arial", 12),
        )
        available_seats_label.pack(pady=10)

        # Label for train route and ID
        route_label = tk.Label(
            frame,
            text="From {x} station to station {y} on train id {z}".format(
                x="Station A", y="Station B", z="123"
            ),
            font=("Arial", 12),
        )
        route_label.pack(pady=10)

        # Entry for ticket count
        self.ticket_entry = tk.Entry(frame, font=("Arial", 12))
        self.ticket_entry.pack(pady=10)
        self.ticket_entry.insert(0, "1")  # Default value

        # CustomDateEntry widget for date selection
        self.date_entry = CustomDateEntry(frame, width=12, font=("Arial", 12))
        self.date_entry.pack(pady=10)

        # Button to book
        book_button = tk.Button(
            frame, text="Book Now", command=self.book_now, font=("Arial", 12)
        )
        book_button.pack(pady=10)

    def book_now(self):
        self.selected_date = self.date_entry.get_date()
        ticket_count_str = self.ticket_entry.get()
        if ticket_count_str.isdigit() and int(ticket_count_str) > 0:
            self.ticket_count = int(ticket_count_str)
            if self.selected_date and self.ticket_count <= self.available_seats:
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


def main():
    root = tk.Tk()
    root.title("Booking Page")
    BookingPage(root)
    root.mainloop()


if __name__ == "__main__":
    main()
