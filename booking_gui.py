import tkinter as tk
from tkinter import ttk
from controllers.booking_controller import BookingController


class BookingPage:
    def __init__(self, root):
        self.root = root
        self.train_id = 6  # Example train ID
        self.booking_frame = self.create_booking_frame(root)

    def create_booking_frame(self, root):
        # Create a frame to contain all the booking elements
        booking_frame = ttk.Frame(root)

        # Load available seats and trip information for the selected train
        available_seats_and_info = BookingController.load_available_seats_and_trip_info(
            self.train_id
        )

        # Create a label to display the selected trip information
        selected_trip_info_label = tk.Label(booking_frame, text="")
        selected_trip_info_label.grid(row=0, column=0, padx=10, pady=10)

        # Update the label with the selected trip information
        if available_seats_and_info:
            (
                seat_id,
                price,
                departure_time,
                arrival_time,
                station_from,
                station_to,
                total_seats,
            ) = available_seats_and_info[0]
            selected_trip_info_label.config(
                text=f"Departure: {departure_time}, Arrival: {arrival_time}, From: {station_from}, To: {station_to}, Seats Available: {total_seats}"
            )

        # Create a dropdown menu for selecting a seat
        seat_var = tk.StringVar(booking_frame)
        seat_var.set(available_seats_and_info[0][0])  # Default value
        seat_menu = ttk.Combobox(
            booking_frame,
            textvariable=seat_var,
            values=[
                f"{seat[0]} - Price: {seat[1]}" for seat in available_seats_and_info
            ],
        )
        seat_menu.grid(row=1, column=0, padx=10, pady=10)

        # Book button

        book_button = ttk.Button(
            booking_frame,
            text="Book Seat",
            command=lambda: self.on_book_click(seat_var),
        )
        book_button.grid(row=2, column=0, padx=10, pady=10)

        return booking_frame

    def on_book_click(self, seat_var):
        seat_id = seat_var.get().split(" - ")[
            0
        ]  # Extract seat ID from the selected option
        success = BookingController.book_seat(seat_id)
        if success:
            print(f"Seat {seat_id} booked successfully.")
            # Here, you would proceed with the booking process
