import tkinter as tk
from tkcalendar import DateEntry
import datetime
from tkinter import ttk
from tkinter import messagebox
from controllers.booking_controller import BookingController
from controllers.home_controller import HomeController

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
       # self.available_seats = BookingController.get_available_seats() # Example variable for available seats
        self.selected_date = None  # Variable to store the selected date
        self.ticket_count = 0  # Variable to store the number of tickets
        self.booking_page = self.setup_gui()

    def setup_gui(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=20, pady=20)

        # available_seats_label = tk.Label(
        #     frame,
        #     text=f"Number of available seats = {self.available_seats}",
        #     font=("Arial", 12),
        # )
        # available_seats_label.pack(pady=10)

        route_label = tk.Label(
            frame,
            text="From {x} station to station {y} with route id {z}".format(
                x=HomeController.station_from, y=HomeController.station_to, z=HomeController.route_id
            ),
            font=("Arial", 12),
        )
        route_label.pack(pady=10)

        self.ticket_entry = tk.Entry(frame, font=("Arial", 12))
        self.ticket_entry.pack(pady=10)
        self.ticket_entry.insert(0, "1")  # Default value

        self.date_entry = CustomDateEntry(frame, width=12, font=("Arial", 12))
        self.date_entry.pack(pady=10)

        book_button = tk.Button(
            frame,
            text="Book Now",
            command=lambda: self.book_now_action(
                self.date_entry, self.ticket_entry
            ),
            font=("Arial", 12),
        )
        book_button.pack(pady=10)

        home_button = tk.Button(
            frame, text="Home", command=self.return_home_page, font=("Arial", 12)
        )
        home_button.pack(pady=10)

        return frame

    def book_now_action(self, date_entry, ticket_count):
        BookingController.book_now(date_entry, ticket_count)

    def return_home_page(self):
        from home_gui import HomePage
        from controllers.home_controller import HomeController

        self.booking_page.pack_forget()
        self.home_controller = HomeController()
        self.home_page = HomePage(self.root, self.home_controller)
